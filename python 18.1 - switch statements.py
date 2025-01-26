from tkinter import*
from tkinter import messagebox as mb
from math import*
def btn_click():
    a, b, c = map(float, [enA.get(), enB.get(), enC.get()])
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + sqrt(discr)) / (2 * a)
        x2 = (-b - sqrt(discr)) / (2 * a)
        s = 'x1 =' + str(round(x1, 2)) + ' x2 = ' + str(round(x2, 2))
        mb.showinfo('Два корені', s)
    elif discr == 0:
        x = -b / (2 * a)
        s = 'x =' + str(round(x, 2))
        mb.showinfo('Один корінь', s)
    else:
        mb.showinfo('Не має коренів', "Рівняння розв'язків не має")
root=Tk()
root.title('Квадратне рівняння')
labA = Label(root, text = 'A')
labA.grid(row = 0, column = 0)
enA = Entry(width = 8)
enA.grid(row = 1, column = 0, pady = 8, padx = 8)
labB = Label(root, text = 'B')
labB.grid(row = 0, column = 1)
enB = Entry(width = 8)
enB.grid(row = 1, column = 1, pady = 8, padx = 8)
labC = Label(root, text = 'C')
labC.grid(row = 0, column = 2)
enC = Entry(width = 8)
enC.grid(row = 1, column = 2, pady = 8, padx = 8)
btn = Button(root, text = 'Знайти корені', command=btn_click)
btn.grid(row = 2, column = 0, columnspan = 3, pady = 8)

root.mainloop()
