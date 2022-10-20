from tkinter import *
from tkinter import messagebox
import tkinter as ttk
from PIL import Image , ImageTk
import psycopg2
from config import params
import time
import datetime
import re
import os

def create_table_orders():
    SQL = (
        '''
            CREATE TABLE IF NOT EXISTS orders (
            Order_ID serial Primary key,
            User_Name VARCHAR(255) NOT NULL ,
            Product_name Varchar(255) NOT NULL,
            Money VARCHAR(255) NOT NULL,
            Date_of_order time 
            )
        '''
    )

    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()
        
    except Exception as Error:
        print(str(Error))

def create_table_users():
    SQL = (
        '''0..........................................................................................................................................0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000










































































































































































































































































































































































































































































































        
        CREATE TABLE IF NOT EXISTS Users_Shop (
        User_ID serial Primary key,
        Name VARCHAR(255) NOT NULL , 
        Telephone VARCHAR(12) NOT NULL,
        Email VARCHAR(255) NOT NULL,
        Password VARCHAR(255) NOT NULL
        ) 
        '''
    )

    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()
        
    except Exception as Error:
        print(str(Error))



def create_table_product():
    SQL = (
        '''
        CREATE TABLE IF NOT EXISTS Products_shop (
        Product_ID serial Primary key,
        Product VARCHAR(255) NOT NULL , 
        Quantity VARCHAR(255) NOT NULL,
        Price VARCHAR(255) NOT NULL
        ) 
        '''
    )

    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()
        
    except Exception as Error:
        print(str(Error))


create_table_users()
create_table_product()
create_table_orders()

user_email = ''

def Window():
    global root
    root = Tk()
    root.title("Shop")
    root.geometry("900x300")
    root.resizable(False,False)
    
    path = 'p_back.png' 
    img = ImageTk.PhotoImage(Image.open(path)) 
    panel = ttk.Label(root, image = img) 
    panel.place(x=0, y=0, relwidth=1, relheight=1)

    button_about_us = Button(root,text="About us", command=str_about_us, fg='white', bg='grey', height=1, width=9)
    button_about_us.grid(column=0, row=0)
    button_login = Button(root,text="Login", command=str_login, fg='white', bg='grey', height=1, width=9)
    button_login.grid(column=1, row=0)
    button_reg = Button(root,text="Registration", command=str_reg, fg='white', bg='grey', height=1, width=13)
    button_reg.grid(column=2, row=0)

    


    root.mainloop()


def str_about_us():
    global root
    str_aboutus = Tk()
    str_aboutus.title("About us")
    str_aboutus.geometry("1000x600")

    root.destroy()    

    str_aboutus.mainloop()

def admin():
    admin_page = Tk()
    admin_page.title("Admin")
    admin_page.geometry("1000x600")

    def fprod():
        find = box.get()
        SQL = "SELECT * FROM orders where product_name ='" + str(find) + "'"
        print(SQL)
        try:
            config = psycopg2.connect(**params)
            query = config.cursor()
            query.execute(SQL)
            result = query.fetchall()
            query.close()
            config.commit()
            
        except Exception as Error:
            print(str(Error))
        sum = 0
        for x in result:
            sum +=int(x[3])
        l=Label(admin_page,text=str(sum))
        l.pack()

    def fname():
        find = box.get()
        SQL = "SELECT * FROM orders where user_name ='" + str(find) + "'"
        try:
            config = psycopg2.connect(**params)
            query = config.cursor()
            query.execute(SQL)
            result = query.fetchall()
            query.close()
            config.commit()
            
        except Exception as Error:
            print(str(Error))
        sum = 0
        for x in result:
            sum +=int(x[3])
        l=Label(admin_page,text=str(sum))
        l.pack()

    box = Entry(admin_page)
    box.pack()
    bprod = Button(admin_page,text="find by product", command=fprod)
    bprod.pack()
    bname = Button(admin_page,text="find by name", command=fname)
    bname.pack()

def str_login():
    global root, p_login
    p_login = Tk()
    p_login.title("Login")
    p_login.geometry("1000x600")

    label_login_form = Label(p_login, text="Login form",width=20,font=("bold", 20))
    label_login_form.place(x=300,y=53)
    label_name = Label(p_login, text="Email",width=20,font=("bold", 10))
    label_name.place(x=290,y=130)
    entry_name = Entry(p_login)
    entry_name.place(x=450,y=130)
    label_password = Label(p_login, text="Password",width=20,font=("bold", 10))
    label_password.place(x=278,y=180)
    entry_password = Entry(p_login, show="*")
    entry_password.place(x=450,y=180)
    def check():
        global user_email
        user_email = entry_name.get()
        SQL = "Select * from Users_Shop where email  = '" + user_email +"' and password = '" + entry_password.get() +"'" 
        # print("Here")
        try:
            config = psycopg2.connect(**params)
            query = config.cursor()
            query.execute(SQL)
            res = query.fetchall()
            query.close()
            config.commit()
            
        except Exception as Error:
            print(str(Error))
        
        if len(res)!=0:
            if user_email != 'Admin':
                str_variants()
            else:
                admin()
        else:     
            label_war = Label(p_login, text="The user with that email doesnt exists!\nTry again!",width=30,font=("bold", 10))
            label_war.place(x=350,y=500)
    Button(p_login, text='Login', command = check, width=20,bg='red',fg='white').place(x=390,y=230)
    print(user_email)
    root.destroy()
    p_login.mainloop()


def str_reg():
    global p_reg
    p_reg = Tk()
    p_reg.title("Registration")
    p_reg.geometry("1000x600")

    def reg_user():
        b=False
        name = entry_name.get()
        email = entry_email.get()
        telephone = entry_telephone.get() #87761812566
        password = entry_password.get()
      

        try:
            if re.findall('\W',name)==[] and re.search('([+]7|8)\d{10}',telephone)[0]==telephone and re.search('.{8,}$',password)[0]==password:
                b=True
                
        except Exception as Error:
            print(str(Error))

        SQL = "Select * from Users_Shop where email = '" + email +"'" 
        # print("Here")
        try:
            config = psycopg2.connect(**params)
            query = config.cursor()
            query.execute(SQL)
            res = query.fetchall()
            query.close()
            config.commit()
            
        except Exception as Error:
            print(str(Error))

        if len(res)!=0:
            label_war = Label(p_reg, text="The user with that email already exists!\nTry again!",width=30,font=("bold", 10))
            label_war.place(x=350,y=500)
        else:
            if b:
                
                SQL = "Insert into Users_Shop (Name,Telephone,Email,Password) values ('"+name+"', '"+telephone+"','"+email+"', '"+password+"')"
                try:
                    config = psycopg2.connect(**params)
                    query = config.cursor()
                    query.execute(SQL)
                    query.close()
                    config.commit()
                    
                except Exception as Error:
                    print(str(Error))
            else: print('wrong input')

            p_reg.destroy()
            str_login()

    label_reg_form = Label(p_reg, text="Registration form",width=20,font=("bold", 20))
    label_reg_form.place(x=300,y=53)
    label_name = Label(p_reg, text="User Name:",width=20,font=("bold", 10))
    label_name.place(x=290,y=130)
    entry_name = Entry(p_reg)
    entry_name.place(x=450,y=130)
    label_email = Label(p_reg, text="Email:",width=20,font=("bold", 10))
    label_email.place(x=278,y=180)
    entry_email = Entry(p_reg)
    entry_email.place(x=450,y=180)
    label_telephone = Label(p_reg, text="Telephone:",width=20,font=("bold", 10))
    label_telephone.place(x=280,y=230)
    entry_telephone = Entry(p_reg)
    entry_telephone.place(x=450,y=230)
    label_password = Label(p_reg, text = "Password:", width=20)
    label_password.place(x=290,y=280)
    entry_password = Entry(p_reg,show = "*")
    entry_password.place(x=450,y=280)
    global root
    root.destroy()

    Button(p_reg, text='Submit',width=20,bg='red',fg='white', command= reg_user).place(x=390,y=380)

    p_reg.mainloop()


def str_variants():
    global flag
    str_products = Tk()
    str_products.title("Variants of animals")
    str_products.geometry("1000x600")
    p_login.destroy()


    
    
    SQL = "Select * from products_shop"
 
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()
        
    except Exception as Error:
        print(str(Error))
    print(res)


    flag=False
    def buy_1():
        global root, p_pay
        p_pay = Tk()
        p_pay.title("pay")
        p_pay.geometry("1000x600")

        label_credit_card = Label(p_pay, text="Enter Your credit card",width=20,font=("bold", 20))
        label_credit_card.place(x=300,y=53)
        label_name = Label(p_pay, text="credit card",width=20,font=("bold", 10))
        label_name.place(x=290,y=130)
        entry_name = Entry(p_pay)
        entry_name.place(x=450,y=130)
        def pay():
            SQL = "Select * from products_shop"
 
            try:
                config = psycopg2.connect(**params)
                query = config.cursor()
                query.execute(SQL)
                res = query.fetchall()
                query.close()
                config.commit()
                
            except Exception as Error:
                print(str(Error))


            global root, p_check
            p_check = Tk()
            p_check.title("Check")
            p_check.geometry("1000x600")
            # label_1 = Label(p_check, text='check',width=20,font=("bold", 10))
            # label_1.grid(column = 0, row=0)
            credit_card=entry_name.get()
            credit_card=credit_card.replace(' ','')
            # for i in credit_card:
            
            
            
            if re.search('[0-9]{16}',credit_card)[0]==credit_card:
                

                tim=datetime.datetime.now()
                SQL = "INSERT into orders (user_name,product_name,money,date_of_order) values ('" + user_email +"','"+res[0][1]+"','"+str(res[0][3]) +"','" + str(tim) + "')"
                try:
                    config = psycopg2.connect(**params)
                    query = config.cursor()
                    query.execute(SQL)
                    query.close()
                    config.commit()
                    
                except Exception as Error:
                    print(str(Error))
                new = int(res[0][2])-1
                if new > 0:
                    SQL = "UPDATE products_shop SET quantity = '" + str(new) +"'  WHERE product_id ='" + str(res[0][0]) +"';"  
                    try:
                        config = psycopg2.connect(**params)
                        query = config.cursor()
                        query.execute(SQL)
                        query.close()
                        config.commit()
                    except Exception as Error:
                        print(str(Error))
                        
                    
            
                    label_1 = Label(p_check, text=f"Shop 1: {res[0][1]} ------------------ '"+str(res[0][3]) +"'   thank you!",width=200,font=("bold", 10))
                    label_1.pack()
                    f= open("check.txt","w+")
                    f.write( user_email+": "+res[0][1]+" ------------------ "+str(res[0][3])+" USD   thank you!")
                    f.close
                    if root.destroy():
                        os.remove("check.txt")
                    root.destroy()
                    p_check.mainloop()
                else:
                    label_1 = Label(p_check, text="There is no that product, Sorry!",width=200,font=("bold", 10))
                    label_1.pack()

            else:
                label_nam = Label(p_pay, text="wrong input",width=20,font=("bold", 10))
                label_nam.place(x=450,y=400)
                p_check.destroy()
                # root.destroy()

        Button(p_pay, text='pay', command = pay, width=20,bg='red',fg='white').place(x=390,y=230)
    
        root.destroy()
        p_pay.mainloop()

        

    label_1 = Label(str_products, text=res[0][1],width=20,font=("bold", 10))
    label_1.grid(column = 0, row=0)
    b1 = Button(str_products,text=str(res[0][3]) + " USD",command = buy_1, width=20,bg='red',fg='white')
    b1.grid(column = 0, row = 1)

    def buy_2():
        global root, p_pay
        p_pay = Tk()
        p_pay.title("pay")
        p_pay.geometry("1000x600")

        label_credit_card = Label(p_pay, text="Enter Your credit card",width=20,font=("bold", 20))
        label_credit_card.place(x=300,y=53)
        label_name = Label(p_pay, text="credit card",width=20,font=("bold", 10))
        label_name.place(x=290,y=130)
        entry_name = Entry(p_pay)
        entry_name.place(x=450,y=130)
        def pay():
            SQL = "Select * from products_shop"
 
            try:
                config = psycopg2.connect(**params)
                query = config.cursor()
                query.execute(SQL)
                res = query.fetchall()
                query.close()
                config.commit()
                
            except Exception as Error:
                print(str(Error))


            global root, p_check
            p_check = Tk()
            p_check.title("Check")
            p_check.geometry("1000x600")
            # label_1 = Label(p_check, text='check',width=20,font=("bold", 10))
            # label_1.grid(column = 0, row=0)
            credit_card=entry_name.get()
            credit_card=credit_card.replace(' ','')
            # for i in credit_card:
            
            
            
            if re.search('[0-9]{16}',credit_card)[0]==credit_card:
                

                tim=datetime.datetime.now()
                SQL = "INSERT into orders (user_name,product_name,money,date_of_order) values ('" + user_email +"','"+res[1][1]+"','"+str(res[1][3]) +"','" + str(tim) + "')"
                print(SQL)
                try:
                    config = psycopg2.connect(**params)
                    query = config.cursor()
                    query.execute(SQL)
                    query.close()
                    config.commit()
                    
                except Exception as Error:
                    print(str(Error))
                new = int(res[1][2])-1
                if new > 0:
                    SQL = "UPDATE products_shop SET quantity = '" + str(new) +"'  WHERE product_id ='" + str(res[1][0]) +"';"  
                    try:
                        config = psycopg2.connect(**params)
                        query = config.cursor()
                        query.execute(SQL)
                        query.close()
                        config.commit()
                    except Exception as Error:
                        print(str(Error))
                        
                    
            
                    label_1 = Label(p_check, text=f"Shop 1: {res[1][1]} ------------------ '"+str(res[1][3]) +"'   thank you!",width=200,font=("bold", 10))
                    label_1.pack()
                    f= open("check.txt","w+")
                    f.write( user_email+": "+res[1][1]+" ------------------ "+str(res[1][3])+" USD   thank you!")
                    f.close
                    if root.destroy():
                        os.remove("check.txt")
                    root.destroy()
                    p_check.mainloop()
                else:
                    label_1 = Label(p_check, text="There is no that product, Sorry!",width=200,font=("bold", 10))
                    label_1.pack()

            else:
                label_nam = Label(p_pay, text="wrong input",width=20,font=("bold", 10))
                label_nam.place(x=450,y=400)
                p_check.destroy()
                # root.destroy()

        Button(p_pay, text='pay', command = pay, width=20,bg='red',fg='white').place(x=390,y=230)
    
        root.destroy()
        p_pay.mainloop()


    label_2 = Label(str_products, text=res[1][1],width=20,font=("bold", 10))
    label_2.grid(column = 1, row=0)
    b2 = Button(str_products,text=str(res[1][3]) + " USD",command = buy_2, width=20,bg='red',fg='white')
    b2.grid(column = 1, row = 1)

    def buy_3():
        global root, p_pay
        p_pay = Tk()
        p_pay.title("pay")
        p_pay.geometry("1000x600")

        label_credit_card = Label(p_pay, text="Enter Your credit card",width=20,font=("bold", 20))
        label_credit_card.place(x=300,y=53)
        label_name = Label(p_pay, text="credit card",width=20,font=("bold", 10))
        label_name.place(x=290,y=130)
        entry_name = Entry(p_pay)
        entry_name.place(x=450,y=130)
        def pay():
            SQL = "Select * from products_shop"
 
            try:
                config = psycopg2.connect(**params)
                query = config.cursor()
                query.execute(SQL)
                res = query.fetchall()
                query.close()
                config.commit()
                
            except Exception as Error:
                print(str(Error))

            global root, p_check
            p_check = Tk()
            p_check.title("Check")
            p_check.geometry("1000x600")
            # label_1 = Label(p_check, text='check',width=20,font=("bold", 10))
            # label_1.grid(column = 0, row=0)
            credit_card=entry_name.get()
            credit_card=credit_card.replace(' ','')
            # for i in credit_card:
            
            
            
            if re.search('[0-9]{16}',credit_card)[0]==credit_card:
                

                tim=datetime.datetime.now()
                SQL = "INSERT into orders (user_name,product_name,money,date_of_order) values ('" + user_email +"','"+res[2][1]+"','"+str(res[2][3]) +"','" + str(tim) + "')"
                print(SQL)
                try:
                    config = psycopg2.connect(**params)
                    query = config.cursor()
                    query.execute(SQL)
                    query.close()
                    config.commit()
                    
                except Exception as Error:
                    print(str(Error))
                new = int(res[2][2])-1
                if new > 0:
                    SQL = "UPDATE products_shop SET quantity = '" + str(new) +"'  WHERE product_id ='" + str(res[2][0]) +"';"  
                    try:
                        config = psycopg2.connect(**params)
                        query = config.cursor()
                        query.execute(SQL)
                        query.close()
                        config.commit()
                    except Exception as Error:
                        print(str(Error))
                        
                    
            
                    label_1 = Label(p_check, text=f"Shop 1: {res[2][1]} ------------------ '"+str(res[2][3]) +"'   thank you!",width=200,font=("bold", 10))
                    label_1.pack()
                    f= open("check.txt","w+")
                    f.write( user_email+": "+res[2][1]+" ------------------ "+str(res[2][3])+" USD   thank you!")
                    f.close
                    if root.destroy():
                        os.remove("check.txt")
                    root.destroy()
                    p_check.mainloop()
                else:
                    label_1 = Label(p_check, text="There is no that product, Sorry!",width=200,font=("bold", 10))
                    label_1.pack()

            else:
                label_nam = Label(p_pay, text="wrong input",width=20,font=("bold", 10))
                label_nam.place(x=450,y=400)
                p_check.destroy()
                # root.destroy()

        Button(p_pay, text='pay', command = pay, width=20,bg='red',fg='white').place(x=390,y=230)
    
        root.destroy()
        p_pay.mainloop()




    label_3 = Label(str_products, text=res[2][1],width=20,font=("bold", 10))
    label_3.grid(column = 2, row=0)
    b3 = Button(str_products,text=str(res[2][3]) + " USD",command = buy_3, width=20,bg='red',fg='white')
    b3.grid(column = 2, row = 1)
    
    def buy_4():
        global root, p_pay
        p_pay = Tk()
        p_pay.title("pay")
        p_pay.geometry("1000x600")

        label_credit_card = Label(p_pay, text="Enter Your credit card",width=20,font=("bold", 20))
        label_credit_card.place(x=300,y=53)
        label_name = Label(p_pay, text="credit card",width=20,font=("bold", 10))
        label_name.place(x=290,y=130)
        entry_name = Entry(p_pay)
        entry_name.place(x=450,y=130)
        def pay():
            SQL = "Select * from products_shop"
 
            try:
                config = psycopg2.connect(**params)
                query = config.cursor()
                query.execute(SQL)
                res = query.fetchall()
                query.close()
                config.commit()
                
            except Exception as Error:
                print(str(Error))

            global root, p_check
            p_check = Tk()
            p_check.title("Check")
            p_check.geometry("1000x600")
            # label_1 = Label(p_check, text='check',width=20,font=("bold", 10))
            # label_1.grid(column = 0, row=0)
            credit_card=entry_name.get()
            credit_card=credit_card.replace(' ','')
            # for i in credit_card:
            
            
            
            if re.search('[0-9]{16}',credit_card)[0]==credit_card:
                

                tim=datetime.datetime.now()
                SQL = "INSERT into orders (user_name,product_name,money,date_of_order) values ('" + user_email +"','"+res[3][1]+"','"+str(res[3][3]) +"','" + str(tim) + "')"
                print(SQL)
                try:
                    config = psycopg2.connect(**params)
                    query = config.cursor()
                    query.execute(SQL)
                    query.close()
                    config.commit()
                    
                except Exception as Error:
                    print(str(Error))
                new = int(res[3][2])-1
                if new > 0:
                    SQL = "UPDATE products_shop SET quantity = '" + str(new) +"'  WHERE product_id ='" + str(res[3][0]) +"';"  
                    try:
                        config = psycopg2.connect(**params)
                        query = config.cursor()
                        query.execute(SQL)
                        query.close()
                        config.commit()
                    except Exception as Error:
                        print(str(Error))
                        
                    
            
                    label_1 = Label(p_check, text=f"Shop 1: {res[3][1]} ------------------ '"+str(res[3][3]) +"'   thank you!",width=200,font=("bold", 10))
                    label_1.pack()
                    f= open("check.txt","w+")
                    f.write( user_email+": "+res[3][1]+" ------------------ "+str(res[3][3])+" USD   thank you!")
                    f.close
                    if root.destroy():
                        os.remove("check.txt")
                    root.destroy()
                    p_check.mainloop()
                else:
                    label_1 = Label(p_check, text="There is no that product, Sorry!",width=200,font=("bold", 10))
                    label_1.pack()

            else:
                label_nam = Label(p_pay, text="wrong input",width=20,font=("bold", 10))
                label_nam.place(x=450,y=400)
                p_check.destroy()
                # root.destroy()

        Button(p_pay, text='pay', command = pay, width=20,bg='red',fg='white').place(x=390,y=230)
    
        root.destroy()
        p_pay.mainloop()




    label_4 = Label(str_products, text=res[3][1],width=20,font=("bold", 10))
    label_4.grid(column = 3, row=0)
    b4 = Button(str_products,text=str(res[3][3]) + " USD",command = buy_4, width=20,bg='red',fg='white')
    b4.grid(column = 3, row = 1)

    def buy_5():
        global root, p_pay
        p_pay = Tk()
        p_pay.title("pay")
        p_pay.geometry("1000x600")

        label_credit_card = Label(p_pay, text="Enter Your credit card",width=20,font=("bold", 20))
        label_credit_card.place(x=300,y=53)
        label_name = Label(p_pay, text="credit card",width=20,font=("bold", 10))
        label_name.place(x=290,y=130)
        entry_name = Entry(p_pay)
        entry_name.place(x=450,y=130)
        def pay():
            SQL = "Select * from products_shop"
 
            try:
                config = psycopg2.connect(**params)
                query = config.cursor()
                query.execute(SQL)
                res = query.fetchall()
                query.close()
                config.commit()
                
            except Exception as Error:
                print(str(Error))

            global root, p_check
            p_check = Tk()
            p_check.title("Check")
            p_check.geometry("1000x600")
            # label_1 = Label(p_check, text='check',width=20,font=("bold", 10))
            # label_1.grid(column = 0, row=0)
            credit_card=entry_name.get()
            credit_card=credit_card.replace(' ','')
            # for i in credit_card:
            
            
            
            if re.search('[0-9]{16}',credit_card)[0]==credit_card:
                

                tim=datetime.datetime.now()
                SQL = "INSERT into orders (user_name,product_name,money,date_of_order) values ('" + user_email +"','"+res[4][1]+"','"+str(res[4][3]) +"','" + str(tim) + "')"
                print(SQL)
                try:
                    config = psycopg2.connect(**params)
                    query = config.cursor()
                    query.execute(SQL)
                    query.close()
                    config.commit()
                    
                except Exception as Error:
                    print(str(Error))
                new = int(res[4][2])-1
                if new > 0:
                    SQL = "UPDATE products_shop SET quantity = '" + str(new) +"'  WHERE product_id ='" + str(res[4][0]) +"';"  
                    try:
                        config = psycopg2.connect(**params)
                        query = config.cursor()
                        query.execute(SQL)
                        query.close()
                        config.commit()
                    except Exception as Error:
                        print(str(Error))
                        
                    
            
                    label_1 = Label(p_check, text=f"Shop 1: {res[4][1]} ------------------ '"+str(res[4][3]) +"'   thank you!",width=200,font=("bold", 10))
                    label_1.pack()
                    f= open("check.txt","w+")
                    f.write( user_email+": "+res[4][1]+" ------------------ "+str(res[4][3])+" USD   thank you!")
                    f.close
                    if root.destroy():
                        os.remove("check.txt")
                    root.destroy()
                    p_check.mainloop()
                else:
                    label_1 = Label(p_check, text="There is no that product, Sorry!",width=200,font=("bold", 10))
                    label_1.pack()

            else:
                label_nam = Label(p_pay, text="wrong input",width=20,font=("bold", 10))
                label_nam.place(x=450,y=400)
                p_check.destroy()
                # root.destroy()

        Button(p_pay, text='pay', command = pay, width=20,bg='red',fg='white').place(x=390,y=230)
    
        root.destroy()
        p_pay.mainloop()




    label_5 = Label(str_products, text=res[4][1],width=20,font=("bold", 10))
    label_5.grid(column = 0, row=2)
    b5 = Button(str_products,text=str(res[4][3]) + " USD",command = buy_5, width=20,bg='red',fg='white')
    b5.grid(column = 0, row = 3)

    def buy_6():
        global root, p_pay
        p_pay = Tk()
        p_pay.title("pay")
        p_pay.geometry("1000x600")

        label_credit_card = Label(p_pay, text="Enter Your credit card",width=20,font=("bold", 20))
        label_credit_card.place(x=300,y=53)
        label_name = Label(p_pay, text="credit card",width=20,font=("bold", 10))
        label_name.place(x=290,y=130)
        entry_name = Entry(p_pay)
        entry_name.place(x=450,y=130)
        def pay():
            SQL = "Select * from products_shop"
 
            try:
                config = psycopg2.connect(**params)
                query = config.cursor()
                query.execute(SQL)
                res = query.fetchall()
                query.close()
                config.commit()
                
            except Exception as Error:
                print(str(Error))

            global root, p_check
            p_check = Tk()
            p_check.title("Check")
            p_check.geometry("1000x600")
            # label_1 = Label(p_check, text='check',width=20,font=("bold", 10))
            # label_1.grid(column = 0, row=0)
            credit_card=entry_name.get()
            credit_card=credit_card.replace(' ','')
            # for i in credit_card:
            
            
            
            if re.search('[0-9]{16}',credit_card)[0]==credit_card:
                

                tim=datetime.datetime.now()
                SQL = "INSERT into orders (user_name,product_name,money,date_of_order) values ('" + user_email +"','"+res[5][1]+"','"+str(res[5][3]) +"','" + str(tim) + "')"
                print(SQL)
                try:
                    config = psycopg2.connect(**params)
                    query = config.cursor()
                    query.execute(SQL)
                    query.close()
                    config.commit()
                    
                except Exception as Error:
                    print(str(Error))
                new = int(res[5][2])-1
                if new > 0:
                    SQL = "UPDATE products_shop SET quantity = '" + str(new) +"'  WHERE product_id ='" + str(res[5][0]) +"';"  
                    try:
                        config = psycopg2.connect(**params)
                        query = config.cursor()
                        query.execute(SQL)
                        query.close()
                        config.commit()
                    except Exception as Error:
                        print(str(Error))
                        
                    
            
                    label_1 = Label(p_check, text=f"Shop 1: {res[5][1]} ------------------ '"+str(res[5][3]) +"'   thank you!",width=200,font=("bold", 10))
                    label_1.pack()
                    f= open("check.txt","w+")
                    f.write( user_email+": "+res[5][1]+" ------------------ "+str(res[5][3])+" USD   thank you!")
                    f.close
                    if root.destroy():
                        os.remove("check.txt")
                    root.destroy()
                    p_check.mainloop()
                else:
                    label_1 = Label(p_check, text="There is no that product, Sorry!",width=200,font=("bold", 10))
                    label_1.pack()

            else:
                label_nam = Label(p_pay, text="wrong input",width=20,font=("bold", 10))
                label_nam.place(x=450,y=400)
                p_check.destroy()
                # root.destroy()

        Button(p_pay, text='pay', command = pay, width=20,bg='red',fg='white').place(x=390,y=230)
    
        root.destroy()
        p_pay.mainloop()




    label_6 = Label(str_products, text=res[5][1],width=20,font=("bold", 10))
    label_6.grid(column = 1, row=2)
    b6 = Button(str_products,text=str(res[5][3]) + " USD",command = buy_6, width=20,bg='red',fg='white')
    b6.grid(column = 1, row = 3)

    def buy_7():
        global root, p_pay
        p_pay = Tk()
        p_pay.title("pay")
        p_pay.geometry("1000x600")

        label_credit_card = Label(p_pay, text="Enter Your credit card",width=20,font=("bold", 20))
        label_credit_card.place(x=300,y=53)
        label_name = Label(p_pay, text="credit card",width=20,font=("bold", 10))
        label_name.place(x=290,y=130)
        entry_name = Entry(p_pay)
        entry_name.place(x=450,y=130)
        def pay():
            SQL = "Select * from products_shop"
 
            try:
                config = psycopg2.connect(**params)
                query = config.cursor()
                query.execute(SQL)
                res = query.fetchall()
                query.close()
                config.commit()
                
            except Exception as Error:
                print(str(Error))

            global root, p_check
            p_check = Tk()
            p_check.title("Check")
            p_check.geometry("1000x600")
            # label_1 = Label(p_check, text='check',width=20,font=("bold", 10))
            # label_1.grid(column = 0, row=0)
            credit_card=entry_name.get()
            credit_card=credit_card.replace(' ','')
            # for i in credit_card:
            
            
            
            if re.search('[0-9]{16}',credit_card)[0]==credit_card:
                

                tim=datetime.datetime.now()
                SQL = "INSERT into orders (user_name,product_name,money,date_of_order) values ('" + user_email +"','"+res[6][1]+"','"+str(res[6][3]) +"','" + str(tim) + "')"
                print(SQL)
                try:
                    config = psycopg2.connect(**params)
                    query = config.cursor()
                    query.execute(SQL)
                    query.close()
                    config.commit()
                    
                except Exception as Error:
                    print(str(Error))
                new = int(res[6][2])-1
                if new > 0:
                    SQL = "UPDATE products_shop SET quantity = '" + str(new) +"'  WHERE product_id ='" + str(res[6][0]) +"';"  
                    try:
                        config = psycopg2.connect(**params)
                        query = config.cursor()
                        query.execute(SQL)
                        query.close()
                        config.commit()
                    except Exception as Error:
                        print(str(Error))
                        
                    
            
                    label_1 = Label(p_check, text=f"Shop 1: {res[6][1]} ------------------ '"+str(res[6][3]) +"'   thank you!",width=200,font=("bold", 10))
                    label_1.pack()
                    f= open("check.txt","w+")
                    f.write( user_email+": "+res[6][1]+" ------------------ "+str(res[6][3])+" USD   thank you!")
                    f.close
                    if root.destroy():
                        os.remove("check.txt")
                    root.destroy()
                    p_check.mainloop()
                else:
                    label_1 = Label(p_check, text="There is no that product, Sorry!",width=200,font=("bold", 10))
                    label_1.pack()

            else:
                label_nam = Label(p_pay, text="wrong input",width=20,font=("bold", 10))
                label_nam.place(x=450,y=400)
                p_check.destroy()
                # root.destroy()

        Button(p_pay, text='pay', command = pay, width=20,bg='red',fg='white').place(x=390,y=230)
    
        root.destroy()
        p_pay.mainloop()




    label_7 = Label(str_products, text=res[6][1],width=20,font=("bold", 10))
    label_7.grid(column = 2, row=2)
    b7 = Button(str_products,text=str(res[6][3]) + " USD",command = buy_7, width=20,bg='red',fg='white')
    b7.grid(column = 2, row = 3)

    def buy_8():
        global root, p_pay
        p_pay = Tk()
        p_pay.title("pay")
        p_pay.geometry("1000x600")

        label_credit_card = Label(p_pay, text="Enter Your credit card",width=20,font=("bold", 20))
        label_credit_card.place(x=300,y=53)
        label_name = Label(p_pay, text="credit card",width=20,font=("bold", 10))
        label_name.place(x=290,y=130)
        entry_name = Entry(p_pay)
        entry_name.place(x=450,y=130)
        def pay():
            SQL = "Select * from products_shop"
 
            try:
                config = psycopg2.connect(**params)
                query = config.cursor()
                query.execute(SQL)
                res = query.fetchall()
                query.close()
                config.commit()
                
            except Exception as Error:
                print(str(Error))

            global root, p_check
            p_check = Tk()
            p_check.title("Check")
            p_check.geometry("1000x600")
            # label_1 = Label(p_check, text='check',width=20,font=("bold", 10))
            # label_1.grid(column = 0, row=0)
            credit_card=entry_name.get()
            credit_card=credit_card.replace(' ','')
            # for i in credit_card:
            
            
            
            if re.search('[0-9]{16}',credit_card)[0]==credit_card:
                

                tim=datetime.datetime.now()
                SQL = "INSERT into orders (user_name,product_name,money,date_of_order) values ('" + user_email +"','"+res[7][1]+"','"+str(res[7][3]) +"','" + str(tim) + "')"
                print(SQL)
                try:
                    config = psycopg2.connect(**params)
                    query = config.cursor()
                    query.execute(SQL)
                    query.close()
                    config.commit()
                    
                except Exception as Error:
                    print(str(Error))
                new = int(res[7][2])-1
                if new > 0:
                    SQL = "UPDATE products_shop SET quantity = '" + str(new) +"'  WHERE product_id ='" + str(res[7][0]) +"';"  
                    try:
                        config = psycopg2.connect(**params)
                        query = config.cursor()
                        query.execute(SQL)
                        query.close()
                        config.commit()
                    except Exception as Error:
                        print(str(Error))
                        
                    
            
                    label_1 = Label(p_check, text=f"Shop 1: {res[7][1]} ------------------ '"+str(res[7][3]) +"'   thank you!",width=200,font=("bold", 10))
                    label_1.pack()
                    f= open("check.txt","w+")
                    f.write( user_email+": "+res[7][1]+" ------------------ "+str(res[7][3])+" USD   thank you!")
                    f.close
                    if root.destroy():
                        os.remove("check.txt")
                    root.destroy()
                    p_check.mainloop()
                else:
                    label_1 = Label(p_check, text="There is no that product, Sorry!",width=200,font=("bold", 10))
                    label_1.pack()

            else:
                label_nam = Label(p_pay, text="wrong input",width=20,font=("bold", 10))
                label_nam.place(x=450,y=400)
                p_check.destroy()
                # root.destroy()

        Button(p_pay, text='pay', command = pay, width=20,bg='red',fg='white').place(x=390,y=230)
    
        root.destroy()
        p_pay.mainloop()




    label_8 = Label(str_products, text=res[7][1],width=20,font=("bold", 10))
    label_8.grid(column = 3, row=2)
    b8 = Button(str_products,text=str(res[7][3]) + " USD",command = buy_8, width=20,bg='red',fg='white')
    b8.grid(column = 3, row = 3)



    


    str_products.mainloop()
Window()