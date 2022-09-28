with open('st.txt','r') as f :
    with open ('st2.txt','w') as res:
        for i in f:
            name,surname,li,num=i.split()
            l=name.capitalize()+' '+surname.capitalize()+' '+li+' 301-'+num
            
            res.write(l)
            res.write('\n')


