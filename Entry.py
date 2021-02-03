import tkinter as tk
from tkinter import ttk

win = tk.Tk()

entry = ttk.Entry(win)

# insert contents
entry.insert(0, "Insert Contents")

entry.pack()

win.mainloop()
