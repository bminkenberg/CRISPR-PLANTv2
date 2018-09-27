# 09-27-2018 Bastian Minkenberg
# Takes the cleaned ID list and extracts the candidates without
# off-targets from the original list with all.

import sys
import re


CLEANEDLIST = sys.argv[1]
SPACERLIST = sys.argv[2]
OUTPUT = sys.argv[3]
     


output = open(OUTPUT, "w")

spacer_dic = {}
with open(SPACERLIST) as g:
    for line in g:
        key = line.rstrip('\n')
      #  print key
        entry = g.next()
      #  print entry
        entry = entry.rstrip('\n')
        spacer_dic[key] = entry

with open(CLEANEDLIST) as f:
    for line in f:
        app = ">" + line.rstrip('\n')
        print >> output, app + '\n' + spacer_dic[app]
        
