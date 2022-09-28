with open('name.txt','r' ) as names:
    res=[]
    r={}
    for name in names:
        b=True
        cnt=1
        for i in name:
            if b: res.append(i)
            if i==' ': 
                b=True
                cnt+=1
            else:b=False
        if cnt==2:
            init=res[-2]+res[-1]
            r[name]=init
        else:    
            init=res[-3]+res[-2]+res[-1]
            r[name]=init
    n=input()
    print(r)
    for i,j in r.items():
        if n== j: print(i)
        elif len(n)<len(j) and n[0]==j[0] and n[1]==j[-1]: print(i)
          