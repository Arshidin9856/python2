import random
x=random.randint(1,100)
cnt=0
print(x)
guess=0
while cnt<3 and guess!=x:
    guess=int(input())
    if guess>x:
         print('The number is fewer') 
         cnt+=1
    elif guess<x: 
        print('The number is more')
        cnt+=1
    if guess==x: print('BINGO')
