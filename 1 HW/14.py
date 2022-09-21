sum=0
cnt=-1
n=None
try:
    while n!=0:
        n=int(input())
        sum+=n
        cnt+=1
    print(sum,sum/cnt)
except ValueError: print("Wrong input")