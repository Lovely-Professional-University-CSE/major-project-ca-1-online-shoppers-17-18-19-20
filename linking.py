
import tkinter as tk
from tkinter import*
import random
import time
import sqlite3
from tkinter import messagebox
r= Tk()
#======================================
r.title('Non Regular Registration Form')
r.geometry('1350x750+0+0')
r.config(bg='brown')
background_imag = PhotoImage(file="back1.png")
backgrounda = Label(r, image=background_imag, bd=0)
backgrounda.pack()
top=Frame(r,width=1300,height=50,bg='brown',relief=SUNKEN)
top.pack(side=TOP)
f1=Frame(r,width=800,height=700,bg='brown',relief=SUNKEN,padx=10)
f1.pack(side=LEFT)
f2=Frame(r,width=600,height=700,bg='brown',relief='ridge',padx=100)
f2.pack(side=RIGHT)
l=Label(r,font=('cooper',30,'bold'),text='Prediction On Online Shoppers Purchasing Dataset',fg='brown',bd=10,anchor='w')
l.place(x=200,y=10)

embed=Frame(r,width=600,height=400)
embed.place(x=8,y=200)
l1=Label(embed,font=('times new roman',18,'bold'),text='In this we have preformed classification',fg='black',bd=10,anchor='w')
l1.place(x=50,y=10)
l2=Label(embed,font=('times new roman',18,'bold'),text='and the intention of the Online Customers',fg='black',bd=10,anchor='w')
l2.place(x=2,y=50)
l2=Label(embed,font=('times new roman',18,'bold'),text='The data set was formed so that each',fg='black',bd=10,anchor='w')
l2.place(x=2,y=90)
l2=Label(embed,font=('times new roman',18,'bold'),text='session would belong to a different  user',fg='black',bd=10,anchor='w')
l2.place(x=2,y=130)
l2=Label(embed,font=('times new roman',18,'bold'),text='in a 1-year period to avoid any',fg='black',bd=10,anchor='w')
l2.place(x=2,y=170)
l2=Label(embed,font=('times new roman',18,'bold'),text='tendency to a specific campaign,',fg='black',bd=10,anchor='w')
l2.place(x=2,y=210)
l2=Label(embed,font=('times new roman',18,'bold'),text=' special day, user profile, or period. ',fg='black',bd=10,anchor='w')
l2.place(x=2,y=250)
l2=Label(embed,font=('times new roman',18,'bold'),text='which is Collected from UCI',fg='black',bd=10,anchor='w')
l2.place(x=2,y=290)
l2=Label(embed,font=('times new roman',18,'bold'),text='For more information of this Click below...  ',fg='black',bd=10,anchor='w')
l2.place(x=2,y=300)

import webbrowser
new = 1
url = "https://en.wikipedia.org/wiki/Online_shopping#Growth_in_online_shoppers"

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(embed, text = "Click here",width=15,font=('arial',15,'bold'),bg='brown',command=openweb)
Btn.place(x=190,y=330)
embed1=Frame(r,width=500,height=400)
embed1.place(x=800,y=210)

background_imag1 = PhotoImage(file="back4.png")
backgrounda1 = Label(embed1, image=background_imag1, bd=0)
backgrounda1.pack()
#import tkinter as tk
#from tkinter import *
#import random
#import os

#print("re")
def sudha():
    r = Toplevel()
    r.title('DATA PREDICTION')
    r.geometry('1350x750+0+0')
    background_imag = PhotoImage(file="back1.png")
    backgrounda = Label(r, image=background_imag, bd=0)
    backgrounda.pack()
    l = Label(r, font=('arial', 25, 'bold'), text='Prediction Models on', fg='black', bd=10, anchor='w', bg='violet')
    l.place(x=500, y=10)
    l = Label(r, font=('arial', 25, 'bold'), text='online shopperspurchasing Dataset', fg='black', bd=10, anchor='w',
              bg='violet')
    l.place(x=430, y=80)

    def training_window():
        newWindowx = Toplevel()
        newWindowx.config(bg='grey')
        newWindowx.geometry('1350x750')
        newWindowx.config(bg='#3D0C02')
        frame = Frame(newWindowx)
        frame.config(bg='#800080')
        frame.pack()
        with open("model_pickle", "rb") as f:
            mp = pickle.load(f)
        mp.process()
        btnl = Button(r, text='Perceptron Model', width=20, font=('times new roman', 20, 'bold'), bg='lavender',
                      command=training_window)
        btnl.place(x=100, y=300)
        btnl = Button(r, text='SOM Model', width=30, font=('times new roman', 20, 'bold'), bg='lavender')
        btnl.place(x=0, y=400)

    btnl = Button(r, text='Perceptron Model', width=30, font=('times new roman', 20, 'bold'), bg='brown',
                  command=training_window)
    btnl.place(x=0, y=300)
    btnl = Button(r, text='SOM Model', width=30, font=('times new roman', 20, 'bold'), bg='brown',
                  command=training_window)
    btnl.place(x=0, y=400)
    btnl = Button(r, text='SVM Model', width=30, font=('times new roman', 20, 'bold'), bg='brown',
                  command=training_window)
    btnl.place(x=0, y=500)
    btnl = Button(r, text='LVQ Model', width=30, font=('times new roman', 20, 'bold'), bg='brown',
                  command=training_window)
    btnl.place(x=0, y=600)

    # Btn = Button(embed2, text = "GO",width=15,font=('arial',15,'bold'),bg='orange',relief='ridge',command=model)
    # Btn.place(x=160,y=50)
    r.mainloop()


embed2=Frame(r,width=500,height=100)
embed2.place(x=800,y=500)
l2=Label(embed2,font=('arial',18,'bold'),text='Click to Go to the data training Models',fg='black',bd=10,anchor='w')
l2.place(x=4,y=5)
Btn = Button(embed2, text = "GO",width=15,font=('arial',15,'bold'),bg='orange',relief='ridge',command=sudha)
Btn.place(x=160,y=50)
r.mainloop()

