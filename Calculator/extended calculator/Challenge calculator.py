import tkinter as Tk
import re
from tkinter import messagebox


def enter_press():
    contents = entry.get()
    print("validating")
    if re.search("^[0-9\+\-\*/\(\)]*$", contents):
        entry.config(state="normal")
        entry.delete(0, Tk.END)
        entry.insert(0, eval(contents))
        entry.config(state="readonly")
        print("validates")
    else:
        messagebox.showerror(
            "Error", "contents of input box were not numbers or calculation symbols.")


def one():
    entry.config(state="normal")
    entry.insert(Tk.END, "1")
    entry.config(state="readonly")


def two():
    entry.config(state="normal")
    entry.insert(Tk.END, "2")
    entry.config(state="readonly")


def three():
    entry.config(state="normal")
    entry.insert(Tk.END, "3")
    entry.config(state="readonly")


def four():
    entry.config(state="normal")
    entry.insert(Tk.END, "4")
    entry.config(state="readonly")


def five():
    entry.config(state="normal")
    entry.insert(Tk.END, "5")
    entry.config(state="readonly")


def six():
    entry.config(state="normal")
    entry.insert(Tk.END, "6")
    entry.config(state="readonly")


def seven():
    entry.config(state="normal")
    entry.insert(Tk.END, "7")
    entry.config(state="readonly")


def eight():
    entry.config(state="normal")
    entry.insert(Tk.END, "8")
    entry.config(state="readonly")


def nine():
    entry.config(state="normal")
    entry.insert(Tk.END, "9")
    entry.config(state="readonly")


def zero():
    entry.config(state="normal")
    entry.insert(Tk.END, "0")
    entry.config(state="readonly")


def plus():
    entry.config(state="normal")
    entry.insert(Tk.END, "+")
    entry.config(state="readonly")


def minus():
    entry.config(state="normal")
    entry.insert(Tk.END, "-")
    entry.config(state="readonly")


def times():
    entry.config(state="normal")
    entry.insert(Tk.END, "*")
    entry.config(state="readonly")


def divide():
    entry.config(state="normal")
    entry.insert(Tk.END, "/")
    entry.config(state="readonly")


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

entry = Tk.Entry(window, foreground="black", )
entry.config(state="readonly")
entry.pack()

enter_button = Tk.Button(window, text="Enter", command=enter_press)
enter_button.place(x=300/2-horizontal_offset, y=vertical_offset+135)

button_one = Tk.Button(window, command=one, text="1")
button_one.place(x=300/2-45-horizontal_offset, y=vertical_offset)

button_two = Tk.Button(window, command=two, text="2")
button_two.place(x=300/2-horizontal_offset, y=vertical_offset)

button_three = Tk.Button(window, command=three, text="3")
button_three.place(x=300/2+45-horizontal_offset, y=vertical_offset)

button_four = Tk.Button(window, command=four, text="4")
button_four.place(x=300/2-45-horizontal_offset, y=vertical_offset+45)

button_five = Tk.Button(window, command=five, text="5")
button_five.place(x=300/2-horizontal_offset, y=vertical_offset+45)

button_six = Tk.Button(window, command=six, text="6")
button_six.place(x=300/2+45-horizontal_offset, y=vertical_offset+45)

button_seven = Tk.Button(window, command=seven, text="7")
button_seven.place(x=300/2-45-horizontal_offset, y=vertical_offset+90)

button_eight = Tk.Button(window, command=eight, text="8")
button_eight.place(x=300/2-horizontal_offset, y=vertical_offset+90)

button_nine = Tk.Button(window, command=nine, text="9")
button_nine.place(x=300/2+45-horizontal_offset, y=vertical_offset+90)

button_zero = Tk.Button(window, command=zero, text="0")
button_zero.place(x=300/2-45-horizontal_offset, y=vertical_offset+135)

button_plus = Tk.Button(window, command=plus, text="+")
button_plus.place(x=300/2-90-horizontal_offset, y=vertical_offset)

button_minus = Tk.Button(window, command=minus, text="-")
button_minus.place(x=300/2-90-horizontal_offset, y=vertical_offset+45)

button_times = Tk.Button(window, command=times, text="*")
button_times.place(x=300/2-90-horizontal_offset, y=vertical_offset+90)

button_divide = Tk.Button(window, command=divide, text="/")
button_divide.place(x=300/2-90-horizontal_offset, y=vertical_offset+135)

button_backspace = Tk.Button(window, command=backspace, text="C")
button_backspace.place(x=300/2+90-horizontal_offset, y=vertical_offset)


window.bind("<Return>", lambda e: enter_press())

window.mainloop()
