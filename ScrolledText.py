import tkinter as tk
from tkinter import scrolledtext

win = tk.Tk()
win.geometry("300x200")

# Scrolltext Frame
f = scrolledtext.Frame(win, bg="grey")
f.pack(fill="both", expand="yes")

text_to_be_inserted = """
Integer posuere erat a ante venenatis dapibus.

Posuere velit aliquet.

Aenean eu leo quam. Pellentesque ornare sem.

Lacinia quam venenatis vestibulum.

Nulla vitae elit libero, a pharetra augue.

Cum sociis natoque penatibus et magnis dis.

Parturient montes, nascetur ridiculus mus.
"""

# Text Area
editArea = scrolledtext.ScrolledText(
    f, wrap=tk.WORD
)
editArea.insert(tk.INSERT, text_to_be_inserted)
editArea.pack()


win.mainloop()
