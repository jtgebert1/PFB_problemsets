#!/usr/bin/env python

#ask for DNA sequence
dna=input("DNA seq:")

#convert all characters to uppercase
dna_up=dna.upper()

# make substring
substring=dna_up[99:200]

# count G's
Gcount=substring.count('G')

print("\n", substring,"\nsubstring length:",  len(substring), "\nsubstring G content:", Gcount )


