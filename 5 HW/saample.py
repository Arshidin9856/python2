from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys
import tkinter
root = Tk() 
root.title("Calculator")
# root.configure(background = 'grey')
root.resizable(width=False, height=False)
# root.geometry("550x150+450+90")
main=tkinter.Entry(root,width=50)
main.grid(row=0,column=0)
root.mainloop()