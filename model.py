import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FileBrowserWidget(tk.Frame):
    def __init__(self, parent, path, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.path = path

        # Create a treeview with 3 columns
        self.treeview = ttk.Treeview(self, columns=("File", "Delete"), show="headings", selectmode="none")
        self.treeview.heading("File", text="File")
        self.treeview.column("File", width=150, anchor=tk.W)
        self.treeview.heading("Delete", text="Delete")
        self.treeview.column("Delete", width=150, anchor=tk.CENTER)
        
        self.treeview.tag_configure("file", background="lightgray")

        self.treeview.pack(fill=tk.BOTH, expand=True)
        self.treeview.bind("<Button-1>", self.on_treeview_click)

        self.populate_treeview()

    def populate_treeview(self):
        # Clear the treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Add files from the specified path to the treeview
        for file in os.listdir(self.path):
            self.treeview.insert("", tk.END, text=file, values=(file, "Delete"), tags=("file",))

    def on_treeview_click(self, event):
        item_id = self.treeview.identify_row(event.y)
        column = self.treeview.identify_column(event.x)

        if item_id:
            file = self.treeview.item(item_id, "values")[0]

            if column == "#1":
                # File name clicked
                print(f"File clicked: {file}")
            elif column == "#2":
                # Delete button clicked
                result = messagebox.askyesno("Delete File", f"Are you sure you want to delete {file}?")
                if result:
                    self.delete_file(file)
                    self.treeview.delete(item_id)

    def delete_file(self, file):
        file_path = os.path.join(self.path, file)
        os.remove(file_path)

    def get_selected_file(self):
        selected_item = self.treeview.selection()
        if selected_item:
            return self.treeview.item(selected_item[0], "values")[0]
        else:
            return None
