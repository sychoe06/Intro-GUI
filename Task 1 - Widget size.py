""" Intro to GUI - task 1
Setting the size of a widget
"""
from tkinter import *
root = Tk()

root.title("My first window")

# Window .geometry - to set size of 500px wide x 200px tall
root.geometry("600x200")  # string using 'x' not '*' - no spaces either side
root.maxsize(800, 400)  # int values - sets max resizeable dimensions

greeting = Label(text="Hello, Tkinter")


greeting.pack()
root.mainloop()
