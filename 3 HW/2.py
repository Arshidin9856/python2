from itertools import zip_longest
with open('st.txt','r') as first,open('st2.txt','r') as second,open('st3.txt','w') as s:
    for i,j in zip_longest(first,second,fillvalue='\n'):
        
        s.write(i.rstrip('\n')+j)                
                    
