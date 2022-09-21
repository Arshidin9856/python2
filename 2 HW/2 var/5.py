def word():
    for i in l: print(i,end='')
    print()
def findall(a,c):
        res=[]
        l=list(map(lambda x:x,a ))
        for i in range(len(l)): 
            if l[i] == c: res.append(i) 
        return res
x="EVAPORATE"
l=list(map(lambda i: "_",x))
lis=[]
print('Welcome to Hangman!')
while "_" in l:
    word()
    guess=input("Letter: ")
    if guess in lis: print("alredy used:")
    lis.append(guess)
    if guess in x: 
        for i in findall(x,guess):
            l[i]=guess
    else : print("wrong guess")

word()