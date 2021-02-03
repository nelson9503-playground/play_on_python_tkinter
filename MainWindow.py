import tkinter as tk

win = tk.Tk()

# set title
win.title("Tkinter Main Window")

# set window size
win.geometry("800x800")

# fix the size of window, user cannot resize the window
win.resizable(0, 0)

win.mainloop()