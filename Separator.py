import tkinter as tk
from tkinter import ttk

window = tk.Tk()

btn1 = ttk.Button(window, text="Button 1")
btn2 = ttk.Button(window, text="Button 2")
sep = ttk.Separator(window, orient=tk.HORIZONTAL)

btn1.grid(column=0, row=0)
btn2.grid(column=0, row=2)
sep.grid(column=0, row=1)

btn3 = ttk.Button(window, text="Button 3")
btn3.grid(column=0, row=3)

tk.mainloop()
