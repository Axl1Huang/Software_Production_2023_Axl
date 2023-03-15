import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog

root = tk.Tk()

# create a label widget to display the uploaded file name
file_label = tk.Label(root, text="Drop file here", font=("Helvetica", 16), pady=50)
file_label.pack()

# create a custom event handler for the drag and drop event
def handle_drop(event):
    # get the filename(s) of the dropped file(s)
    filenames = ctk.get_dropfiles(event)
    filename = filenames[0]
    print('Dropped file:', filename)
    
    # do something with the file, e.g. display its contents
    with open(filename, 'r') as file:
        contents = file.read()
    print('File contents:', contents)

# bind the event handler to the label widget
file_label.bind('<Drop>', handle_drop)

root.mainloop()