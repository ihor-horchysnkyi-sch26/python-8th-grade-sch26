from tkinter import *

def click (event):
    root['bg'] = 'yellow'
    root.title('Змінення значень властивості вікна')
    root.geometry('400x200+500+70')
    print('Подія клік')
    
root = Tk()
root.bind('<1>', click)
root['bg'] = 'green'
root.title('Тестове вікно')
root.geometry('100x100+500+70')
print('Ініціалізація вікна завершена')
    
