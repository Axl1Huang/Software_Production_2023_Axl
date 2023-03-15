import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

root = tk.Tk()
root.geometry('300x300')

label = ttk.Label(root, text='Drag and drop CSV file here')
label.pack(pady=50)

def on_drag_enter(event):
    event.widget.configure(bg='red')

def on_drag_leave(event):
    event.widget.configure(bg='SystemButtonFace')

def on_drag_motion(event):
    pass

def on_button_release(event):
    filename = event.widget.selection_get().strip()
    if filename.endswith('.csv'):
        data = pd.read_csv(filename)
        print(data.head())
    event.widget.configure(bg='green')

label.bind('<Enter>', on_drag_enter)
label.bind('<Leave>', on_drag_leave)
label.bind('<Motion>', on_drag_motion)
label.bind('<ButtonRelease-1>', on_button_release)

root.mainloop()
