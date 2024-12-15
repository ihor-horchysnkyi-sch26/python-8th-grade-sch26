from tkinter import *
from tkinter.messagebox import *
def click (event):
    root.title('Я змінюю значення властивостей вікна')
    root['bg']='yellow'
    h=root.winfo_height()+150
    root.geometry('400x{}'.format(h))
    showinfo('Подія', 'Відкрите вікно повідомлень!')
root=Tk()
root.bind('<1>', click)
