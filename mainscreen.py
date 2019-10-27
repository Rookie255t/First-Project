from tkinter import *

def A():
    mainscreen = Tk()
    mainscreen.title("New window")
    mainscreen.geometry("200x200")
    E = Label(mainscreen, text = "New window")
    E.pack()

mainscreen = Tk()
mainscreen.title("Main Screen")
mainscreen.geometry("200x200")

OkBtn = Button(mainscreen, text = "Okay", command = A)
OkBtn.pack()

mainscreen.mainloop()
