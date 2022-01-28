class FlowGraph:

    def __init__(self, token_str):
        self.token_str = str(token_str)
        self.children = []
        self.parents = []


    def printFlowGraph(self):
        print(self.token_str)
        #print("Children(left):", self.children[:])
        #print("Parents(right):", self.parents[:])

    def setToken(self, token_str):
        self.token_str = str(token_str)

    def get_token(self):
        return self.token_str

    def has_children(self):
        return len(self.children) > 0

    def has_parents(self):
        return len(self.parents) > 0

    def __add_parent(self, parent):
        self.parents.append(parent)

    def get_children(self):
        return self.children


    def add_child(self, childGraph):
        if self != childGraph and childGraph not in self.children:
            childGraph.__add_parent(self)
            self.children.append(childGraph)


    def paths(self, k=10):
        """Get all possibles paths in complete graph starting in self graph"""

        if not self.children or k == 0:  # leaf or max depth
            return [[self.token_str]]

        paths = []
        for child in self.children:
            for path in child.paths(k-1):
                paths.append([self.token_str] + path)
                print(path)
                #paths.append([self.token_str] + path)
        
        for el in paths: ##Temporary fix for making all elements of path strings (without some being lists)
            for path in el:
                if(len(path) != 0):
                    if(path[0] == '['):
                        el.remove(path)
                        el.append(eval(path)[0])
        return paths


    def __str__(self):
        child_names = [str(child.token_str) for child in self.children]
        return self.get_token() + str(child_names)