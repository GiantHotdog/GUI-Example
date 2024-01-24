import tkinter as Tk
import re
from tkinter import messagebox


def enter_press():
    contents = entry.get()
    if re.search("^[0-9\+\-\*/]", contents):
        entry.delete(0, Tk.END)
        entry.insert(0, eval(contents))
    else:
        messagebox.showerror(
            "Error.", "contents of input box were not numbers or calculation symbols")


window = Tk.Tk()
window.title("Calculator")
window.resizable(False, False)

entry = Tk.Entry(window)
entry.pack()

enter_button = Tk.Button(window, text="Enter", command=enter_press)
enter_button.pack()

window.bind("<Return>", lambda e: enter_press())

window.mainloop()
