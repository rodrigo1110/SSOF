class Tainted:
    def __init__(self,origin,taintedList,sanitizedList):
        self.origin = origin
        self.taintedList = taintedList
        self.sanitizedList = sanitizedList
    
    def toString(self):
        print("-----Tainted-----")
        print("Origin:", self.origin)
        print("TaintedList:", self.taintedList[:])
        print("SanitizedList:", self.sanitizedList[:])
       
    