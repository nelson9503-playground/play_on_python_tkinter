import tkinter as tk
from tkinter import ttk


def get_values():
    print(var1.get())
    print(var2.get())


win = tk.Tk()

# Create TK variables to track the checkbox
var1 = tk.IntVar(value=0)
var2 = tk.BooleanVar()

# Create check boxes
check1 = ttk.Checkbutton(win, text="Option1", variable=var1)
check1.pack()

check2 = ttk.Checkbutton(win, text="Opetion2", variable=var2)
check2.pack()

# Create a button to get the value from check boxes
btn = ttk.Button(win, text="Get Values", command=get_values)
btn.pack()

win.mainloop()
