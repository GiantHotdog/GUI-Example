import tkinter as Tk
from sqlite3 import *


def on_button_press():
    print("Button pressed")
    print(entry.get())


# def destroy():
#     window.destroy()


window = Tk.Tk()
# window, text="Press", command=on_button_press)
button = Tk.Button(text="Enter", command=on_button_press)
button.pack()

# button2 = Tk.Button(window, text="Close", command=destroy)
# button2.pack()

entry = Tk.Entry(window)
entry.pack()

window.bind("<Return>", lambda e: on_button_press())

window.mainloop()
