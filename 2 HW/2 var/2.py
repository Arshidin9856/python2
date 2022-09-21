l=list(map(int,input().split()))
flag=0
if l[0]+l[1]==l[2]:flag=1
if l[1]+l[2]==l[0]:flag=1
if l[0]+l[2]==l[1]:flag=1
    
    
    
    
    
if flag :print("yes")
else: print('no')