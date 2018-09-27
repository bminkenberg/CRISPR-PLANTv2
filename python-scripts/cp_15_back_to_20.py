# 09-27-18 This script will take the fasta file that contains all the notmatched
# 15nt spacers and will use the > information to extract them from the 20nt fasta file.
# Afterwards that file will be used for alignments.
# The script will create a dictionary of inputtwo and
# use the list info from imputone as key to access the sequences.
# Bastian Minkenberg

import sys


INPUTONE = sys.argv[1]
INPUTTWO = sys.argv[2]
OUTPUT = sys.argv[3]

output = open(OUTPUT, "w")

index = []
with open(INPUTONE) as f:

    for line in f:
        if '>' == line[0]:
            index.append(line.rstrip('\n'))
    
spacer_dic = {}
with open(INPUTTWO) as g:

    for line in g:
        key = line.rstrip('\n')
        entry = g.next()
        entry = entry.rstrip('\n')
        spacer_dic[key] = entry
        

i = 0
for spacer_key in index:
    print >> output, index[i].rstrip('\n')
    i = i + 1
    print >> output, spacer_dic[spacer_key].rstrip('\n')
