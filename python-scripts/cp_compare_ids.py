# 09-27-2018 Bastian Minkenberg
# Takes the ID files and compares them to the original
# spacer list to subtract any candidates with off-targets

import sys

OFFTARGETIDS = sys.argv[1]
SPACERIDS = sys.argv[2]
OUTPUT = sys.argv[3]

output = open(OUTPUT, "w")

with open (OFFTARGETIDS) as f:
    listoff = list(f)
with open (SPACERIDS) as f:
    spacerlist = list(f)
newlist = list(set(spacerlist) - set(listoff))

for line in newlist:
    print >> output, line.rstrip('\n')

        
