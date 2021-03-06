import pandas as pd 
import numpy as np
import random
from collections import Counter

print("""\
      
                              SocioLens 
                                ______              
                             .-'      `-.           
                           .'            `.         
                          /                \        
                         ;                 ;`       
                         |         S       |;       
                         ;                 ;|
                         '\               / ;       
                          \`.           .' /        
                           `.`-._____.-' .'         
                             / /`_____.-'           
                            / / /                   
                           / / /
                          / / /
                         / / /
                        / / /
                       / / /
                      / / /
                     / / /
                    / / /
                    \/_/

                    """)

intc = input("Nom du fichier.xlsx : ")

df=pd.read_excel(intc, header=None)
digitsupp=['1','2','3','4','5','6','7','8','9']

#Dictionnaire des liens : Répondant --> Personnes cites 

#Colonnes : Répondant + Personnes cites

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

#Liens répondants --> Amis + Amis --> Personnes cites (Femmes)

df[52]=df[52].fillna(0)  #Nbre d'amies  

df['str48']=df[53].astype(str) #Indexe des personnes cités
nomnodf=list(df[9]) # Repondant
nbnodefe=list(df[47].fillna(0)) #NB Amies 
nbnodefe=([int(nbnodefe) for nbnodefe in nbnodefe])

cf = sum([[s] * n for s, n in zip(nomnodf, nbnodefe)], [])


dfn=dfn.drop([9],axis=1) #Repondant

inde=[]
ln=[]

for item in df['str48'].iteritems():
    a= list(item)
    a.pop(0)
    a=[int(x) for x in str(a[0])] 
    for digit in a :           
        e=int(digit)
        inde.append(e)

for ele in inde: 
    if ele == 0: 
        inde.remove(ele) 

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

a=0
c=0
b1=0
b2=0
det=0
aleatoire=[]
lki=len(count)

while c<lki :
    if df.iloc[c][47] == 0 : #Nombre d'amies 
        a=count[c]
        b1=b1+a
        c=c+1
        b2=b1
    else: 
        a=count[c]
        b1=b1+a
        aaa=possible[b2:b1] 
        ccc=number_of_unique_values[det]
        ran=random.choices(aaa, k=ccc)
        aleatoire.append(ran)
        det=det+1
        c=c+1
        b2=b1


flat_aleatoire = [item for sublist in aleatoire for item in sublist]
    
a=" AF"

amif=[item+a for item in cf]

dvb=0

while dvb<len(amif)-1:
    if amif[dvb] == amif[dvb+1] or amif[dvb].split(' ')[1] == amif[dvb+1].split(' ')[1]   : 
        c1=2
        amif[dvb+1]=amif[dvb]+str(c1)
        c1=c1+1
    else :
        pass
    dvb=dvb+1
    
lienamif = list(zip(amif, flat_aleatoire))    
e=pd.DataFrame(lienamif) 

originf=[]

for ami in amif :
    ami = " ".join(ami.split(" ", 2)[:2])
    originf.append(ami)

lienamif2=list(zip(originf, amif))

slll=0
longamif=0
slicer1=0
slicer2=number_of_unique_values[0]
pairsf=[]

totalf = 0
for ele in range(0, len(number_of_unique_values)):
    totalf = totalf + number_of_unique_values[ele]

def pop_random(lst):
    idx = random.randrange(0, len(lst))
    return lst.pop(idx)

while slll<=len(number_of_unique_values) :
        possssif=amif[slicer1:slicer2]
        if len(possssif) > 1 :
            if len(possssif) in (3,5,7,9) :
                posit=len(possssif)-1
                elem=possssif[posit]    
                possssif.append(elem)
            else :
                possssif=possssif
            while possssif:
                rand1f = pop_random(possssif)
                rand2f = pop_random(possssif)
                pair = rand1f, rand2f
                pairsf.append(pair) 
        slicer1=slicer2
        if slll+1 == len(number_of_unique_values) :
            break
        else:
            slll=slll+1
            slicer2=slicer2+number_of_unique_values[slll]
    
e=e.append(lienamif2, ignore_index=True) #Dictionnaire relation amies --> Répondant / Personnes cités
e=e.append(pairsf, ignore_index=True)


#Liens répondants --> Amis + Amis --> Personnes cites (Hommes)
    
df[52]=df[52].fillna(0) #Possibilité de suppr --> Utile si diff amitiés H/F
    
df['str53']=df[53].astype(str) #Indexe des personnes cités
nbnodefe2=list(df[52].fillna(0))  #NB Amis
nbnodefe2=([int(nbnodefe2) for nbnodefe2 in nbnodefe2])
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

for ele in indee: 
    if ele == 0: 
        indee.remove(ele) 
   
bb=0
df['count2'] = df['str53'].str.len()
count2=list(df['count2'])
aa1=0
aa2=0
lkk=len(dfn)


possi=[]

while bb<lkk :
    if df.iloc[bb][52] == 0 : #Nombre d'amis
        bbb=count2[bb]
        aa1=aa1+count2[bb]
        bb=bb+1
    if df.iloc[bb][52] != 0  :
        aaa=list(dfn.iloc [bb])
        aa1=aa1+count2[bb]
        ccc=[]
        ccc.append(indee[aa2:aa1])
        ccc=list(ccc)
        for num in ccc :
            for n in num :
                possi.append(aaa[n-1])
    aa2=aa1
    bb=bb+1

number_of_unique_value=list(Counter(cff).values())

aa=0
cc=0 # index count 2
bb1=0 #positionnels count 2 = slicer
bb2=0   #positionnels count 2
dd=0
lkki=len(count)
aleatoiree=[]



while cc<lkki :
    if df.iloc[cc][52] == 0 :
        aa=count[cc]
        bb1=bb1+int(aa)
        cc=cc+1
        bb2=bb1
    else :
        aa=count[cc]
        bb1=bb1+aa
        aaa=possible[bb2:bb1]
        ccc=number_of_unique_value[dd]
        ran=random.choices(aaa, k=ccc)
        aleatoiree.append(ran)
        dd=dd+1
        cc=cc+1
        bb2=bb1
     

flat_aleatoiree = [item for sublist in aleatoiree for item in sublist]

b=" AH" 

amih=[item+b for item in cff]
zardo=[item+b for item in cff]


dvb=0

while dvb<len(amih)-1:
    c1=2
    if amih[dvb] == amih[dvb+1] or amih[dvb].split(' ')[1] == amih[dvb+1].split(' ')[1] :
        amih[dvb+1]=amih[dvb]+str(c1)
        c1=c1+1
        dvb=dvb+1
    else :
        dvb=dvb+1
                        
lienamih = list(zip(amih, flat_aleatoiree))    
f=pd.DataFrame(lienamih) 

originh=[]

for ami in amih :
    ami = " ".join(ami.split(" ", 2)[:2])
    originh.append(ami)

lienamih2=list(zip(originh,amih))

totalh = 0
for ele in range(0, len(number_of_unique_value)):
    totalh = totalh + number_of_unique_value[ele]

sllh=0
longamih=0
slicer1h=0
slicer2h=number_of_unique_value[0]
pairsh=[]

while sllh<=len(number_of_unique_value) :
        possssih=amih[slicer1h:slicer2h]
        if len(possssih) != 1 :
            if len(possssih) in (3,5,7,9) :
                posit=len(possssih)-1
                elem=possssih[posit]    
                possssih.append(elem)
            else :
                possssih=possssih
            while possssih:
                    rand1 = pop_random(possssih)
                    rand2 = pop_random(possssih)
                    pair = rand1, rand2
                    pairsh.append(pair) 
        slicer1h=slicer2h
        if sllh+1 == len(number_of_unique_value) :
            break
        else:
            sllh=sllh+1
            slicer2h=slicer2h+number_of_unique_value[sllh]
            
f=f.append(lienamih2, ignore_index=True) #Dictionnaires hommes
f=f.append(pairsh, ignore_index=True)


amiff=f[0].tolist()
sanschiffre=[item+b for item in cff]

dfhf=df[[9,54]] 
homme='Homme'
femme='Femme'

dih = {k:homme for k in amih}
dif = {k:femme for k in amif}

dfhf2=df[[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]].transpose() #Personnes cité + sexes

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
dictionnairedesliens = dictionnairedesliens.drop_duplicates(subset=[0, 1], keep='first')

dictionnairedessexes.to_excel("Dictionnaire_attribut_sexe.xlsx")  
dictionnairedesliens.to_excel("Dictionnaire_liens.xlsx")  
    
    
