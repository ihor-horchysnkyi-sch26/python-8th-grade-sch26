from tkinter import*
from tkinter import ttk
from random import*

def btn1_click():
    s = combo1.get()+' '+combo2.get()+' '+combo3.get()
    phraze.delete(0, END)
    phraze.insert(0, s)

def btn1_click_2():
    s = c1[combo1.get()] + ' ' + c3[combo3.get()] + ' ' + c2[combo2.get()]
    phraze.delete(0, END)
    phraze.insert(0, s)

def btn1_click_3():
    combo1.current(randint(0, 3))
    combo2.current(randint(0, 3))
    combo3.current(randint(0, 3))

root=Tk()
root.title('Перекладач')

c1 = {'Собака': 'A dog', 'Кінь': 'A horse', 'Пташка': 'A bird', 'Сонце': 'The Sun'}
c2 = {'голосно': 'loudly', 'швидко': 'fast', 'високо': 'high', 'яскраво': 'brightly'}
c3 = {'гавкає': 'barks', 'бігає': 'runs', 'літає': 'flies', 'сяє': 'shines'}
key1 = list(c1.keys())
key2 = list(c2.keys())
key3 = list(c3.keys())

combo1 = ttk.Combobox(root, width = 10, values = key1)
combo1.current(0)
combo1.grid(row = 0, column = 0, padx=5, pady=5)


combo2 = ttk.Combobox(root, width = 10, values = key2)
combo2.current(0)
combo2.grid(row = 0, column = 1, padx=5, pady=5)

combo3 = ttk.Combobox(root, width = 10, values = key3)
combo3.current(0)
combo3.grid(row = 0, column = 2, padx=5, pady=5)

phraze = Entry(text = '', width = 45)
phraze.grid(row = 1, column = 0, columnspan = 3, pady=5)

btn1 = Button(text = 'Скласти фразу', width = 20, command=btn1_click)
btn1.grid(row = 2, column = 0, columnspan = 3, pady=5)
btn2 = Button(text = 'Зробити переклад', width = 20, command=btn1_click_2)
btn2.grid(row = 3, column = 0, columnspan = 3, pady=5)
btn3 = Button(text = 'Задати випадковий вибір', width = 20, command=btn1_click_3)
btn3.grid(row = 4, column = 0, columnspan = 3, pady=5)

root.mainloop()
