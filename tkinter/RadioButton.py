
from tkinter import *

#radio button = similar to checkbox, but you can only select one from the group

food = ["pizza", "hamburger", "Samosa"]

def order():
    if (x.get() ==0):
        print("You ordered Pizza!")
    elif (x.get() == 1):
        print("You ordered a hamburger!")
    else:
        print("You ordered Samosa!")

window = Tk()

pizza_photo =PhotoImage(file="pizza.png")
ham_photo =PhotoImage(file='ham.png')
sam_photo =PhotoImage(file='sam.png')
food_photo =[pizza_photo, ham_photo, sam_photo]

x = IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                          text=food[index], #adds text to radio buttons
                          variable=x, #groups radiobuttons together if they share the same variable
                          value=index, #assigns each radio button a different value
                          fg='#00ff00',
                          font = ('Impact', 50),
                          padx = 25,
                          image = food_photo[index], # adds image to radio button
                          compound = 'left', #add image & text(left-side)
                          indicatoron = 0, #eliminates circle indicators
                          width =375,
                          command=order)
    radiobutton.pack(anchor=W)

window.mainloop()
