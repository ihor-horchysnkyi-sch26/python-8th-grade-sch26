from tkinter import *
def click(event):
    root['bg'] = 'yellow'
root = Tk()
root.geometry('300x200+350+200')
button = Button(text='Змінити', width='15')
button.pack(pady=30)
button.bind('<1>', click)
