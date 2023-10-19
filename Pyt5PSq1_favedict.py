#!/usr/bin/env python
import sys

favdict={'color':'orange', 'book':'The Pearl', 'food':'Panang curry','organism':'drosophila'}

favthing=input('Who is your favorite musician?:')

favdict['musician']=favthing

print(f"Your favorite musician is {favdict['musician']}")
print("updated list of favorites:")

for fav in favdict:
	print(fav,":", favdict[fav])





##change value of favorite organism
#moved up to precede loop

