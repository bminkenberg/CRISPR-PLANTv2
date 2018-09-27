# 09-27-2018 Bastian Minkenberg
# Prepares list for A and B classification. Transform the list to only keep
# the 10 nt seed reion

import sys

FASTA = sys.argv[1]
OUTPUT = sys.argv[2]

output = open(OUTPUT, "w")

with open(FASTA) as f:

    for line in f:
        if '>' == line[0]:
            print >> output, line.rstrip('\n')
        else:
            line = line[10:]
            print >> output, line.rstrip('\n')
  
        
