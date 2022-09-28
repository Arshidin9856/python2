# 42536258796157867       #17 digits in card number → Invalid 
# 4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
# 5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
# 44244x4424442444        #Contains non digit characters → Invalid
# 0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
import re
d={}
def le(n):
    cnt=0
    if len(n)>20:
        return 0
    for i in n:
        if ord(i)>=48 and ord(i)<=57 :
            cnt+=1
    return cnt 
n= int(input())
b=False
while n!=0:
    creditnum=input() #5123 - 3567 - 8912 - 3456
    # print(le(creditnum))
    if le(creditnum)!=16:
        d[creditnum]='invalid'
    else:
        for i in creditnum:
            cnt=0
            for j in creditnum:
                if i==j: cnt+=1
                elif j=='-': continue
                else: cnt=0 
                if cnt==4:
                    b=True
                    d[creditnum]='invalid'
        if  not b: 
                          
            x=re.fullmatch('(\A(4|5|6)\d{15})|((\d{4})-(\d{4})-(\d{4})-(\d{4}))',creditnum)
            if x!=None:
                d[creditnum]='valid'
            else:    d[creditnum]='invalid'
    n-=1
for i,j in d.items(): print(i,j)        
    
    