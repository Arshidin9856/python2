code=input()
word=input()
mach={}
res=[]
def check():
    # print(mach)
    for i,j in mach.items():
        cnt=-1
        for x,y in mach.items():
            if j==y: cnt+=1
            elif cnt>=1 and i!=x: return False
    return True

for i,c in enumerate(word):
    if c not in mach: mach[c]=code[i]

for i,c in enumerate(word):
    t=False
    for k,j in enumerate(code):
        if c==j and i==k: t=False
        elif mach[c]==j and i==k and check(): t=True
        else: t=False
        if t: res.append(c)
if len(res)==len(word) : print(f'{code} would be an encoding of {word}.')
else: print("wrong code")