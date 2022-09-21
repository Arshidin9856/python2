s=input()
n=input()
cnt=0
cnt1=0
b=0
for i in s:
    if i in n:
        cnt+=1
if cnt==len(s):
    for i in n:
        if i in s:cnt1+=1
        else :cnt1=0
        if cnt1==len(s):
            print(True)
            b=1            
if not b: print(False)