import sys
import json
import input_parser
import vulnerability_identifier
import ast_transverser
from Pattern import Pattern
from OutputVulnerability import OutputVulnerability
from FlowGraph import FlowGraph

keys = ["vulnerability", "source", "sink", "unsanitized flows", "sanitized flows"]
patterns = []
output = []

def main():
    if(len(sys.argv) != 3): 
        print("Invalid number of arguments. Must be two json files.")
        return

    program_slice = input_parser.parsing(patterns)    
    flow_graph = ast_transverser.transverse(program_slice)
    vulnerabilities = vulnerability_identifier.identifyVulnerabilities(flow_graph, patterns)
       
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