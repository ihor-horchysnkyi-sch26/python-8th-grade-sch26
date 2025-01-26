from tkinter import*
from tkinter import filedialog as fd
from tkinter import messagebox
def loadText():
    file_name = fd.askopenfilename()
    f = open(file_name)
    text.insert(1.0, f.read())
    f.close()
def count_C():
    c = entry.get()
    k = text.get(1.0, END).count(c)
    messagebox.showinfo('Відповідь', 'k = '+str(k))
root=Tk()
root.title('Аналіз тексту')
text=Text(width='30', heigh='10')
text.grid(row = 0, column = 0, columnspan = 2, padx = 8, pady = 8)
b_open = Button(root, text = 'Відкрити', command=loadText)
b_open.grid(row = 1, column = 0, columnspan = 2, pady = 8)
lab1 = Label(root, text = 'Уведіть символ')
lab1.grid(row = 2, column = 0)
entry = Entry(width = 8)
entry.grid(row = 2, column = 1, pady = 8)
b_count = Button(root, text = 'Підрахувати', command=count_C)
b_count.grid(row = 3, column = 0, columnspan = 2, pady = 8)

root.mainloop()
