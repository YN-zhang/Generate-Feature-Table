import sys
import pandas as pd
motifs=open(sys.argv[1],'r')


dict1={}
motifs_set=[]
for line in motifs:
	line =line.strip('\n')
	line=line.split()
	if line[7] not in motifs_set:
		motifs_set.append(line[7])
		dict1[line[7]]=0

motifs.close()
motif_freq=open(sys.argv[1],'r')

windows=open(sys.argv[2],'r')
dict2={}
for line in windows:
	line = line.strip('\n')
	temp = line.split()
	dict2[temp[3]]={}
#	motifs=open('motif.list','r')
	for j in motifs_set:
#		j=j.strip('\n')
		dict2[temp[3]][j]=0
	motifs.close()
#	dict2[temp[3]]=dict1
#		dict2.update({line:{j:0}})
windows.close()

for line in motif_freq:
	line=line.strip('\n')
	temp=line.split()
	dict2[temp[3]][temp[7]]=1

res='name'
for i in dict1:
	res=res+','+i
print(res)
for i in dict2:
	line = i
	for j in dict2[i]:
		line = line+','+str(dict2[i][j])
	print(line)
