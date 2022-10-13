def pal(n): #aabbaa 6/2  AAbAA
    b=False
    if len(n)%2==0:
        s=n[:len(n)//2]
        q=n[len(n)//2:]
        for i in range(len(n)//2):
            if s[i]==q[(len(n)//2)-i-1]:
                b=True
            else: b=False   
        return b    
    else:
        s=n[:len(n)//2]
        q=n[len(n)//2+1:]
        
        for i in range(len(s)):
            if s[i]==q[len(s)-i-1]:
                b=True
            else: b=False
        return b
n=input()
if (pal(n)) : print (f'{n} is palindrom')
else : print ('No')
# : print(f'{n} is palindrom') 
