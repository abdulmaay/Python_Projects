# importing only those functions which are needed
from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("First GUI project")

icon = PhotoImage(file='ETS_LOGO.png')
window.iconphoto(True, icon)
window.config(background="#5cfcff")

window.mainloop()

