#Code for transversing AST and parse it into a flow graph. 
#Need to understand code better and change a few things for more efficient vuln analysis in vulnerability_identifier.
import ast
import astor
import astunparse
from Pattern import Pattern
from OutputVulnerability import OutputVulnerability
from FlowGraph import FlowGraph
#def assignment_expression_strategy(curr_tree):
# pass


flowGraph = FlowGraph('root')

def transverse(program_slice): 
    
    print(program_slice["body"])
    print("\n")
    print(program_slice["body"][0]["ast_type"])  #get specific field 
    #print(astor.to_source(program_slice["body"]))
    #return [OutputVulnerability("A","sourceA","sinkA","yes",[]),OutputVulnerability("B","sourceb","sinkB","no",[["one"]])] #just for testing

    build_graph(program_slice)

    return flowGraph



def searchFlowGraph(graph, token, k=10, visited = None):
    # found target graph
    if graph.get_token() == token:
        return graph

    if k == 0 or (visited is not None and token in visited):
        return False

    # reached leaf graph without finding target graph
    if not graph.has_children():
        return False

    # search in children graphs for target graph
    for child in graph.get_children():
        n = searchFlowGraph(child, token, k - 1,[graph] if visited is None else (visited + [graph]))
        if n:
            return n

    return False



def right_to_left_op( left, right):
    """ Appends each of nodes on the left as children of all the right ones """
    # No implicit flows because no sub-graph is created for condition inside if or while
    if not isinstance(left, list):
        left = [left]

    if not isinstance(right, list):
        right = [right]

    left_nodes = []  
    for left_token in left:
        left_node = searchFlowGraph(flowGraph, left_token)
        if not left_node:
            #if(len(left_token) != 0 and left_token[0] == '[' ):
             #   print("true")
                #left_node = FlowGraph(eval(left_token)[0])
            #else:
            left_node = FlowGraph(left_token)
            #print("Left token:", left_token)
        left_nodes.append(left_node)

    for token in right:
        right_node = searchFlowGraph(flowGraph, token)
        if not right_node:  # if graph doesnt exist create a new one
            right_node = FlowGraph(token)
            #print("Token:" , token)

        for left_node in left_nodes:
            # make the left graph a child of the right one
            right_node.add_child(left_node)

        # if the right node has no parent, it becomes a child of root
        if not right_node.has_parents():
            flowGraph.add_child(right_node)




def build_graph(program_slice):
    return build_graph_aux(program_slice["body"])


def build_graph_aux(curr_tree):
    if curr_tree is None:
        return []

    if isinstance(curr_tree, list):
        return build_graph_from_list_aux(curr_tree)

    strategy = strategies[curr_tree['ast_type']]
    if strategy is not None:
        return strategy(curr_tree) 
    else: 
        return []


def build_graph_from_list_aux(curr_tree):
    result_list = []
    for el in curr_tree:
        result = build_graph_aux(el)
        if isinstance(result, list):
            result_list += result
        else:
            result_list.append(result)
    return result_list



def constant(curr_tree):
    return  "" #str(curr_tree['value'])  #Substitui valores de constantes por "" pois estes nao interessam para a identificacao de vulnerabilidades

def name(curr_tree):
    return curr_tree['id']

def expression(curr_tree):
    return build_graph_aux(curr_tree['value'])


def assignment(curr_tree):
    left = str(build_graph_aux(curr_tree['targets']))
    right = build_graph_aux(curr_tree['value'])

    right_to_left_op(left, right if isinstance(right, list) else [right])
    return [left]


def binaryOperation(curr_tree):
    left = build_graph_aux(curr_tree['left'])
    right = build_graph_aux(curr_tree['right'])
    
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]
    return left + right


def functionCall(curr_tree):
    c_name = build_graph_aux(curr_tree['func'])
    args = build_graph_aux(curr_tree['args'])
    if args is None:  
        args = []

    right_to_left_op(c_name, args)
    return c_name


def conditionalStatement(curr_tree):
    test = build_graph_aux(curr_tree['body'])
    consequent = build_graph_aux(curr_tree['orelse'])
    alternate = build_graph_aux(curr_tree['test'])

    right_to_left_op(consequent, test)
    right_to_left_op(alternate, test)
    return [consequent, alternate]


def comparison(curr_tree):
    return build_graph_aux(curr_tree['comparators'])

def whileLoop(curr_tree):
    test = build_graph_aux(curr_tree['test'])
    body = build_graph_aux(curr_tree['body'])
    right_to_left_op(body, test)



strategies = {
    "Constant" : constant, "Name" : name, "Expr" : expression, 
    "Assign" : assignment, "BinOp" : binaryOperation, "Call" : functionCall, 
    "If" : conditionalStatement, "Compare" : comparison, "While" : whileLoop
}