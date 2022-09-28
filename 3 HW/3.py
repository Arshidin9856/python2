# (a) All words ending in ime 
# (b) All words whose second, third, and fourth letters are ave 
# (c) How many words contain at least one of the letters r, s, t, l, n, e 
# (d) The percentage of words that contain at least one of the letters r, s, t, l, n
# (e) All words with no vowels 
# (f) All words that contain every vowel
import re
def ime(n):
    if n[-3:]=='ime':
        return True
def ave(n):
    if n[1:4]=='ave':
        return True
def rstlne(n):
    x=re.findall('[rstlne]',n)
    if len(x)!=0:
        return n
    else: return 0
def perc():
    cnt=0
    for i in l: 
            if i ==0 : continue
            else: cnt+=1
    perc=cnt*100/len(l)
    return perc    
def wv(n):
    x=re.findall('^[aeyuio]',n)
    if len(x)!=0:
            return n
    else: return 0
def nov(n):
    for i in n:
        if i in ['a','e','y','u','i','o']:
            return 0
    
    return n
    
l=[]
withvovels=[]
vovels=[]

with open('for3.txt','r') as text:
    for i in text:
        ListOfWords=i.split()
        for j in ListOfWords:
            # if ime(j): print(j) 
            # if ave(j): print(j)   
            # l.append(rstlne(j))
            # withvovels.append(wv(j))
            vovels.append(nov(j))
        # print(perc())
        # print(withvovels)
        print(vovels)