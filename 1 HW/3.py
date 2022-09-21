# For the first two years, a dog year is equal to 10.5 human years.
# After that, each dog year equals 4 human years.
# ExpectedOutput: Input a dog's age in human years: 15
# The dog's age in dog's years is 73
try:
    AgeInHuman=int(input('Input a dog\'s age in human years:'))
    def toDogs(n):
        sum=21
        if n==2:
            print ('The dog\'s age in dog\'s years is 21')
        elif n==1:
            print ('The dog\'s age in dog\'s years is 10.5')
        elif n==0: print('The dog\'s age in dog\'s years is 0') 
        else:
            while  not n<3:
                sum+=4
                n=n-1
            else: print(f'The dog\'s age in dog\'s years is {sum}')
    toDogs(AgeInHuman)

except:
    print ('your input is not int')
