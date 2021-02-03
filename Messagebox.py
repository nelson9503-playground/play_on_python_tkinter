from tkinter import messagebox

# Warming
messagebox.showwarning(
    title="Warning",
    message="This is warning box."
)

# Error
messagebox.showerror(
    title="Error",
    message="This is error box."
)

# Info
messagebox.showinfo(
    title="Information",
    message="This is information box."
)

# Ask Question
"""
answers: "yes", "no"
"""
ans = messagebox.askquestion("Ask Question", "Ask user a question.")
print(ans)

# Ask Ok / Cancel
"""
answers: True, False
"""
ans = messagebox.askokcancel("Ask Ok / Cancel", "Ok or Cancel?")
print(ans)

# Ask Retry / Cancel
"""
answers: True, False
"""
ans = messagebox.askretrycancel("Ask Retry / Cancel", "Retry or Cancel?")
print(ans)

# Ask Yes / No
"""
answers: True, False
"""
ans = messagebox.askyesno("Ask Yes / No", "Yes or No?")
print(ans)

# Ask Yes / No / Cancel
"""
ansers: True, False, None
"""
ans = messagebox.askyesnocancel("Ask Yes / No / Cancel", "Yes, No or Cancel?")
print(ans)
