n=int(input())
sum=0
while n!=0:
    x=n
    res=1
    while x<2*n+1:
        res=res*x # 1
        x=x+1
    sum+=res
    n=n-1
print(sum)