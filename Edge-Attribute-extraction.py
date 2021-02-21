import pandas as pd 
import numpy as np
import random
from collections import Counter


df=pd.read_excel('df.xlsx', header=None)

#Lien : Répondant p cité 

dfn=df[[9,12,13,14,15,16,17,18,19,20,21]].applymap(lambda x: np.nan if x =="Prénom Nom" else x)

node={}

for row in dfn.iterrows():
    y = []
    for x in row[1]:
        y.append(x)
    node[y[0]] = y[1:] 
    
new_data = list(node.items())
    
d=pd.DataFrame(new_data)
d=d.explode(1)
d=d.dropna()

#Lien Ami univ (F):

df['str48']=df[48].astype(str)
nomnodf=list(df[9])
nbnodefe=list(df[47].dropna())

cf = sum([[s] * n for s, n in zip(nomnodf, nbnodefe)], [])


dfn=dfn.drop([9],axis=1)

inde=[]
ln=[]

for item in df['str48'].iteritems():
    a= list(item)
    a.pop(0)
    a=[int(x) for x in str(a[0])] 
    for digit in a :           
        e=int(digit)
        inde.append(e)
        
b=0
df['count'] = df['str48'].str.len()
count=list(df['count'])
lk=len(dfn)
a1=0
a2=0

possible=[]

while b<lk :
    aaa=list(dfn.iloc [b])
    bbb=count[b]
    a1=a1+bbb
    ccc=[]
    ccc.append(inde[a2:a1])
    ccc=list(ccc)
    for num in ccc :
        for n in num :
            possible.append(aaa[n-1])
    a2=a1
    b=b+1


number_of_unique_values=list(Counter(cf).values())

c=0
b1=0
b2=0
det=0
aleatoire=[]
lki=len(number_of_unique_values)

while c<lki :
    b1=b2
    b2=count[c]+b2
    aaa=possible[b1:b2] 
    ccc=number_of_unique_values[det]
    ran=random.choices(aaa, k=ccc)
    aleatoire.append(ran)
    c=c+1
    det=det+1


flat_aleatoire = [item for sublist in aleatoire for item in sublist]
    
a=" AF"

amif=[item+a for item in cf]

dvb=0
c1=2

while dvb<len(amif)-1:
    if amif[dvb] == amif[dvb+1] or amif[dvb][:-1] == amif[dvb+1]  : 
        amif[dvb+1]=amif[dvb]+str(c1)
        c1=c1+1
    else :
        pass
    dvb=dvb+1



lienamif = list(zip(amif, flat_aleatoire))    
e=pd.DataFrame(lienamif) 

                     

#Lien Ami univ (H):
    

    
df['str53']=df[53].astype(str)
nbnodefe2=list(df[52].dropna())
new_list = []
for item in nbnodefe2:
    new_list.append(int(item))
    
nbnodefe2=new_list

cff = sum([[s] * n for s, n in zip(nomnodf, nbnodefe2)], [])


indee=[]
lnn=[]

for item in df['str53'].iteritems():
    a= list(item)
    a.pop(0)
    a=[int(x) for x in str(a[0])] 
    for digit in a :           
        ef=int(digit)
        indee.append(ef)
        
bb=0
df['count2'] = df['str53'].str.len()
count2=list(df['count2'])
aa1=0
aa2=0
lkk=len(dfn)


possi=[]

while bb<lkk :
    aaa=list(dfn.iloc [bb])
    bbb=count2[bb]
    aa1=aa1+bbb
    ccc=[]
    ccc.append(indee[aa2:aa1])
    ccc=list(ccc)
    for num in ccc :
        for n in num :
            possi.append(aaa[n-1])
    aa2=aa1
    bb=bb+1

number_of_unique_value=list(Counter(cff).values())

cc=0 # index count 2
bb1=0 #positionnels count 2 = slicer
bb2=0   #positionnels count 2
dd=0
lkki=len(number_of_unique_value)
aleatoiree=[]



while cc<lkki :
    bb1=bb2
    bb2=count2[cc]+bb2
    aaa=possi[bb1:bb2] 
    ccc=number_of_unique_value[dd]
    ran=random.choices(aaa, k=ccc)
    aleatoiree.append(ran)
    cc=cc+1
    dd=dd+1
     

flat_aleatoiree = [item for sublist in aleatoiree for item in sublist]

b=" AH" 

amih=[item+b for item in cff]

dvb=0
c1=2


while dvb<len(amih)-1:
    if amih[dvb] == amih[dvb+1] or amih[dvb][:-1] == amih[dvb+1]  :
        amih[dvb+1]=amih[dvb]+str(c1)
        c1=c1+1
        dvb=dvb+1
    else :
        dvb=dvb+1

lienamih = list(zip(amih, flat_aleatoiree))    
f=pd.DataFrame(lienamih) 

dfhf=df[[9,64]]
homme='Homme'
femme='Femme'

dih = {k:homme for k in amih}
dif = {k:femme for k in amif}

dfhf2=df[[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]].transpose()

connsexe={}

for item in dfhf2.iteritems():
    item=list(item)
    item=item[1]
    el=12
    al=22
    while al<32 :
        connsexe.update({item[el]:item[al]})
        el=el+1
        al=al+1

desired_key = "Prénom Nom"

for key in connsexe.keys():
  if key == desired_key:
    del connsexe[key]
    break


g=pd.DataFrame.from_dict(connsexe,orient='index')
g=g[0].replace({"Un homme":"Homme", "Une femme":"Femme"})
h=pd.DataFrame.from_dict(dih,orient='index')
i=pd.DataFrame.from_dict(dif,orient='index')

dfhf=dfhf.set_index(9,inplace=True)

dictionnairedessexes=pd.concat([g,h,i,dfhf])
dictionnairedesliens=pd.concat([d,e,f])

    
    