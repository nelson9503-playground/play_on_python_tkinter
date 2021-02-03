import tkinter as tk
from tkinter import simpledialog

# Not like filedialog and messagebox,
# simpledialog MUST create a mainwindow.

# None is return for cancelling.

win = tk.Tk()

ans = simpledialog.askfloat("Ask Float", "Give me a float:")
print(ans)

ans = simpledialog.askinteger("Ask Integer", "Give me a Integer:")
print(ans)

ans = simpledialog.askstring("Ask String", "Give me a String:")
print(ans)

win.mainloop()
