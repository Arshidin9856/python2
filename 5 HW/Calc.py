from tkinter import *
from tkinter import  messagebox,ttk
import math,sys,random
root = Tk() 
root.title("Calculator")
root.resizable(width=False, height=False)
bttn_list = [
"2nd", "(", ")", "10^x", "AC","<-","+/-","/", 
"1/x", "x^2", "x^3", "y^x", "7","8","9","*",
"x!", "-/", "x-/y",  "lg", "4","5","6","-",
"sin","cos", "tan", "ln","1","2","3","+",
"π", "Rand", "Deg", "Rad","%","0",".","="]

calc_entry = Entry(master=root,width=75,foreground='black',borderwidth=5)
calc_entry.grid(row=0, column=0,columnspan=7)
memore=[]
deg=True
def calc(x):
    global memore,deg
    if x=='=' :
        try:
                    result = eval(calc_entry.get())
                    calc_entry.insert(END, "=" + str(result))
        except:
                    calc_entry.insert(END, "Error!")
                    messagebox.showerror("Error!", "Check the correctness of data")    
    elif x in '0123456789':
        calc_entry.insert(END,x)
    elif x in '/*-+.()':
        calc_entry.insert(END,x)
    elif x=="AC":
        calc_entry.delete(0,END)
    elif x=="Deg":
        deg=True    
    elif x=='Rad':
        deg=False
    elif x=='π':calc_entry.insert(END,math.pi)
    elif x=='Rand':calc_entry.insert(END,random.random())

    elif x=='+/-':
        if '-' in calc_entry.get():
            st=calc_entry.get()[-1:]
            ind=calc_entry.get().find(st)
        
            calc_entry.delete(ind-1,ind)
            calc_entry.insert(ind-1,'+')
        elif '+' in calc_entry.get():
            st=calc_entry.get()[-1:]
            ind=calc_entry.get().find(st)
            calc_entry.delete(ind-1,ind)
            calc_entry.insert(ind-1,'-')
        else:
            if calc_entry.get()[0]=='-':
                calc_entry.delete(0,1)
            else:    calc_entry.insert(0,'-')
    elif x=='<-':
        st=len(calc_entry.get())
        calc_entry.delete(st-1,END)   
    elif x=='%':     
        if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
            x=calc_entry.get()
            calc_entry.delete(0,END)
            calc_entry.insert(0,float(x)/100)
        else:
            st=calc_entry.get()[-1:]
            ind=calc_entry.get().find(st)
            calc_entry.delete(ind,ind+1)
            calc_entry.insert(ind,float(st)/100)
    elif x=='10^x':        
        if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
            x=calc_entry.get()
            calc_entry.delete(0,END)
            calc_entry.insert(0,pow(10,float(x)))
        else:
            st=calc_entry.get()[-1:]
            ind=calc_entry.get().find(st)
            calc_entry.delete(ind,ind+1)
            calc_entry.insert(ind,pow(10,float(st)))
    elif x=='1/x':
        if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
            x=calc_entry.get()
            calc_entry.delete(0,END)
            calc_entry.insert(0,1/float(x))
        else:
            st=calc_entry.get()[-1:]
            ind=calc_entry.get().find(st)
            calc_entry.delete(ind,ind+1)
            calc_entry.insert(ind,1/float(st))
    elif x=='x^2':  
        if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
            x=calc_entry.get()
            calc_entry.delete(0,END)
            calc_entry.insert(0,float(x)**2)
        else:
            st=calc_entry.get()[-1:]
            ind=calc_entry.get().find(st)
            calc_entry.delete(ind,ind+1)
            calc_entry.insert(ind,float(st)**2)      

    elif x=='x^3':  
        if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
            x=calc_entry.get()
            calc_entry.delete(0,END)
            calc_entry.insert(0,float(x)**3)
        else:
            st=calc_entry.get()[-1:]
            ind=calc_entry.get().find(st)
            calc_entry.delete(ind,ind+1)
            calc_entry.insert(ind,float(st)**3)      

    elif x=='y^x':  
        calc_entry.insert(END,'**')
    elif x=='x!':
        if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
            x=calc_entry.get()
            calc_entry.delete(0,END)
            calc_entry.insert(0,math.factorial(float(x)))
        else:
            st=calc_entry.get()[-1:]
            ind=calc_entry.get().find(st)
            calc_entry.delete(ind,ind+1)
            calc_entry.insert(ind,math.factorial(float(st))) 
    elif x=='-/':
        if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
            x=calc_entry.get()
            calc_entry.delete(0,END)
            calc_entry.insert(0,math.sqrt(float(x)))
        else:
            st=calc_entry.get()[-1:]
            ind=calc_entry.get().find(st)
            calc_entry.delete(ind,ind+1)
            calc_entry.insert(ind,math.sqrt(float(st))) 
    elif x=='lg':
        if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
            x=calc_entry.get()
            calc_entry.delete(0,END)
            calc_entry.insert(0,math.log10(float(x)))
        else:
            st=calc_entry.get()[-1:]
            ind=calc_entry.get().find(st)
            calc_entry.delete(ind,ind+1)
            calc_entry.insert(ind,math.log10(float(st))) 
    elif x=='sin':
        if deg:
            if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
                x=calc_entry.get()
                calc_entry.delete(0,END)
                n_deg = float(x)*math.pi/180
                calc_entry.insert(0,math.sin(n_deg))
            else:
                st=calc_entry.get()[-1:]
                ind=calc_entry.get().find(st)
                calc_entry.delete(ind,ind+1)
                n_deg = float(st)*math.pi/180
                
                calc_entry.insert(ind,math.sin(n_deg)) 
        else:
            if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
                x=calc_entry.get()
                calc_entry.delete(0,END)
                calc_entry.insert(0,math.sin(float(x)))
            else:
                st=calc_entry.get()[-1:]
                ind=calc_entry.get().find(st)
                calc_entry.delete(ind,ind+1)  
                calc_entry.insert(ind,math.sin(float(st))) 
                
            
    elif x=='cos':
        if deg:
            if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
                x=calc_entry.get()
                calc_entry.delete(0,END)
                n_deg = float(x)*math.pi/180
                calc_entry.insert(0,math.cos(n_deg))
            else:
                st=calc_entry.get()[-1:]
                ind=calc_entry.get().find(st)
                calc_entry.delete(ind,ind+1)
                n_deg = float(st)*math.pi/180
                
                calc_entry.insert(ind,math.cos(n_deg)) 
            
        else:

            if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
                    x=calc_entry.get()
                    calc_entry.delete(0,END)
                    calc_entry.insert(0,math.cos(float(x)))
            else:
                    st=calc_entry.get()[-1:]
                    ind=calc_entry.get().find(st)
                    calc_entry.delete(ind,ind+1)
                    calc_entry.insert(ind,math.cos(float(st))) 
    elif x=='tan':
        if deg:
            if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
                x=calc_entry.get()
                calc_entry.delete(0,END)
                n_deg = float(x)*math.pi/180
                calc_entry.insert(0,math.tan(n_deg))
            else:
                st=calc_entry.get()[-1:]
                ind=calc_entry.get().find(st)
                calc_entry.delete(ind,ind+1)
                n_deg = float(st)*math.pi/180
                
                calc_entry.insert(ind,math.tan(n_deg)) 
            
        else:

            if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
                    x=calc_entry.get()
                    calc_entry.delete(0,END)
                    calc_entry.insert(0,math.tan(float(x)))
            else:
                    st=calc_entry.get()[-1:]
                    ind=calc_entry.get().find(st)
                    calc_entry.delete(ind,ind+1)
                    calc_entry.insert(ind,math.tan(float(st))) 
    elif x=='ln':
        if '+' not in calc_entry.get() and '-' not in calc_entry.get() and '*' not in calc_entry.get() and '/' not in calc_entry.get():
            x=calc_entry.get()
            calc_entry.delete(0,END)
            calc_entry.insert(0,math.log(float(x)))
        else:
            st=calc_entry.get()[-1:]
            ind=calc_entry.get().find(st)
            calc_entry.delete(ind,ind+1)
            calc_entry.insert(ind,math.log(float(st))) 
r = 1
c = 0
for i in bttn_list:
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i,command=cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c >= 8:
        c = 0
        r += 1
root.mainloop()