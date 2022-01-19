#To run: python3 bo-analyser.py inputTests/1a-basic-flow.py.json inputTests/6b-patterns.json (for instance)
#Output written in inputTests directory with same name as first argument + .output.json

import sys
import json
import input_parser
import ast_transverser
from Pattern import Pattern
from OutputVulnerability import OutputVulnerability

keys = ["vulnerability", "source", "sink", "unsanitized flows", "sanitized flows" ]
patterns = []
program_slice = []
vulnerabilities = []
output = []

def main():
    if(len(sys.argv) != 3): #check arguments
        print("Invalid number of arguments. Must be two json files.")
        return

    input_parser.parsing(program_slice, patterns)
    for pattern in patterns:
        pattern.toString()

    vulnerabilities = ast_transverser.transverse(program_slice, patterns)
    
    for vulnerability in vulnerabilities:
        identifier = vulnerability.identifier
        source = vulnerability.source
        sink = vulnerability.sink
        unsanitizedFlag = vulnerability.unsanitized_flag
        sanitizedFlows = vulnerability.sanitized_flows

        output.append({keys[0]: identifier, keys[1]: source, keys[2]: sink, keys[3]: unsanitizedFlag, keys[4]: sanitizedFlows})

    targetFileName = sys.argv[1] + ".output.json"
    outputFile = open(targetFileName, 'w')
    jsonStr = json.dump(output,outputFile)
    outputFile.close()


main()