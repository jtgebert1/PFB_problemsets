#!/usr/bin/env python3

import sys
from Bio import SeqIO 
from Bio.SeqUtils import GC
from statistics import mean

input_FASTA=sys.argv[1]

#Parse FASTA file using SeqIO 
count=0
seqlist=[]
shortest=100000000
longest=0
GChigh=0
GClow=100
totalnuc=0
GClist=[]
for seq_record in SeqIO.parse(input_FASTA, "fasta"):
	count=count+1
	seq=str(seq_record.seq)
	length=len(seq)
	if length<shortest:
		shortest=length
	if length>longest:
		longest=length
	seqlist.append(seq)
	#find GC content 
	GClist.append(GC(seq))
	if GC(seq)<GClow:
		GClow=int(GC(seq))
	if GC(seq)>GChigh:
		GChigh=int(GC(seq))
	totalnuc=totalnuc+length	

print(f'Sequence count: {count} \nTotal nucleotides: {totalnuc}, \nAverage length: {int(totalnuc)/count} \nlongest: {longest} \n shortest: {shortest} \n average GC: {mean(GClist)} \n highest GC: {GChigh} \n lowest GC: {GClow}')
