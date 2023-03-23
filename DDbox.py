import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import os
from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter.messagebox as messagebox

class DragAndDropWidget(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg="blue", width=300, height=300)

        self.drop_text = tk.Label(self, text="Drop CSV file here", bg="blue", fg="white")
        self.drop_text.place(x=100, y=140)

        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.on_drop)

    def on_drop(self, event):
        data = event.data.strip().split("\n")
        print(f"Data received: {data}")
        for item in data:
            if item:
                file_path = item.replace('{', '').replace('}', '')
                if os.path.isfile(file_path):
                    if file_path.lower().endswith(".csv"):
                        self.handle_file(file_path)
                    else:
                        messagebox.showerror("Invalid file", "Only CSV files are allowed.")
                else:
                    print(f"Invalid file path: {file_path}")

    def handle_file(self, file_path):
        print(f"Handling file: {file_path}")
        # Perform actions with the CSV file
        self.master.app.csv_file_uploaded(file_path)
        print(f"File dropped: {file_path}")

def main():
    root = TkinterDnD.Tk()
    root.title("Drag and Drop CSV")
    root.geometry("400x400")

    drag_and_drop_widget = DragAndDropWidget(root)
    drag_and_drop_widget.place(x=50, y=50)

    root.mainloop()

if __name__ == "__main__":
    main()
