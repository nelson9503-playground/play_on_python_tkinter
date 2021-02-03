import tkinter as tk
from tkinter import ttk

# selection return the values from line selected by users


def output():
    for item in tree.selection():
        text = tree.item(item, "values")
        print(text)


window = tk.Tk()

# show = "headings" hide the first column
tree = ttk.Treeview(window, columns=["1", "2", "3"], show="headings")

# columns
tree.column("1", width=200, minwidth=200, anchor="center")
tree.column("2", width=200, anchor="center")
tree.column("3", width=200, anchor="center")

# headings
tree.heading("1", text="Name")
tree.heading("2", text="Gender")
tree.heading("3", text="Age")

# insert
folder = tree.insert("", 1, None, values=("Folder", "", ""))
tree.insert(folder, 1, None, values=("Tom", "M", "30"))

tree.grid(column=0, row=0)


btn = ttk.Button(window, text="Output", command=output)
btn.grid(column=0, row=1)

window.mainloop()
