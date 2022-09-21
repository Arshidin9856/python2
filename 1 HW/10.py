# Input birthday: 15
# Input month of birth (e.g. march, july etc): may
# Your Astrological sign is: Taurus
try: 
    Day=int(input('Input birthday: '))
    Mon=input('Input month of birth: ')
    listOfMonths=['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    x=listOfMonths.index(Mon)
    l=['Capricorn','Aquarius','Pisces','Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius']
    for i in range(len(listOfMonths)):
        if (x==i-1 and Day>=22) or (x==i and Day<=21) : print(l[i])

except: ValueError: print('wrong input') 
