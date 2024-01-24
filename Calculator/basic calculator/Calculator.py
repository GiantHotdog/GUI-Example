import tkinter as Tk


def enter_press():
    contents = entry.get()
    entry.delete(0, Tk.END)
    entry.insert(0, eval(contents))


window = Tk.Tk()
window.title("Calculator")
window.resizable(False, False)

entry = Tk.Entry(window)
entry.pack()

enter_button = Tk.Button(window, text="Enter", command=enter_press)
enter_button.pack()

window.bind("<Return>", lambda e: enter_press())

window.mainloop()
