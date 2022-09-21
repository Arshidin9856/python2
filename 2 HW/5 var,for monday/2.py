x=int(input())
f=x//100
s=(x%100)//10
l=x%10
if l>=s>=f: print('Yes')
else: print("no")