#!\usr\bin\env python3
from Bio import SeqIO



#read in the file
 
count=0
length_list=[]
line_number=int(0)
for seq_record in SeqIO.parse('ecoli_0.25.contigs.fasta', "fasta"):
		length=len(seq_record.seq)
		length_list.append(length)
		count=count+1

L50count=0
indexN50=int(count/2)
N50=length_list[indexN50]
for length in length_list: 
	if length>int(N50):
		L50count=L50count+1	
			
	#	else:
	#		line_number=line_number+1
	#		if line_number==2:
	#			length_list.append(len(line))



print('shortest contig length: ', min(length_list))
print('longest contig length: ', max(length_list))
print('total contig length: ', sum(length_list))
print('N50:  ', N50)
print('# of contigs: ', count)
print('L50: ', L50count)
#count number of contigs

