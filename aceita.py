import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox



root = tk.Tk()
root.title('DESENVOLVIDO POR DENI!')
root.geometry('600x600')
root.configure(background='#000000')

def move_button_1():   
     #if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(10, root.winfo_width() - button_1.winfo_width())
        y = random.randint(10, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

def move_button_2(e):
 if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
    x = random.randint(10, root.winfo_width() - button_2.winfo_width())
    y = random.randint(10, root.winfo_height() - button_2.winfo_height())
    button_2.place(x=x, y=y)

def accepted():
   # move_button_1()
    messagebox.showinfo('CUIDA', 'CHEGO JÁ AI BLZ?')

def denied():
    move_button_1()
    
margin = Canvas(root, width=500, bg='#000000', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()

text_id = Label(root, bg='#000000', text='VAMOS TOMAR UMA?', fg='#00FF00', font=('Montserrat', 35, 'bold'))
text_id.pack()

#root.bind('<Motion>', move_button_1)

button_1 = tk.Button(root, text='TO AFIM NÃO', bg='#FF00FF', command=denied, relief=RIDGE, bd=5, font=('Montserrat', 14, 'bold'))
button_1.pack()

root.bind('<Motion>', move_button_1)

button_2 = tk.Button(root, text='CHAMAAA', bg='#FF00FF', relief=RIDGE, bd=5, command=accepted, font=('Montserrat', 14, 'bold'))
button_2.pack()


root.mainloop()

