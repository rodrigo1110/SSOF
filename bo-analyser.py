#To run: python3 bo-analyser.py inputTests/1a-basic-flow.py.json inputTests/6b-patterns.json (for instance)
#Output written in inputTests directory with same name as first argument + .output.json

import sys
import json
import input_parser
import vulnerability_identifier
import ast_transverser
from Pattern import Pattern
from OutputVulnerability import OutputVulnerability
from FlowGraph import FlowGraph


keys = ["vulnerability", "source", "sink", "unsanitized flows", "sanitized flows" ]
patterns = []
output = []

def main():
    if(len(sys.argv) != 3): #check arguments
        print("Invalid number of arguments. Must be two json files.")
        return


    program_slice = input_parser.parsing(patterns) #program slice is a dictionary with one key ("body").   
                                                    #program_slice["body"] is a list of dictionaries with keys like ast_type, value ...
    
    
    flow_graph = ast_transverser.transverse(program_slice)
    flow_graph.printFlowGraph()

    vulnerabilities = vulnerability_identifier.identifyVulnerabilities(flow_graph, patterns)
    
    
    for vulnerability in vulnerabilities: #format vulnerabilities found into output jason file
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