from tkinter import *
def click (event):
    t=root.winfo_y()+50
    w=root.winfo_width()+40
    root.geometry('{}x320+200+{}'.format(w,t))
root = Tk()
root.geometry('480x320+200+200')
root.bind('<1>', click)
