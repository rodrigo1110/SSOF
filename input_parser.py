#1-parsing of both json input Files and creation of AST in this file
#2-transversing AST, definition of rules of thumb, implementation of algorithm based on those rules, and json ouptut creation in other future files 

import sys
import json
import ast
import astunparse
from Pattern import Pattern #import class Pattern from file Pattern


#patterns = []

def parsing(program_slice, patterns):
   
    program_file = open(sys.argv[1],'r') #future parsing of first json file into AST structure. Learn more about this and think of how we want to store the tree for easier transversing later
    program_content = program_file.read()
    program_file.close()
    program_json = json.loads(program_content)
    #print(astunparse.unparse(program_json))

    i = 0
    #for line in lines_program:
       # i += 1
        #print("Line", i)
    #end parsing of first json file
    
    
    patterns_file = open(sys.argv[2],'r') #implemented parsing of second json file 
    patterns_content = patterns_file.read() 
    patterns_file.close() 
    patterns_json = json.loads(patterns_content) 

    i = 0
    for dict in patterns_json:
        vulnerability = dict["vulnerability"]
        sources = dict["sources"]
        sanitizers = dict["sanitizers"]
        sinks = dict["sinks"]
        implicit = dict["implicit"]

        patterns.append(Pattern(vulnerability,sources,sanitizers,sinks,implicit))
        i += 1
    #end parsing of second json file
