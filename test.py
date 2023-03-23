import tkinter as tk
from tkinter import filedialog
import pandas as pd

class DragAndDropBox(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.master.title("Drag and Drop Box")
        self.master.geometry("400x300")
        self.master.config(bg="white")

        self.label = tk.Label(self.master, text="Drag and Drop a CSV file here!", font=("Arial", 14), bg="white")
        self.label.pack(expand=True)

        self.label.bind("<Button-1>", self.browse_files)
        self.label.bind("<B1-Motion>", self.drag_motion)
        self.label.bind("<ButtonRelease-1>", self.drop_file)

    def browse_files(self, event):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.file_path = file_path
        self.label.config(text="File selected: " + self.file_path)

    def drag_motion(self, event):
        self.label.config(bg="lightgray")

    def drop_file(self, event):
        self.label.config(bg="white")

        if hasattr(self, "file_path"):
            df = pd.read_csv(self.file_path)
            self.show_data(df)

    def show_data(self, df):
        top = tk.Toplevel()
        top.title("CSV Data")
        top.geometry("600x400")

        data_frame = tk.Frame(top)
        data_frame.pack(fill="both", expand=True)

        # create scrollbar
        scrollbar = tk.Scrollbar(data_frame)
        scrollbar.pack(side="right", fill="y")

        # create table
        table = tk.Frame(data_frame)
        table.pack(fill="both", expand=True)

        # add data to table
        for i, col_name in enumerate(df.columns):
            tk.Label(table, text=col_name, relief="solid", width=20).grid(row=0, column=i)
            for j, cell_value in enumerate(df[col_name]):
                tk.Label(table, text=cell_value, relief="solid", width=20).grid(row=j+1, column=i)

        # configure scrollbar
        scrollbar.config(command=table.yview)

if __name__ == "__main__":
    root = tk.Tk()
    app = DragAndDropBox(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
