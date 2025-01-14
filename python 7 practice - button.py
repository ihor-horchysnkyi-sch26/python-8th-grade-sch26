from tkinter import *

def label_click (event):
    button['text'] = 'В мене все вийшло!'
    button['font'] = ("Arial", 30)
    button['fg'] = 'green'

root = Tk()
root.title = 'Проект з кнопками та написами'
root.geometry('500x300')

button = Button(text = 'Кнопка з написом', width=40)
button['fg'] = 'yellow'
button['bg'] = 'blue'
button['font'] = ("Arial", 20)
button.bind('<1>', label_click)
button.place(x = 75, y = 10)
