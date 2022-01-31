import sys
import json
from Pattern import Pattern 

def parsing(patterns):
    program_file = open(sys.argv[1],'r') 
    program_content = program_file.read()
    program_file.close()
    program_slice = json.loads(program_content)
    
    patterns_file = open(sys.argv[2],'r')  
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
    
    return program_slice
