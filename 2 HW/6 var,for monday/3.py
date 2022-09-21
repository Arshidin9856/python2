a=input()
res=[]
for i in a:
    if ord(i.lower())>=97 and ord(i.lower())<=122:
        res.append(ord(i.lower())-96)
print(res)