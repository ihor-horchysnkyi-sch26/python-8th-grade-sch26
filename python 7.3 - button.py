from tkinter import *

def label_click (event):
    button['text'] = 'Я навчаюсь у 8 класі'
    button['font'] = 14
    button['fg'] = 'red'
    button['bg'] = 'yellow'

root = Tk()
root.geometry('300x200')

button = Button(text = 'Це напис')
button.bind('<1>', label_click)
button.place(x = 75, y = 10)
