import tkinter as tk


def click_event():
    print("check")


win = tk.Tk()

# setup menu
menu = tk.Menu(win)
win.config(menu=menu)

# m1
m1 = tk.Menu(menu, tearoff=0)  # tearoff remove split line
m1.add_command(label="m1-func1", command=click_event)
m1.add_command(label="m1-func2")

# m2
m2 = tk.Menu(menu)
m2.add_command(label="m2-func1")
m2.add_command(label="m2-func2")

# setup m1 and m2
menu.add_cascade(label="M1", menu=m1)
menu.add_cascade(label="M2", menu=m2)

win.mainloop()
