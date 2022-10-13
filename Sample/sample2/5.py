s=input()
a=['i','a','u','y','e','o']
q=str()

b=True
c=True
if s[0] not in a :

    for i in s:

        if i not in a and b:
            
            q+=i
            
        else: b=False    
    for i in q:
        s+=i
    print (s[len(q):]+'yo')
else:
    for i in s:

        if i in a and c:
            
            q+=i
            
        else: c=False    
    for i in q:
        s+=i
    print (s[len(q):]+'ayo')