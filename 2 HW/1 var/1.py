# Given the coefficients a, b, c of the equation ax2 + bx + c = 0. Find a solution. 
# Please consider exceptions, like no roots (0.25 points)
try:
    a=int(input())
    b=int(input())
    c=int(input())
    disc=(b**2-4*a*c)
    if disc<0: print('no')
    elif disc==0:
        print(-b/(2*a))
    else : print(f'x1={(-b+(disc**0.5))/(2*a)}\nx2={(-b-(disc**0.5))/(2*a)}')    

    
except ValueError: print('wrong input')