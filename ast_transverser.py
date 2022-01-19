#Future code for transversing the parsed AST and identify vulnerabilities based on rules of thumb and parsed patterns received as input
import ast
import astunparse
from Pattern import Pattern
from OutputVulnerability import OutputVulnerability


vulnerabilities = []

def transverse(program_slice, patterns): 
    return [OutputVulnerability("A","sourceA","sinkA","yes",[]),OutputVulnerability("B","sourceb","sinkB","no",[["one"]])] #just for testing


#add more auxiliar functions in this file later called by transverse or by the main function 