#!/usr/bin/env python
#ask for DNA sequence
dna=input("DNA seq:")
 
#convert all characters to uppercase
dna_up=dna.upper()

#find total number of nucleotides
total=len(dna)

#find number of A and T
A_count=dna_up.count('A')
T_count=dna_up.count('T')

AT_count=int(A_count) + int(T_count)

percentAT=int(AT_count) /int(total)
percentGC=1-float(percentAT)

#return new sequence
print("% AT=", percentAT, "\n% GC=", percentGC)
