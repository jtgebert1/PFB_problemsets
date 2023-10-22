#!/usr/bin/env python3

import Bio

#FASTA parser to get sequence name, description, sequence 

from Bio import SeqIO

seq_count=0
for seq_record in SeqIO.parse("Python_08_short.fasta", "fasta"):
	print('ID', seq_record.id)
	print('Sequence', seq_record.seq)
	print('Description', seq_record.description) 	
	seq_count=seq_count+1
	
	total_nuc=0
	for seq in seq_record.seq:
		length=len(seq_record.seq)
		total_nuc=total_nuc + int(length)
	print(length)

print(total_nuc)
