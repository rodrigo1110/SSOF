#1-parsing of both json input Files and creation of AST in this file
#2-transversing AST, definition of rules of thumb, implementation of algorithm based on those rules, and json ouptut creation in other future files 

import sys
import json
import ast
import astor
import astunparse
from Pattern import Pattern #import class Pattern from file Pattern


#patterns = []

def parsing(patterns):
   
    #Parsing of first json file
    program_file = open(sys.argv[1],'r') # parsing of first json file into AST structure. Learn more about this and think of how we want to store the tree for easier transversing later
    program_content = program_file.read()
    program_file.close()
    #print(astor.to_source(program_content).strip())
    program_slice = json.loads(program_content)
    
    
    #Parsing of second json file 
    patterns_file = open(sys.argv[2],'r')  
    patterns_content = patterns_file.read() 
    patterns_file.close() 
    patterns_json = json.loads(patterns_content) 
    print(patterns_json)

    i = 0
    for dict in patterns_json:
        vulnerability = dict["vulnerability"]
        sources = dict["sources"]
        sanitizers = dict["sanitizers"]
        sinks = dict["sinks"]
        implicit = dict["implicit"]

        patterns.append(Pattern(vulnerability,sources,sanitizers,sinks,implicit))
        i += 1
    
    return program_slice
