""" Intro to GUI - task 2
Exercise 1
"""
from tkinter import *
root = Tk()

root.title("Welcome")
computer = Label(root, bg="green", fg="white", text="Computer",
                 font=("Times", 50, "normal"))
science_is = Label(root, bg="blue", fg="yellow", text="Science is",
                   font=("Comic Sans", 50, "bold"))
awesome = Label(root, bg="orange", fg="red", text="awesome!",
                font=("Britannica", 60, "bold"))

computer.pack()
science_is.pack()
awesome.pack()


root.mainloop()
