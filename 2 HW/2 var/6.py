# 1 + 2 + 3*2*3! + 4*2*4! + ….+n*2*n!
def factorial(n):
    res=1
    while n!=0 :
        res=n*res
        n=n-1
    return res    
n=int(input())
res=3# 39+ 8*24+10*125 
for i in range (3,n+1):
    # print(i,res,factorial(i))
    res+=(i*2)*(factorial(i))
print(res)