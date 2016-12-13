#!/usr/bin/python3

#### THIS SCRIPT IS FOR RANDOMLY SAMPLING SNPS FROM A VCF FILE; ONE SNP EACH LOCUS OR CHROMOSOME ####
#### USAGE: python3 random_snps.vcf.py [input file] [output file] ####
#### Andrew D. Sweet and Julie M. Allen ####

import csv
import random
import sys
from collections import defaultdict
from pprint import pprint

locusdict=defaultdict(list)
randict=defaultdict(list)
with open(sys.argv[1],"r") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		locus = (row[0])
		if locus in locusdict:
			locusdict[locus] += 1
		else:
			locusdict[locus] = 1
for key, value in locusdict.items():
	number = random.randrange(0,value,1)
	randict[key] = number
with open(sys.argv[2],"w") as outfile:
	writer = csv.writer(outfile)
	with open(sys.argv[1],"r") as csvfile:
		reader = csv.reader(csvfile)
		l1 = "old"
		line = 1
		for row in reader:
			locus = (row[0])
			if locus == l1:
				line += 1
				if line == randict[locus]:
					writer.writerow(row)
			else:
				l1 = locus
				line = 1 
