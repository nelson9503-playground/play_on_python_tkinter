from tkinter import filedialog

"""
Some options of filedialog:

    - parent
    - title
    - initaldir
    - filetypes
    - defaultextension (for saving dialog)
    - multiple (True or False)

"""


# Get the file name for opening file.
# Return None if open cancelled.
filename = filedialog.askopenfilename(
    title="Open File",  # "," should be added to make types as tuple
    filetypes=(("CSV Files", "*.csv"),),
    defaultextension=".csv",
    initialdir="C:/"  # you may use this option to set default file name
)


# Get the file name for saving file.
# Return None if save cancelled.
filename = filedialog.asksaveasfilename(
    title="Save File",  # "," should be added to make types as tuple
    filetypes=(("PDF Files", "*.pdf"),),
    defaultextension=".pdf",
    initialdir="C:/"  # you may use this option to set default file name
)
