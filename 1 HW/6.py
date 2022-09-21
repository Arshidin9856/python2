try :
    a,b=int(input()),int(input())
    c=a+b if not (a+b<=20 and a+b>=15) else 20
    print (c)
except : print ('your input not int')