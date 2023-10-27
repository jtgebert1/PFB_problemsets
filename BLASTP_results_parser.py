#!\usr\bin\env python3

import os 
import re

results_dict={}
alen_dict={}
percentid_dict={}
evalue_dict={}
matrix_list=[]

#read in the files
for file in os.listdir('/Users/pfb21/problemsets/BLAST'):
	if re.search(r'.txt', file):
		matrixname=file[-8:-4]
		matrix_list.append(matrixname)
		with open(f'/Users/pfb21/problemsets/BLAST/{file}') as result:
			for line in result:
				#find lines that begin with "random" -- only need first, thus break after one loop
				if line[0]=="r":
					line=line.split('\t')
					alen_dict[matrixname]=line[3]
					percentid_dict[matrixname]=line[2]
					evalue_dict[matrixname]=line[-2]
					break

print(f'Matrix\tlen\t%ID\tE')	
for matrix in sorted(matrix_list):
	print(f'{matrix}\t{alen_dict[matrix]}\t{percentid_dict[matrix]}\t{evalue_dict[matrix]}')
