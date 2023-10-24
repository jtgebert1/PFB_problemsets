#!\usr\bin\env python3
from Bio import SeqIO
 
count=0
A=int(0)
G=int(0)
C=int(0)
T=int(0)
a=int(0)
g=int(0)
c=int(0)
t=int(0)
N=int(0)
length_list=[]
line_number=int(0)
for seq_record in SeqIO.parse('D_melanogaster_genomic.fna', "fasta"):
		seq=str(seq_record.seq)
		length=len(seq_record.seq)
		length_list.append(length)
		count=count+1
		A=A+seq.count('A')
		G=G+seq.count('G')
		C=C+seq.count('C')
		T=T+seq.count('T')
		a=a+seq.count('a')
		g=g+seq.count('g')
		c=c+seq.count('c')
		t=t+seq.count('t')
		N=N+seq.count('N')
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
print('Unresolved: ', N)
print(f"A: {A}, C: {C}, G: {G}, T: {T}, a: {a}, c: {c}, g: {g}, t: {t}")
