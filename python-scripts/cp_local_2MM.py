# 09-27-2018 Bastian Minkenberg
# This script should take the blast6out file and make a dictionary with
# all spacers that have only 2 or 1 mismatches to other spacers as key and
# the actual smallest mismatch should be the entry to the key
# b6 file for UBLAST 5->mm 6->gap 7->start query 8->end query



import sys

BLASTOUT = sys.argv[1]
OUTPUT = sys.argv[2]

output = open(OUTPUT, "w")

spacer_mm = {}
listofkeys = []

with open(BLASTOUT) as f:
    for line in f:
        line = line.strip().split('\t')
        key = line[0]
        mm = (20 - int(line[7])) + (int(line[6]) - 1) + int(line[4]) + int(line[5])
        if mm < 3:
        	entry = []
        	entry.append(line[1])
        	entry.append(str(mm))
        	spacer_mm[key] = entry
        	print >> output, key +'\t' + spacer_mm[key][0] + '\t' + spacer_mm[key][1] #+ '\t' + spacer_mm[key][2] + '\t' + spacer_mm[key][3] + '\t' + spacer_mm[key][4]
        
