try:
    x=int(input("input number: "))
    for i in range(1,11) : print(f'{x}*{i} = {x*i}')
except ValueError: print("wrong input")