from tkinter import *

def submit():
    print("The tempreture is: " + str(scale.get())+ " degrees C")
window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length = 600,
              orient=VERTICAL,
              font=('Consolas', 20),
              tickinterval = 10,
              showvalue = 0)
scale.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()
