# Input your birth year: 1986 1986-1912= 74//12=6
# Your Zodiac sign: Tiger
# 1912-rat pig-1923
l=['rat', 'ox', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'goat', 'monkey', 'rooster', 'dog', 'pig']
try:
    Year=int(input('Input your birth year: '))
    x=(Year-1912)//12
    i=(Year-1912)-12*x
    print (l[i])
except ValueError: print ('wrong input')