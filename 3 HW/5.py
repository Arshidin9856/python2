# 2  
# DEXTER <dexter@hotmail.com>
# VIRUS <virus!@variable.:p>
# Sample Output
# DEXTER dexter@hotmail.com
import re
n=int(input())
l=[]
while n!=0:
    em=input()
    if em[-9:-1]=='mail.com':
        em=re.sub('<|>','',em)
        l.append(em)

    n-=1
for i in l:
    print (i)
    