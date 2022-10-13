n=int(input())
# 0 1 1 2 3 5 8 13 21 34 55 ... - Fibonacy seq 
# n   =     5
def Fib(n):
    if n==0: return 0
    elif n==1: return 1
    else:                                                              # 1+0 + 1 +1 +0 +1+0+1+1+0
        return Fib(n-1)+Fib(n-2) # n=5 : (n=4 : (n=3 : (n=2 (: n=1 1 ), n=0 0), n=1 1) ,n=2 (: n=1 1 ), n=0 0) , n=3 : (n=2 (: n=1 1 ), n=0 0), n=1 1) ,n=2 (: n=1 1 ), n=0 0)
print (Fib(n)) 
#1 - 1 ===1 
#2 - 1+0 ===1
#3 - 2+1 -- 1+0 +1 ===2 
#4 - 3+2 -- 1+0+1+1+0 ===3
