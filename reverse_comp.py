#!/usr/bin/env python
  
#ask for DNA sequence
dna=input("DNA seq:")

  
#convert all characters to uppercase
dna_up=dna.upper()

#reverse
reverse=dna_up[::-1]

#complement
dna1=dna_up.replace('A','t').replace('T','a').replace('G','c').replace('C','g')

dna_up_final=dna1.upper()

print(dna_up_final)


