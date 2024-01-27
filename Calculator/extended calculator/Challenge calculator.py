import tkinter as Tk
import re
from tkinter import messagebox


def enter_press():
    contents = entry.get()
    if re.search("^[0-9\+\-\*/\(\)]*$", contents):
        entry.config(state="normal")
        entry.delete(0, Tk.END)
        entry.insert(0, eval(contents))
        entry.config(state="readonly")
    else:
        messagebox.showerror(
            "Error", "contents of input box were not numbers or calculation symbols.")


def make_cmd(cmd):
    def action():
        entry.config(state="normal")
        entry.insert(Tk.END, cmd)
        entry.config(state="readonly")
    return action


def backspace():
    contents = entry.get()
    entry.config(state="normal")
    entry.delete(len(contents)-1, Tk.END)
    entry.config(state="readonly")


window = Tk.Tk()
window.title("Calculator")
window.resizable(False, False)
width = window.winfo_screenwidth()
height = window.winfo_screenwidth()
window.geometry("300x500")
vertical_offset = 50
horizontal_offset = 15

entry = Tk.Entry(window)
entry.config(state="readonly")
entry.pack()

enter_button = Tk.Button(window, text="Enter", command=enter_press)
enter_button.place(x=300/2-horizontal_offset, y=vertical_offset+135)

button_one = Tk.Button(window, command=make_cmd("1"), text="1")
button_one.place(x=300/2-45-horizontal_offset, y=vertical_offset)

button_two = Tk.Button(window, command=make_cmd("2"), text="2")
button_two.place(x=300/2-horizontal_offset, y=vertical_offset)

button_three = Tk.Button(window, command=make_cmd("3"), text="3")
button_three.place(x=300/2+45-horizontal_offset, y=vertical_offset)

button_four = Tk.Button(window, command=make_cmd("4"), text="4")
button_four.place(x=300/2-45-horizontal_offset, y=vertical_offset+45)

button_five = Tk.Button(window, command=make_cmd("5"), text="5")
button_five.place(x=300/2-horizontal_offset, y=vertical_offset+45)

button_six = Tk.Button(window, command=make_cmd("6"), text="6")
button_six.place(x=300/2+45-horizontal_offset, y=vertical_offset+45)

button_seven = Tk.Button(window, command=make_cmd("7"), text="7")
button_seven.place(x=300/2-45-horizontal_offset, y=vertical_offset+90)

button_eight = Tk.Button(window, command=make_cmd("8"), text="8")
button_eight.place(x=300/2-horizontal_offset, y=vertical_offset+90)

button_nine = Tk.Button(window, command=make_cmd("9"), text="9")
button_nine.place(x=300/2+45-horizontal_offset, y=vertical_offset+90)

button_zero = Tk.Button(window, command=make_cmd("0"), text="0")
button_zero.place(x=300/2-45-horizontal_offset, y=vertical_offset+135)

button_plus = Tk.Button(window, command=make_cmd("+"), text="+")
button_plus.place(x=300/2-90-horizontal_offset, y=vertical_offset)

button_minus = Tk.Button(window, command=make_cmd("-"), text="-")
button_minus.place(x=300/2-90-horizontal_offset, y=vertical_offset+45)

button_times = Tk.Button(window, command=make_cmd("*"), text="*")
button_times.place(x=300/2-90-horizontal_offset, y=vertical_offset+90)

button_divide = Tk.Button(window, command=make_cmd("/"), text="/")
button_divide.place(x=300/2-90-horizontal_offset, y=vertical_offset+135)

button_backspace = Tk.Button(window, command=backspace, text="C")
button_backspace.place(x=300/2+90-horizontal_offset, y=vertical_offset)


window.bind("<Return>", lambda e: enter_press())

window.mainloop()
