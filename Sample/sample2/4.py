def fun(n):
    # 1 2 3 4 5 6 7  8 9 10 15 22 100 333  if 25*25=625
    for i in range(1,n):
        if deg(i):
            print(f'{i}*{i}={i*i}')
def deg (j):
    k=j
    i=0
    while k!=0 :
        k//=10
        i+=1
            
    if j==(j*j)%(10**i): return True 
    else: return False
n=int(input())
fun (n)

