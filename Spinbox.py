import tkinter as tk
from tkinter import ttk

# Virtual events
# <<Increment>>
# <<Decrement>>

window = tk.Tk()


def event():
    print(spin.get())


spin = ttk.Spinbox(
    master=window,
    from_=0,  # use from_ since from is a keyword of Python
    to=10,
    increment=0.5,
    wrap=True,  # make cycle
    format="%05f",
    command=event
)
spin.grid(column=0, row=0)

string_spin = ttk.Spinbox(
    values=[
        "val1",
        "val2",
        "val3"
    ],
    wrap=True,
    command=event
)
string_spin.grid(column=1, row=1)

tk.mainloop()
