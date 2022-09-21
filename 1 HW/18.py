s=''
for i in range(6):
    if i%3==0 and not i==0: continue
    s+=str(i)+' '

print(s)