# List of months: January, February, March, April,May, June, July, August, September, October, November, December
# Input the name of Month: FebruaryNo. of days: 28/29 days
listOfMonths=['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
Mon=input('Input the name of Month: ')
try: 
    x=listOfMonths.index(Mon)
    Even=False
    if x>6:x=x-7
    if x%2==0: Even=True
    if Even and not Mon=='February': print ('No. of days: 31 days')
    elif Mon=='February': print ('No. of days: 28/29 days')
    else:  print ('No. of days: 30 days')
except: print ("wrong input")
