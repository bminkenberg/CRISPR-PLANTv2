# 09-27-2018 Bastian Minkenber
# Spacers being only 10 bp away
# from each others should not be considered as off-targets. Therefore,
# this script removes all the hits with other spacers that are only 10 bp away
# from each other so that they stay conserved.

import sys
import re

OFFTARGETLIST1 = sys.argv[1]
OUTPUT = sys.argv[2]

output = open(OUTPUT, "w")

with open(OFFTARGETLIST1) as f:
    for line in f:
        linelist = line.strip().split('\t')

        # extract numbers from the two matches sequences
        line0numbers = re.findall('\d+', linelist[0])
        line1numbers = re.findall('\d+', linelist[1])

       # extract first number of the list and conver to integer
        line0numbers = int(line0numbers[1])
        line1numbers = int(line1numbers[1])
    # print the line only if both number are MORE or LESS than 11
    # bp away from each other. I chose < > 11 instead of <= >= 10
        if line1numbers > line0numbers + 11 or line1numbers < line0numbers - 11:
            print >> output, line.rstrip('\n')

      
