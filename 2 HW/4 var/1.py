l=list(map(int,input().split()))
res=[]
for i in l:

    if i%2!=0: res.append(i)
res.sort()   
if len(res)>0: 
    print(res[0])
else: print('not found')