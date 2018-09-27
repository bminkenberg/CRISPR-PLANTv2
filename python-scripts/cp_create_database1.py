# 09-27-2018 Bastian Minkenberg
# This script will take a end-result spacerlist and create the database without location and PAM
#
# seqID	minMM_GG	minMM_AG	seq	Chr	cut_start	cut_end	strand	location	PAM
# Chr1:10000524-10000544	NA	NA	TCTGAATCTTTTAAAGCATT	Chr1	10000540	10000543	+	igr	AGGCTCTCTC
# scaffold_10:1000086-1000105:rc	4+	4+	TAGCAACGACACACTCTACA	scaffold_10	1000102	1000105	-	
# 
# 1) Decided to populate location and PAM later
#
# 2) All the other information can be easily extracted from the spacer files
#
# 3) for minMM_GG and minMM_AG chose >3 >2 1 etc instead of exact number.
#
# A0	4+	4+	
# B0	4+	4+
# A0.1	4+	3+
# B0.1	4+	3+
# A1	4+	1+
# B1	4+	1+
# A2	4+	0
# B2	4+	0
import sys
import re

SPACERLIST = sys.argv[1]
CLASS = sys.argv[2]
OUTPUT = sys.argv[3]

output = open(OUTPUT, "w")

if "0" in CLASS:
    minMM = ["4+", "4+"]
if "1" in CLASS:
    minMM = ["4+", "1+"]
if "0.1" in CLASS:
    minMM = ["4+", "3+"]
if "2" in CLASS:
    minMM = ["4+", "0"]

print >> output, 'seqID\tminMM_GG\tminMM_AG\tseq\tChrt\tcut_start\tcut_end\tstrand\tlocation\tPAM\n'

with open(SPACERLIST) as f:
    for line in f:
        if ">" in line:
             seqID = line[1:]
             seqID = seqID.rstrip()
             seq = f.next()
             seq = seq.rstrip()
             split1 = line.split(':')
             Chr = split1[0][1:]              
             split2 = split1[1].split('-')
             if "rc" in line:
                cut_start = str(int(split2[0])-3)
                cut_end = split2[0]
                strand = "-"
             else:
                cut_start = str(int(split2[1])-3)
                cut_end = split2[1].rstrip()
                strand = "+"
                              
        print >> output, seqID + '\t' + minMM[0] + '\t' + minMM[1] + '\t' + seq + '\t' + Chr + '\t' + cut_start + '\t' + cut_end + '\t' + strand
