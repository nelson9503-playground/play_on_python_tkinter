import tkinter as tk
from tkinter import ttk
import time


def progress():
    for i in range(101):
        bar["value"] = i
        bar.update()
        time.sleep(0.1)


window = tk.Tk()

bar = ttk.Progressbar(
    master=window,
    orient=tk.HORIZONTAL,
    length=100)
bar.grid(column=0, row=0)

btn = ttk.Button(
    master=window,
    text="Press Me",
    command=progress
)
btn.grid(column=0, row=1)

window.mainloop()
