import tkinter as tk
from tkinter import ttk

# Virtual Events
# <<NotebookTabChanged>>


def enableTag():
    notebook.add(tag4, text="tag4", state="normal")


window = tk.Tk()

notebook = ttk.Notebook(window)

tag1 = ttk.Frame(notebook)
tag2 = ttk.Frame(notebook)
tag3 = ttk.Frame(notebook)
tag4 = ttk.Frame(notebook)

btn = ttk.Button(tag1, text="press me", command=enableTag)
btn.grid(column=0, row=0)

notebook.add(tag1, text="tag1")
notebook.add(tag2, text="tag2")
notebook.add(tag3, text="tag3", state="disabled")
notebook.add(tag4, text="tag4", state="hidden")

notebook.grid(column=0, row=0)

window.mainloop()
