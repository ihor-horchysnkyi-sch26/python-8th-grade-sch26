from tkinter import*
from random import*
import time 
tk = Tk()
canvas = Canvas(tk, width = 400, height = 400)  
canvas.pack()
x = randint(10, 350) # Задання випадкових початкових координат
y = randint(10, 350)  
id = canvas.create_oval(x, y, x+50, y+50, fill = 'red')
				# Створення об’єкта
dx = randint(2, 5)
dy = randint(2, 5)               # Задання кроку руху
while True:         # Організація нескінченного циклу
    if x>350 or x<10: dx = -dx  # Якщо об’єкт досягає меж полотна,
    if y>350 or y<10: dy = -dy  # напрямок руху змінюється 
         				       # на протилежний
    x = x+dx       			# Обчислення нових координат об’єкта
    y = y+dy
    canvas.move(id, dx, dy)	# Переміщення об’єкта в точку 
         				# з новими координатами
    tk.update()       		# Оновлення полотна
    time.sleep(0.05)      # Затримка виконання програми на 0,05 с
