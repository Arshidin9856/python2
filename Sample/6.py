'''Find the Most Frequent Element in a List
Create a program that takes a list and return the most frequently occuring element contained within it.
Examples
[3, 7, 3] ➞ 3

[None, "hello", True, None]➞ None

[False, "up", "down", "left", "right", True, False] ➞ False'''
l=list(input().split())
q=[]
# for i in l:
#     s+=i
#     s+=' '
for i in l:
    cnt=0
    for j in l:
        if i == j and i not in q: 
            cnt+=1
    q.append(i)
    q.append(cnt)
max=q[1]    
for i in range(1,len(q),2) :
    if q[i]>max: max=q[i]  
    
for i in range (len(q)):
    if max==q[i]: print (q[i-1])
    
