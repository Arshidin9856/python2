x=int(input())
four=(x%100)/10
x=x+(int(four)*10)
second=(x%10000)/1000
# print(second)
x=x+(int(second)*1000)
print(x)
