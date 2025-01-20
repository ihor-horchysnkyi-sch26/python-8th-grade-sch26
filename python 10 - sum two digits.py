from tkinter import *

def twoDigitsSum():
    x = float(entry1.get())
    y = float(entry2.get())
    z = x+y
    label['text'] = str(z)

root = Tk()
root.geometry("300x250")
entry1 = Entry()
entry1. pack(pady = 10)
entry2 = Entry()
entry2.pack(pady = 10)

label = Label()
label.pack(pady = 10)

button = Button(text = 'Сума', command=twoDigitsSum)
button.pack(pady = 10)
