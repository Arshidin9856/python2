import tkinter
import psycopg2

conn = psycopg2.connect(
  host="localhost",
  database="pp2demo",
  user="pp2demo_user",
  password="pp2demo")

cursor = conn.cursor()
sql1='select * from users1;'
# sql1='CREATE TABLE users1 (name VARCHAR(255), user_name VARCHAR(255));'
# cursor.execute("create table users1(Name varchar(255),Password varchar(255));")
cursor.execute(sql1)
users = cursor.fetchall()
print(users)
b=True
window=tkinter.Tk()


E2=tkinter.Entry(window)
E2.pack(side='bottom')    

E1=tkinter.Entry(window)
E1.pack(side='bottom')

def getlogin():
    global b
    log=E1.get()
    pasw=E2.get()
    for u,s in  users:
        if u == log :
            root=tkinter.Tk()
            widget=tkinter.Label(root,text="user alredy exist").pack(side="bottom")
            b=False
    if b:
        sql = f"insert into users1(Name,Password) values ('{log}',{pasw});"
        cursor.execute(sql)
        conn.commit()
        root1=tkinter.Tk()
        widget=tkinter.Label(root1,text="You are welcome!").pack(side="bottom")

Log=tkinter.Button(window,text='enter',command=getlogin).pack(side="bottom")

window.mainloop()
conn.commit() 
cursor.close()
conn.close()