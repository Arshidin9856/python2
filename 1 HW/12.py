# Input first number: 15Input second number: 26Input third number: 29
try :

    x,y,z=int(input('first number: ')),int(input('second number: ')),int(input('third number: '))
    l=[x,y,z]
    l.sort()
    print(l[1])




except ValueError: print('wrong input')
