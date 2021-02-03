import tkinter as tk
from tkinter import ttk


def getValue():
    print(var1.get())


window = tk.Tk()

var1 = tk.IntVar()

scale = ttk.Scale(window, orient=tk.HORIZONTAL, from_=0, to=100, variable=var1)
scale.grid(column=0, row=0)

scale1 = ttk.Scale(window, orient=tk.VERTICAL, from_=0, to=100)
scale1.grid(column=0, row=1)

btn = ttk.Button(window, text="Get Value", command=getValue)
btn.grid(column=0, row=2)

window.mainloop()
