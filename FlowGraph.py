class FlowGraph:

    def __init__(self, name):
        self.name = str(name)
        self.children = []
        self.parents = []

    def printFlowGraph(self):
        print(self.name)


    def hasChildren(self):
        return len(self.children) > 0

    def hasParents(self):
        return len(self.parents) > 0
    
    def addChild(self, childGraph):
        if(self != childGraph and childGraph not in self.children): 
            childGraph.parents.append(self)
            self.children.append(childGraph)                                                                                  

    
    def getPaths(self):
        if(not self.children):  
            return [[self.name]]

        paths = []
        for child in self.children:
            for path in child.getPaths():
                paths.append([self.name] + path)
        
        for el in paths: 
            for path in el:
                if(len(path) != 0):
                    if(path[0] == '['):
                        el.remove(path)
                        el.append(eval(path)[0])
        return paths
