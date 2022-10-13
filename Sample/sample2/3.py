f=open('data.txt','r')
s=f.read()
f.close()
l=s.split()
for i in l:
    i=int(i)
l.sort()
print(l)