import re
month=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
date=input('Enter date: ')
x=re.sub('(\s|[,])','.',date)
x=x.split('.')
mon=x[0][:3].lower()
l=[]
for i in x:
   if i!='':
      l.append(i)
if mon in month:
   print(f'{month.index(mon)+1}/{l[1]}/{l[2][-2:]}')


