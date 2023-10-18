#!/usr/bin/env python3

#ask for DNA sequence
dna=input("DNA seq:")

#convert all characters to uppercase
dna_up=dna.upper()

#replace Ts with U's
transcribed=dna_up.replace('T','U')

#return new sequence
print(transcribed)

