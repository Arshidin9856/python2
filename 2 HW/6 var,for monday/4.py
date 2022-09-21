import re
l=list(input().split(','))
for i in l:
    if type(re.search('[a-zA-Z]',i)) != type(None): 
        if type(re.search('\d',i)) !=type(None) :
            if type(re.search('[$#@]',i))!=type(None):
                if type(re.search('\s',i))==type(None):
                    print(i) 
        