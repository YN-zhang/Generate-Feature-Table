import pandas as pd
import sys
import numpy as np

df = pd.read_csv('motif_tf.tsv',index_col=0,sep='\t')

dict1=df.to_dict()
dict2=dict1['Transcription factor']

df2=pd.read_csv(sys.argv[1],index_col=0)
res=pd.DataFrame()
res['name']=df2.index


for i in df2.columns:
	res[dict2[i]]=np.zeros(len(df2.index)).astype(int)

for i in df2.columns:
	res[dict2[i]]=np.array(res[dict2[i]])|np.array(df2[i])
res=res.set_index('name')
temp_col=sorted(res.columns)
print(temp_col)
#print(res)
#print(res.describe().T)
res=pd.DataFrame(res,columns=temp_col)
print(res.columns)
output=sys.argv[1].split('.')
res.to_csv(output[0]+'.tf.csv')
