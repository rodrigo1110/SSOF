class Tainted:
    def __init__(self,origin,taintedList):
        self.origin = origin
        self.taintedList = taintedList
    
    def toString(self):
        print("-----Tainted-----")
        print("Origin:", self.origin)
        print("TaintedList:", self.taintedList[:])
       
    