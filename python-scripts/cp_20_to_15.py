# 09-27-18 This script should produce a new fasta file
# from the incoming 20N spacer file to 15N spacer
# Only the sequences will change, not the identifier
# This is done so that they can be matched back to the
# original file after vsearch --search_exact

import sys

FASTA = sys.argv[1]
OUTPUT = sys.argv[2]

output = open(OUTPUT, "w")

with open(FASTA) as f:

    for line in f:
        if '>' == line[0]:
            print >> output, line.rstrip('\n')
        else:
            line = line[5:]
            print >> output, line.rstrip('\n')
  
        
