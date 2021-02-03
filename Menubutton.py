import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("800x600")

# setup menubutton
menu = ttk.Menubutton(window, text="MenuButton")
menu.pack()

main = tk.Menu(menu, tearoff=0)
main.add_command(label="test")

menu["menu"] = main

window.mainloop()
