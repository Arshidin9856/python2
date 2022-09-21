# Input the month (e.g. [1-12]): 07
# Input the day: 31
# Output: July, 31. 
# Season is autumn
try :
    Mon,Day=input("Input the month (e.g. [1-12]): "),int(input("Input the day: "))
    listOfMonths=['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    try: 
        x=listOfMonths.index(Mon)
        Even=False
        if x>6:x=x-7
        if x%2==0: Even=True
        if Even and not Mon=='February': 
            print ('No. of days: 31 days')
            if Day<=31 and Day>0: 
                if (Mon==listOfMonths[0] or Mon==listOfMonths[-1]):
                    print("Season is winter")
                elif  (Mon==listOfMonths[2] or Mon==listOfMonths[4]):
                    print("Season is spring")
                elif  (Mon==listOfMonths[6] or Mon==listOfMonths[7]):
                    print("Season is summer")
                elif  (Mon==listOfMonths[9]):
                    print("Season is autumn")
            else: print ('Day out of range')        

        elif Mon=='February': 
            print ('No. of days: 28/29 days')
            if Day<=29 and Day>0: 
                print("Season is winter")
            else: print ('Day out of range')        
            
        else:  
            print ('No. of days: 30 days')
            if Day<=30 and Day>0: 
                    if  (Mon==listOfMonths[3] ):
                        print("Season is spring")
                    elif  (Mon==listOfMonths[5] ):
                        print("Season is summer")
                    elif  (Mon==listOfMonths[8] or Mon==listOfMonths[10]):
                        print("Season is autumn")
            else: print ('Day out of range')        
            
    except:
        print ("wrong input")
except ValueError:
    print("Wrong input")
