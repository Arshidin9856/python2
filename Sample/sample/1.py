def Fib( n,a=0,b=1) : #0112


    if n==0:
        print(b)
    n=n-1 #3 
    c=a+b
    d=c+b
    
    a=c
    b=d
    Fib(n-1,a,b) 

        

n= int(input())
print(Fib(n))