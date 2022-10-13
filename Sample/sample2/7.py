# list [] 1 2 3 of  11 11 2 not
n=input()
L=n.split()
b=True
for i in range (len(L)):
    k=L[i]
    L[i]= None
    for j in L:
        if k==j: 
            b=False
if b: print ('Yes') 
else: print ('No')