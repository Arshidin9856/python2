x=int(input())
last=x%10
first=x//100
d=last-first
x=x%100
x=last*100+x-d
print(x)