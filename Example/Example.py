import tkinter as Tk
from sqlite3 import *


def on_button_press():
    print("Button pressed")
    print(entry.get())


window = Tk.Tk()

button = Tk.Button(text="Enter", command=on_button_press)
button.pack()

entry = Tk.Entry(window)
entry.pack()

window.bind("<Return>", lambda e: on_button_press())

window.mainloop()
