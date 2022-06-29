from tkinter import *
# button = you click it, then it does stuff

count = 0

def click():
    global count
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file='like.png')





button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='top')
button.pack()
window.mainloop()
