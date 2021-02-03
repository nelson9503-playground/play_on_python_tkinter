import tkinter as tk
from tkinter import ttk


def newWin():
    win = tk.Toplevel()
    win.geometry("600x600")


window = tk.Tk()

btn = ttk.Button(window, text="Show New Window", command=newWin)
btn.grid(column=0, row=0)

window.mainloop()
