datesOfBirth= {'user1':'01/02/03','user3':'03/03/03','user2':'02/02/02'}
for i in datesOfBirth.keys():
    print (f'we have: {i}')
n=input ("Choose name")
b=True
for i,j in datesOfBirth.items():
    if n==i:
        print (f'{i}`s birthday is {datesOfBirth.get(i)}')
        b=False    
if b:print ('wrong name')