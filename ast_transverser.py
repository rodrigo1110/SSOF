from Pattern import Pattern
from OutputVulnerability import OutputVulnerability
from FlowGraph import FlowGraph


flowGraph = FlowGraph('root')


def transverse(program_slice): 
    buildGraph(program_slice["body"])
    return flowGraph



def searchFlowGraph(graph, name, visited = None):
    if(graph.name == name):
        return graph

    if((visited is not None and name in visited) or (not graph.hasChildren)):
        return False

    for child in graph.children:
        if(visited is None):
            n = searchFlowGraph(child, name, [graph])
        else:
            n = searchFlowGraph(child, name, visited + [graph])
        
        if(n):
            return n
    return False



def createGraph(left, right):
    if(not isinstance(left, list)):
       left = [left]
    if(not isinstance(right, list)):
       right = [right]

    leftGraphs = []  
    for leftName in left:
        leftGraph = searchFlowGraph(flowGraph, leftName)
        if(not leftGraph):
            leftGraph = FlowGraph(leftName)
        leftGraphs.append(leftGraph)

    for rightName in right:
        rightGraph = searchFlowGraph(flowGraph, rightName)
        if(not rightGraph):  
            rightGraph = FlowGraph(rightName)

        for leftGraph in leftGraphs:
            rightGraph.addChild(leftGraph)

        if(not rightGraph.hasParents()):
            flowGraph.addChild(rightGraph)



def buildGraph(internalStruct):
    if(internalStruct is None):
        return []

    if(isinstance(internalStruct, list)):
        return buildGraphList(internalStruct)

    instanceOfType = types[internalStruct['ast_type']]
    if(instanceOfType is not None):
        return instanceOfType(internalStruct) 
    else: 
        return []


def buildGraphList(internalStruct):
    result_list = []
    for el in internalStruct:
        result = buildGraph(el)
        if(isinstance(result, list)):
            result_list += result
        else:
            result_list.append(result)

    return result_list


def constant(internalStruct):
    return  ""

def name(internalStruct):
    return internalStruct['id']

def expression(internalStruct):
    return buildGraph(internalStruct['value'])


def assignment(internalStruct):
    left = str(buildGraph(internalStruct['targets'])) 
    right = buildGraph(internalStruct['value'])

    createGraph(left, right)
    return [left]


def binaryOperation(internalStruct):
    left = buildGraph(internalStruct['left'])
    right = buildGraph(internalStruct['right'])
    
    if(not isinstance(left, list)):
        left = [left]
    if(not isinstance(right, list)):
        right = [right]
    return left + right


def functionCall(internalStruct):
    functionName = buildGraph(internalStruct['func'])
    args = buildGraph(internalStruct['args'])
    if(args is None):  
        args = []

    createGraph(functionName, args)
    return functionName


def conditionalStatement(internalStruct):
    ifBody = buildGraph(internalStruct['body'])
    elseBody = buildGraph(internalStruct['orelse'])
    test = buildGraph(internalStruct['test'])

    createGraph(elseBody, ifBody)
    createGraph(test, ifBody)
    return [elseBody, test]


def comparison(internalStruct):
    return buildGraph(internalStruct['comparators'])

def whileLoop(internalStruct):
    test = buildGraph(internalStruct['test'])
    body = buildGraph(internalStruct['body'])
    createGraph(body, test)


types = {
    "Constant" : constant, "Name" : name, "Expr" : expression, 
    "Assign" : assignment, "BinOp" : binaryOperation, "Call" : functionCall, 
    "If" : conditionalStatement, "Compare" : comparison, "While" : whileLoop
}