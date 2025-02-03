from tkinter import *

def click():
    temperature = float(entry.get())
    if temperature < 0:
        state['text'] ='Поточний стан: Лід'
    elif (temperature < 100 and temperature >=0):
        state['text'] ='Поточний стан: Вода'
    else:
        state['text'] ='Поточний стан: Пар'
        

root = Tk()
root.geometry("300x250")

label = Label(text = 'T води:')
label.pack()

entry = Entry()
entry.pack(pady = 20)
entry.focus_set()

button = Button(text = 'Визначити стан', command = click)
button.pack(pady = 10)

state = Label(text = 'Поточний стан: ?')
state.pack(pady = 20)




root.mainloop()
