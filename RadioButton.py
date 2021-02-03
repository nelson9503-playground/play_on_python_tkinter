import tkinter as tk
from tkinter import ttk


def get_value():
    print(var1.get())


window = tk.Tk()

# Create a TK variable to track radio options
var1 = tk.IntVar(value=1)

radio1 = ttk.Radiobutton(window, text="Option1", variable=var1, value=1)
radio1.pack()

radio2 = ttk.Radiobutton(window, text="Option2", variable=var1, value=2)
radio2.pack()

# create a button to get value
btn = ttk.Button(window, text="Get Values", command=get_value)
btn.pack()

window.mainloop()
