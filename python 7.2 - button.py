from tkinter import *

def label_click (event):
    label['text'] = 'Я навчаюсь у 8 класі'
    label['font'] = 14
    label['fg'] = 'red'
    label['bg'] = 'yellow'

root = Tk()
root.geometry('300x200')

label = Label(text = 'Це напис')
label.bind('<1>', label_click)
label.place(x = 75, y = 10)
