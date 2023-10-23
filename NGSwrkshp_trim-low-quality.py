#!/usr/bin/python3

import sys

file=sys.argv[1]
lowerthresh=int(sys.argv[2])
#sys.argv[3] defined as file_out below

#specify lower threshold on command line, start with 20 
#undo ASCII offset phred score 

#read in the file 


#phred=ord(ascii_char)-33
#use count to differentiate sequences and quality reads. Seq will be divisible by 3
with open(sys.argv[1], "r") as file, open(sys.argv[3], "w") as file_out:
	for line in file:
		line=line.rstrip()
		if line[0]=='@':
			header=line
			count=int(1)
		#find 2nd line -- this is the sequences
		if count==2:
			seq=line[::-1]
		#find 4th line -- this is the quality score
		if count==4:
			#invert seq to iterate from 3' end 
			qual=line[::-1]
			phredstring=[]
			for char in qual:
				phred=ord(char)-33
				phredstring.append(phred)
				instance=0
				if phred>=lowerthresh:
					instance=qual.find(char)
			seq_trimmed=seq[instance:]
			seq_trimmed=seq_trimmed[::-1]
			phred_trimmed=phredstring[instance:]
			phred_trimmed=phred_trimmed[::-1]
			ascii_phred=''
			for phred in phred_trimmed:
				ascii_phred=ascii_phred + chr(int(phred) + 33)
			#write trimmed to a new file 
			file_out.write(f"{header}\n{seq_trimmed}\n+\n{ascii_phred}\n")
		
		count=count+1
print(f"{str(sys.argv[1])} trimmed from 3' end to first phred score greater than {sys.argv[2]}, written to {str(sys.argv[3])}")
