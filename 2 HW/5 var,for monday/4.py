def findall(a,c):
        res=[]
        l=list(map(lambda x:x,a ))
        for i in range(len(l)): 
            if l[i] == c: res.append(i) 
        return res  
L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
s=input() #*a*a****
for i in L:
    res=''
    cnt=0        
    for j in s:
        if j!='*':
            ind=s.find(j)
            if i[ind]==j:
                res+=j
        else: 
            res+=i[cnt]
        cnt+=1
        if len(res)==len(i) and res==i:
            print(res)