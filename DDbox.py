import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import os
from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter.messagebox as messagebox
import pandas as pd
from tkinter import Tk, Label, Canvas, PhotoImage
from PIL import Image
import customtkinter as ctk
from PIL import ImageTk, Image

class DragAndDropWidget(tk.Frame):
    def __init__(self, parent, app, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg="#91E9FD", width=300, height=300)
        self.drop_text = tk.Label(self, text="Drop CSV File Here", bg="#91E9FD", fg="white", font = ("Arial", 15))
        self.drop_text.place(x=55, y=30)

        # self.canvas = Canvas(self, width=180, height=180, bg="#C2EFFA", highlightthickness=0)
        # self.canvas.place(x=50, y=60)

        # small_blue_box = tk.Frame(self, bg="#C2EFFA", width=120, height=120)
        # small_blue_box.place(relx=0.52, rely=0.55, anchor=tk.CENTER)


        self.path = None
        self.app = app
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.on_drop)
    def reset(self):
        self.path = None
        self.drop_text.config(text="Drop CSV File Here")
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
        self.app.shared_data["uploaded_file_path"] = self.path

    def handle_file(self, file_path):
        print(f"Handling file: {file_path}")
        self.path = file_path
        # Perform actions with the CSV file
        try:
            df = pd.read_csv(file_path, nrows=0)  # Read only the header row
            column_names = df.columns.tolist()

            if column_names:
                column_selection_dialog = ColumnSelectionDialog(self.master, column_names)
                selected_columns = column_selection_dialog.result
                if selected_columns:  # Check if selected_columns is not empty
                    print(f"Selected columns: {selected_columns}")
                    self.send_selected_columns_to_third_page(selected_columns)
                    messagebox.showinfo("Success", "You have successfully selected columns.")
                else:
                    messagebox.showerror("Nothing selected", "You have to select content to continue, otherwise there is no entry box in the next page.")
            else:
                messagebox.showerror("Invalid file", "The CSV file is empty or has no header.")
        except pd.errors.EmptyDataError:
            messagebox.showerror("Invalid file", "The CSV file is empty.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while reading the file: {e}")

    def send_selected_columns_to_third_page(self, selected_columns):
        print(f"Setting selected_columns to {selected_columns}")
        self.app.shared_data["selected_columns"] = selected_columns
class ColumnSelectionDialog(simpledialog.Dialog):
    def __init__(self, parent, columns):
        self.columns = columns
        self.result = []
        super().__init__(parent, title="Select a Column")

    def body(self, master):
        tk.Label(master, text="Select a column to use:\nMention: Price column is mandatory to be selected for training").pack(pady=10)

        self.listbox = tk.Listbox(master, selectmode=tk.MULTIPLE, exportselection=0)
        for column in self.columns:
            self.listbox.insert(tk.END, column)
        self.listbox.pack(padx=10, pady=5)

        return self.listbox

    def validate(self):
        selected_indices = self.listbox.curselection()
        selected_columns = [self.columns[i] for i in selected_indices]

        if len(selected_indices) >= 1:
            if "price" not in selected_columns:
                messagebox.showwarning("Price column missing", "Please ensure you select the 'Price' column.")
                return False
            elif len(selected_indices) == 1:
                messagebox.showwarning("Training column missing", "Please ensure you select the two column.(price included)")
                return False
            else:
                return True
        else:
            messagebox.showwarning("No Selection", "Please select at least two column from the training.(price included)")
            return False

    def apply(self):
        selected_indices = self.listbox.curselection()
        self.result = [self.columns[i] for i in selected_indices]
def main():
    root = TkinterDnD.Tk()
    root.title("Drag and Drop CSV")
    root.geometry("400x400")

    drag_and_drop_widget = DragAndDropWidget(root, app=root)
    drag_and_drop_widget.place(x=50, y=50)

    root.mainloop()

if __name__ == "__main__":
    main()