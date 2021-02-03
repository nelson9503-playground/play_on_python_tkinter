import tkinter as tk
from tkinter import ttk

window = tk.Tk()

scroll = ttk.Scrollbar(window)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

box = tk.Listbox(window, yscrollcommand=scroll.set)
for line in range(1, 100):
    box.insert(line, "Number"+str(line))
box.pack(side=tk.LEFT, fill=tk.BOTH)

scroll.configure(command=box.yview)

window.mainloop()
