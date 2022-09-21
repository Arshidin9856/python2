x=[0,0]
up=int(input())
left=int(input())
right=int(input())
down=int(input())
x[1]= x[1]+up
x[1]= x[1]-down
x[0]= x[0]+right
x[0]= x[0]-left
d=(x[0]**2+x[1]**2)**0.5
print(d//1)
