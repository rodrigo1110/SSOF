class Pattern:
    
    def __init__(self,vulnerability,sources,sanitizers,sinks,implicit):
        self.vulnerability = vulnerability
        self.sources = sources
        self.sanitizers = sanitizers
        self.sinks = sinks
        if(implicit=='yes'):
            self.implicit = True
        else:
            self.implicit = False
    
    def toString(self):
        print("-----Pattern-----")
        print("Vulnerability:", self.vulnerability)
        print("Sources:", self.sources[:])
        print("Sanitizers:", self.sanitizers[:])
        print("Sinks:", self.sinks[:])
        print("Implicit:", self.implicit)
