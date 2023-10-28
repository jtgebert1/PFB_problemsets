#!/usr/bin/env python3

from Bio import Align
from Bio.Align import MultipleSeqAlignment
from Bio import SeqIO
import sys

file=sys.argv[1]

#create a dictionary of dictionaries. First key will be nucleotide position.Next will be nucleotide, with the count across all seq.

SA11_NSP4='MEKLTDLNYTLSVITLMNNTLHTILEDPGMAYFPYIASVLTVLFALHKASIPTMKIALKTSKCSYKVVKYCIVTIFNTLLKLAGYKEQITTKDEIEKQMDRVVKEMRRQLEMIDKLTTREIEQVELLKRIYDKLTVQTTGEIDMTKEINQKNVRTLEEWESGKNPYEPREVTAAM'

count_dict={'0':{'M':int(0)}}

for record in SeqIO.parse(file, "fasta"):
	if len(record.seq)==175: 
		for nuc in str(record):
			if index[nuc] not in count_dict:
				count_dict[index[nuc]]={nuc:int(1)}
			else:
				count_dict[index[nuc]]={nuc:countdict[index[nuc]]

