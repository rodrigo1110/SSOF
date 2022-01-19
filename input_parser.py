#1-parsing of both json input Files and creation of AST in this file
#2-transversing AST, definition of rules of thumb, implementation of algorithm based on those rules, and json ouptut creation in other future files 

#To run: python3 input_parser.py inputTests/0-helloWorld inputTests/5b-patterns.json 

import sys
import json
from Pattern import Pattern #import class Pattern from file Pattern


patterns = []

def main():
    if(len(sys.argv) != 3): #check arguments
        print("Invalid number of arguments. Must be two json files.")
        return

    program_file = open(sys.argv[1],'r') #future parsing of first json file into AST structure 
    lines_program = program_file.readlines()
    i = 0
    for line in lines_program:
        i += 1
        print(line)
    program_file.close() #end parsing of first json file
    
    
    patterns_file = open(sys.argv[2],'r') #correct parsing of second json file 
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
        patterns[i].toString()
        i += 1
    #end parsing of second json file

    
if(__name__ == "__main__"):
    main()
