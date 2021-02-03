import tkinter as tk
from tkinter import ttk


def get_value():
    for item in box.curselection():
        print(box.get(item))


win = tk.Tk()

box = tk.Listbox(win, selectmode="multiple")
box.pack()
# insert options
box.insert(0, "option1")
box.insert(1, "option2")
box.insert(2, "option3")

# create a button to get values
btn = ttk.Button(win, text="Get Values", command=get_value)
btn.pack()

win.mainloop()
