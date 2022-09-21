# Input a year: 2016
# Input a month [1-12]: 08
# Input a day [1-31]: 23
# The next date is [yyyy-mm-dd] 2016-8-24


try:
    import datetime
    Y=int(input())
    M=int(input())
    D=int(input())
    MyDay=datetime.datetime(Y,M,D)
    x=MyDay+datetime.timedelta(days=1)
    print(f' tommorow is --- {x.strftime("%Y-%m-%d")}')
except ValueError: print('wrong input')