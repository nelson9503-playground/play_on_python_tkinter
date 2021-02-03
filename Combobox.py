import tkinter as tk
from tkinter import ttk

# bind function


def bindfunc(event):
    print("Element Select Event.")


win = tk.Tk()

# Combo1
combo1 = ttk.Combobox(
    win,
    values=["option1", "option2"],  # preset values
    state="readonly"  # user can choose options, but cannot typing.
)
combo1.set("please choose a option")  # set the default message
combo1.bind("<<ComboboxSelected>>", bindfunc)  # bind event to function
combo1.pack()

# Combo2
combo2 = ttk.Combobox(win, values=["option1", "option2"])
combo2.current(0)  # set the first option as default
combo2.pack()

win.mainloop()
