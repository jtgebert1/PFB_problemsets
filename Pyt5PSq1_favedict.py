#!/usr/bin/env python
import sys

favdict={'color':'orange', 'book':'The Pearl', 'food':'Panang curry'}


favdict['organism']='drosophila'
favthing=favdict['organism']
##print(favthing)

##for loop to print all items in dictionary 
for item in favdict:
	print(item)

##take item from command line and print 
item=input("which of the above?:")
print(favdict[item])


