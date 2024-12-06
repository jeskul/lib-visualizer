#!/usr/bin/env python3
import re
import os
import sys
import getopt
import shutil

inputfile = ''
outputfile = ''
try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
    print (sys.argv[0] + " -i <inputfile> -o <outputfile>")
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print (sys.argv[0] + " -i <inputfile> -o <outputfile>")
        print ("Where <inputfile> is a file containing the output of 'nm -C library.a'")
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg

if inputfile == "":
    print ("Missing input file")
    print (sys.argv[0] + " -i <inputfile> -o <outputfile>")
    sys.exit(2)


#
# Step 1. Read and parse input
#
needed = {}
provided = {}
providers = {}
currentObjFile=""
with open(inputfile) as file_object:
    for line in file_object:
        line = line.rstrip()
        matchObjectFile = re.match(r'(.+)\.o', line)
        matchProvided   = re.match(r'.{16} T (.+?)\(', line)
        matchNeeded     = re.match(r'.{16} U (.+?)\(', line)
        matchEmptyLine  = re.match(r'^$', line)
        if matchObjectFile:
            currentObjectFile = matchObjectFile.group(1)
            needed[currentObjectFile] = []
            provided[currentObjectFile] = []
        elif matchProvided:
            provided[currentObjectFile].append(matchProvided.group(1))
            providers[matchProvided.group(1)] = currentObjectFile 
        elif matchNeeded:
            needed[currentObjectFile].append(matchNeeded.group(1))
        elif matchEmptyLine:
            currentObjFile = ""       

#
# Step 2. Creating links between object files
#

# Use a set to avoid duplicates i.e. where one file has many dependencies to another file
links = set()

for key, value in needed.items():
    for need in value:
        dest = providers.get(need)
        if dest != None:
            links.add("    \"" + key + "\" -> \"" + dest + "\";")
        else:
            links.add("    \"" + key + "\" -> \"" + "external" + "\";")

#print(links)

#
# Step 3. Generating the the output
#

if outputfile != "":
    sys.stdout = open(outputfile, "w")

print("digraph library {")
print("    graph [rankdir = \"LR\"];")
print("    node [shape=box];")

for value in links:
    print(value)

print("}")

sys.stdout = sys.__stdout__

if outputfile != "" and shutil.which("dot") == None:
    print("Now run Graphviz dot:")
    print("dot -Tpng " + outputfile + " -o <mygraphfile>.png")

if outputfile != "" and shutil.which("dot") != None:
    os.system("dot -Tsvg " + outputfile + " -o " + outputfile + ".svg")
    print("Created " + outputfile + ".svg")
    os.system("rm " + outputfile)
