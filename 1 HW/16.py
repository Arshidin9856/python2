try:
    x=int(input("input int: "))
    for i in range(1,x+1):
        s=''
        for j in range (1,i+1):s+=str(i)
        print(s)
except ValueError: print("input wrong")