from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title='This is an info message me', message='You are a person')
    #messagebox.showwarning(title='WARNING!', message='You have a virus!!!')
    if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
        print('you did a thing!')
    else:
        print('You canceled a thing')

window = Tk()

button = Button(window,
                command=click,
                text='click me')
button.pack()


window.mainloop()
