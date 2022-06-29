# importing only those functions which are needed
from tkinter import *

#label = an area widget that

window = Tk()

photo = PhotoImage(file='logo.png')

label = Label(window, text="Welcome to Bluebird Aviation ",
              font=("Arial", 40, "bold"),
              fg='#00FF00',
              bg="black",
              relief=RAISED,
              bd=10,
              padx= 20,
              pady=20,
              image=photo,
              compound='bottom')
#label.place(x=100, y=100)
label.pack()

window.mainloop()
