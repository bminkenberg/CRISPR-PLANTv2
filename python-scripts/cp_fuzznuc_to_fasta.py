# 09-27-2018 Scans the fuzznuc output file and assambles
# a FASTA file with a unique identifier for each protospacer.
# 

import sys
import re

SEQTABLE = sys.argv[1]
OUTPUT = sys.argv[2]

output = open(OUTPUT, "w")

with open(SEQTABLE) as f:

    for line in f:
        line = line.strip().split(' ')
        line = filter(lambda a: a != '', line)
        #print >> output, line
        if 'Sequence:' in line:
            chrnumber = re.findall(r'\d+', line[2])
            fasta_one = '>' + 'Chr' + chrnumber[0] + ':'
        # only works if zero mismatches
        if '.' in line:
            #written to remove the NGG

            if '+' == line[2]:
                # set -3 and remove last three characters from line [5]
                line[1] = str(int(line[1])-3)
                line[5] = line[5][:-3]
                fasta = fasta_one + line[0] + '-' + line[1] + '\n' + line[5]

            else:
                # set +3, add :rc, and remove first three char from line[5]
                line[5] = line[5][:-3]
                line[0] = str(int(line[0])+3)
                line[1] = line[1] + ':rc'
                fasta = fasta_one + line[0] + '-' + line[1] + '\n' + line[5]
                
            print >> output, fasta
        
        
