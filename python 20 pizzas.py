from tkinter import *
def btn_click():
    suma = var.get()*(60+cvar1.get()*8+cvar2.get()*18
			 	    +cvar3.get()*39)
    lab2.config(text = 'Вартість: ' +str(suma)+ ' грн')
root = Tk()
root.title('Конструктор піц')
var = IntVar()
var.set(2)
Radiobutton(text = 'Великий корж', variable = var, value = 2).pack(anchor = W)
Radiobutton(text = 'Середній корж', variable = var, value = 1).pack(anchor = W)
Button(root, text = 'Замовити', command = btn_click).pack(pady = 10)

Label(root, text = 'Виберіть складники', width = 20, anchor = W).pack(pady = 10)
cvar1 = BooleanVar()
cvar1.set(0)
c1 = Checkbutton(text = 'Цибуля', variable = cvar1, onvalue = 1, offvalue = 0)
c1.pack(anchor = W)
cvar2 = BooleanVar()
cvar2.set(0)
c2 = Checkbutton(text = 'Моцарела', variable = cvar2, onvalue = 1, offvalue = 0)
c2.pack(anchor = W)
cvar3 = BooleanVar()
cvar3.set(0)
c3 = Checkbutton(text = 'Бекон', variable = cvar3, onvalue = 1, offvalue = 0)
c3.pack(anchor = W)

lab2 = Label(root, text = 'Вартість: ', width = 20, anchor = W)
lab2.pack(padx = 5, pady = 10)
