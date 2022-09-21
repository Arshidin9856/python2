x=int(input())
f=x//100
s=(x%100)//10
l=x%10
if x==f**3+s**3+l**3: print('yes')
else :print('no')