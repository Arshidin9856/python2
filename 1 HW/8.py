# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# ExpectedOutput:
# Input lengths of the triangle sides:
# x: 6
# y: 8
# z: 12
# Scalene triangle
x=input("x: ")
y=input("y: ")
z=input("z: ")
try:
    x=int(x)
    y=int(y)
    z=int(z)
    l=[x,y,z]
    for i in l: z=5/i
    for i in l:
        cnt=0
        for j in l:
            if i==j: cnt+=1
        if cnt>=2:print ("isosceles triangle")
        break
    if x==y==z: print ("equilateral triangle") 
    elif  not x==y==z: print ( 'Scalene triangle')
except ValueError:
    print ('Your input data must be int type:')
except ZeroDivisionError:
    print ('Your input data must be nonzero')