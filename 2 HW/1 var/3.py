a=input()
c=input()
if len(c)>1 or len(c)==0:
     print('your input not char')
else:
    def findall(a,c):
        res=[]
        l=list(map(lambda x:x,a ))
        for i in range(len(l)): 
            if l[i] == c: res.append(i) 
        print(res)    
    findall(a,c)