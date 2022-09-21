s=input()
d={}
for i in s:
    cnt=0
    for j in s:
        if i==j: cnt+=1
    d[i]=cnt 
print(d)      