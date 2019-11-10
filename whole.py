
import tkinter as tk
from tkinter import*
r= Tk()
#======================================
r.title('main page')
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
embed=Frame(r,width=600,height=400,bg='black')
embed.place(x=8,y=200)
l1=Label(embed,font=('times new roman',18,'bold'),text='In this we have preformed classification',fg='white',bg='black',bd=10,anchor='w')
l1.place(x=50,y=10)
l2=Label(embed,font=('times new roman',18,'bold'),text='and the intention of the Online Customers',fg='white',bg='black',bd=10,anchor='w')
l2.place(x=2,y=50)
l2=Label(embed,font=('times new roman',18,'bold'),text='The data set was formed so that each',fg='white',bg='black',bd=10,anchor='w')
l2.place(x=2,y=90)
l2=Label(embed,font=('times new roman',18,'bold'),text='session would belong to a different  user',fg='white',bg='black',bd=10,anchor='w')
l2.place(x=2,y=130)
l2=Label(embed,font=('times new roman',18,'bold'),text='in a 1-year period to avoid any',fg='white',bg='black',bd=10,anchor='w')
l2.place(x=2,y=170)
l2=Label(embed,font=('times new roman',18,'bold'),text='tendency to a specific campaign,',fg='white',bg='black',bd=10,anchor='w')
l2.place(x=2,y=210)
l2=Label(embed,font=('times new roman',18,'bold'),text=' special day, user profile, or period. ',fg='white',bg='black',bd=10,anchor='w')
l2.place(x=2,y=250)
l2=Label(embed,font=('times new roman',18,'bold'),text='which is Collected from UCI',fg='white',bd=10,bg='black',anchor='w')
l2.place(x=2,y=290)
l2=Label(embed,font=('times new roman',18,'bold'),text='For more information of this Click below...  ',fg='white',bg='black',bd=10,anchor='w')
l2.place(x=2,y=300)

import webbrowser
new = 1
url = ""

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
def sudha1():
    pw = Toplevel()
    pw.title("Perceptron")
    pw.geometry('1360x850+0+0')
    background_imag2 = PhotoImage(file="jp.png")
    backgrounda = Label(pw, image=background_imag2, bd=0)
    backgrounda.pack()

    def back():
        pw.destroy()
    l = Label(pw, font=('Goudy Stout', 25, 'bold italic'), text='Perceptron Model', fg='white', bd=10, anchor='w',
              bg='black')
    l.place(x=400, y=30)
    f1 = Frame(pw, width=700, height=500, relief='sunken', bg='black')
    f1.place(x=100, y=120)
    background_imag3 = PhotoImage(file="bs.png")
    backgroundai = Label(f1, image=background_imag3, bd=0)
    backgroundai.pack()
    f2 = Frame(pw,width=340, height=60, relief='sunken', bg='black')
    f2.place(x=800, y=300)
    f3 = Frame(pw, width=280, height=60, relief='sunken', bg='black')
    f3.place(x=800, y=600)

    import webbrowser
    new = 1
    url = "https://github.com/Lovely-Professional-University-CSE/major-project-ca-1-online-shoppers-17-18-19-20/blob/master/Perceptron_Model.ipynb"

    def openweb():
        webbrowser.open(url, new=new)

    Btn = Button(f2, text="Click here for code of perceptron", width=0, font=('arial', 15, 'bold'), bg='white', command=openweb)
    Btn.place(x=0, y=8)
    b1 = Button(f3, text="back", command=back, font=('arial', 15), fg="black", bg='white', bd=4).pack(side=LEFT)
    pw.mainloop()
    # Btn = Button(embed2, text = "GO",width=15,font=('arial',15,'bold'),bg='orange',relief='ridge',command=model)
    # Btn.place(x=160,y=50)
    pw.mainloop()
    
    
def bharath():
    pw = Toplevel()
    pw.title("LVQ")
    pw.geometry('1360x850+0+0')
    #background_imag2 = PhotoImage(file="jp.png")
    #backgrounda = Label(pw, image=background_imag2, bd=0)
    #backgrounda.pack()

    def back():
        pw.destroy()
    l = Label(pw, font=('Goudy Stout', 25, 'bold italic'), text='LVQ', fg='white', bd=10, anchor='w',
              bg='black')
    l.place(x=400, y=30)
    f1 = Frame(pw, width=700, height=500, relief='sunken', bg='black')
    f1.place(x=100, y=120)
    #background_imag3 = PhotoImage(file="bs.png")
    #backgroundai = Label(f1, image=background_imag3, bd=0)
    #backgroundai.pack()
    f2 = Frame(pw,width=340, height=60, relief='sunken', bg='black')
    f2.place(x=800, y=300)
    f3 = Frame(pw, width=280, height=60, relief='sunken', bg='black')
    f3.place(x=800, y=600)

    import webbrowser
    new = 1
    url = "https://github.com/Lovely-Professional-University-CSE/major-project-ca-1-online-shoppers-17-18-19-20/blob/master/mu.py"

    def openweb():
        webbrowser.open(url, new=new)

    Btn = Button(f2, text="Click here for code of LVQ", width=0, font=('arial', 15, 'bold'), bg='white', command=openweb)
    Btn.place(x=0, y=8)
    b1 = Button(f3, text="back", command=back, font=('arial', 15), fg="black", bg='white', bd=4).pack(side=LEFT)
    pw.mainloop()
    # Btn = Button(embed2, text = "GO",width=15,font=('arial',15,'bold'),bg='orange',relief='ridge',command=model)
    # Btn.place(x=160,y=50)
    pw.mainloop()
    
    
def sudha():
    r = Toplevel()
    r.title('DATA PREDICTION')
    r.geometry('1350x750+0+0')
    background_imag = PhotoImage(file="back3.png")
    backgrounda = Label(r, image=background_imag, bd=0)
    backgrounda.pack()


    l = Label(r, font=('arial', 25, 'bold'), text='Prediction Models on', fg='black', bd=10, anchor='w', bg='white')
    l.place(x=500, y=10)
    l = Label(r, font=('arial', 25, 'bold'), text='online shopperspurchasing Dataset', fg='black', bd=10, anchor='w',
              bg='white')
    l.place(x=430, y=80)
    btnl = Button(r, text='Perceptron Model', width=30, font=('times new roman', 20, 'bold'), bg='white',fg='black',command=sudha1)
    btnl.place(x=0, y=300)
    btnl = Button(r, text='SOM Model', width=30, font=('times new roman', 20, 'bold'), bg='white',fg='black',command=bharath)
    btnl.place(x=0, y=400)
    btnl = Button(r, text='SVM Model', width=30, font=('times new roman', 20, 'bold'), bg='white',fg='black')
    btnl.place(x=0, y=500)
    btnl = Button(r, text='LVQ Model', width=30, font=('times new roman', 20, 'bold'), bg='white',fg='black')
    btnl.place(x=0, y=600)
    def back():
       r.destroy()

    f4 = Frame(r, width=280, height=60, relief='sunken', bg='black')
    f4.place(x=50, y=680)
    btn = Button(f4, text="back", command=back, font=('arial', 15), fg="black", bg='white', bd=4).pack(side=LEFT)

    r.mainloop()


embed2=Frame(r,width=500,height=100)
embed2.place(x=800,y=500)
l2=Label(embed2,font=('arial',18,'bold'),text='Click to Go to the data training Models',fg='black',bd=10,anchor='w')
l2.place(x=4,y=5)
Btn = Button(embed2, text = "GO",width=15,font=('arial',15,'bold'),bg='orange',relief='ridge',command=sudha)
Btn.place(x=160,y=50)


r.mainloop()

