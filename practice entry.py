from tkinter import *

def calc():
    a = float(entry_a.get())
    b = float(entry_b.get())
    sum = a*(4*b-a)
    entry_res.insert(0, sum)

root = Tk()
root.geometry("500x450")

label_a = Label();
label_a['text'] = 'Variable a:'
label_a.pack(pady = 20)

entry_a = Entry()
entry_a.pack()

label_b = Label();
label_b['text'] = 'Variable b:'
label_b.pack(pady = 20)

entry_b = Entry()
entry_b.pack()

button = Button(command = calc)
button['text'] = '='
button['font'] = 20
button.pack(pady = 30)

label_res = Label();
label_res['text'] = 'Result:'
label_res.pack(pady = 20)

entry_res = Entry()
entry_res.pack()
