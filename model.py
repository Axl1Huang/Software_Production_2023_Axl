import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FileBrowserWidget(tk.Frame):
    def __init__(self, parent, path, prediction_instance, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.path = path
        self.selected_file = None
        self.parent = parent
        self.prediction_instance = prediction_instance

        # Create a treeview with 3 columns
        self.treeview = ttk.Treeview(self, columns=("File", "Delete"), show="headings", selectmode="browse")
        self.treeview.heading("File", text="File")
        self.treeview.column("File", width=150, anchor=tk.W)
        self.treeview.heading("Delete", text="Delete")
        self.treeview.column("Delete", width=150, anchor=tk.CENTER)

        self.treeview.tag_configure("file", background="lightgray")

        self.treeview.pack(fill=tk.BOTH, expand=True)
        self.treeview.bind("<Button-1>", self.on_treeview_click)

        # Add a Select button below the treeview
        self.select_button = tk.Button(self, text="Select", command=self.load_selected_model)
        self.select_button.pack()

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
                self.selected_file = file
                self.treeview.selection_set(item_id)  # Set the clicked item as selected

            elif column == "#2":
                # Delete button clicked
                result = messagebox.askyesno("Delete File", f"Are you sure you want to delete {file}?")
                if result:
                    self.delete_file(file)
                    self.treeview.delete(item_id)
            self.on_file_select()

    def load_selected_model(self):
        if self.selected_file is not None:
            model_path = os.path.join(self.path, self.selected_file)
            self.prediction_instance.load_model(model_path)  # Load the selected model

            # Get the input columns from the loaded model
            model_input_columns = self.prediction_instance.input_columns

            # Pass the input columns to the third page and create entry boxes
            enter_page = self.parent.get_page(3)  # Get the third page instance
            enter_page.selected_columns = model_input_columns  # Pass the selected_columns to the third page
            enter_page.create_entry_boxes()  # Create the entry boxes

    def delete_file(self, file):
        file_path = os.path.join(self.path, file)
        os.remove(file_path)

    def get_selected_file_path(self):
        selected_item = self.treeview.selection()
        if selected_item:
            file_name = self.treeview.item(selected_item[0], "values")[0]
            return os.path.join(self.path, file_name)
        else:
            return None
    def on_file_select(self):
        self.parent.treeview_selected = True

    def get_selected_columns(self):
        selected_columns = []
        for item in self.treeview.selection():
            column_name = self.treeview.item(item)["text"]
            selected_columns.append(column_name)
        return selected_columns