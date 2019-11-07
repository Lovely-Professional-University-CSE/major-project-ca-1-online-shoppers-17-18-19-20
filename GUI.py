import tkinter as tk
from tkinter import *
import random
import os

print("re")
r = Tk()
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
    btnl = Button(r, text='Perceptron Model', width=20, font=('times new roman', 20, 'bold'), bg='lavender', command=training_window)
    btnl.place(x=100, y=300)
    btnl = Button(r, text='SOM Model', width=30, font=('times new roman', 20, 'bold'), bg='lavender')
    btnl.place(x=0, y=400)


btnl = Button(r, text='Perceptron Model', width=30, font=('times new roman', 20, 'bold'), bg='brown', command=training_window)
btnl.place(x=900, y=500)
btnl = Button(r, text='SOM Model', width=30, font=('times new roman', 20, 'bold'), bg='brown',command=training_window)
btnl.place(x=0, y=500)
btnl = Button(r, text='SVM Model', width=30, font=('times new roman', 20, 'bold'), bg='brown',command=training_window)
btnl.place(x=0, y=300)
btnl = Button(r, text='LVQ Model', width=30, font=('times new roman', 20, 'bold'), bg='brown',command=training_window)
btnl.place(x=900, y=300)
r.mainloop()