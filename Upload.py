import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from DDbox import DragAndDropWidget
from model import FileBrowserWidget
from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter.messagebox as messagebox
from DDbox import DragAndDropWidget as dd

class second(tk.Frame):
  
    ##############
    # COMPONENTS #
    ##############

    labelTitle: ctk.CTkLabel = None
    label_upload_Area:ctk.CTkLabel = None
    label_Enter_information:ctk.CTkLabel = None
    label_Predicted_Price_Show:ctk.CTkLabel = None
    ButtonBack : ctk.CTkButton = None
    ButtonUpload : ctk.CTkButton = None
    saved_path = "src\saved_model"
    label_Saved : ctk.CTkButton = None

    #############
    # FUNCTIONS #
    #############
    def on_confirm_button_click(self):
        model_file_path = self.file_browser.get_selected_file_path()
        if model_file_path is None:
            tk.messagebox.showwarning(title="Warning", message="Please choose a model file before proceeding.")
        else:
            # Save the selected model path to the App class
            self.app.shared_data["selected_model_path"] = model_file_path

    def proceed(self):
      uploaded_file_path = self.drag_and_drop_widget.path
      model_file_path = self.file_browser.get_selected_file_path()

      if not uploaded_file_path and not model_file_path:
          tk.messagebox.showwarning(title="Warning", message="Please upload a CSV file or select a saved model before proceeding.")
          return

      if uploaded_file_path:
          # Check if 'selected_columns' is in 'shared_data'
          if "selected_columns" in self.app.shared_data:
              print(self.app.shared_data["selected_columns"])
          else:
              tk.messagebox.showwarning(title="Warning", message="Please select columns from the uploaded CSV file before proceeding.")
              return

      if model_file_path:
          self.app.shared_data["selected_model_path"] = model_file_path
          # read the columns from the saved model file and update 'selected_columns'
          self.app.shared_data["selected_columns"] = self.file_browser.get_selected_columns()
          print(self.app.shared_data["selected_columns"])
      self.app.show_page(3)

    def back(self):
        self.app.show_page(1)

    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent)
        self.app = app
        self.file_browser = FileBrowserWidget(self, self.saved_path, self.app.prediction_instance)
        NORMALFONT = app.styles.get("NORMALFONT")
        LARGEFONT = app.styles.get("LARGEFONT")

        self.labelTitle = ctk.CTkLabel(master=self, text="Upload Area", font=LARGEFONT)
        self.labelTitle.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.label_upload_Area = ctk.CTkLabel(master=self, text="Upload Area", font=NORMALFONT)
        self.label_upload_Area.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

        self.label_Enter_information = ctk.CTkLabel(master=self, text="Enter Information", font=NORMALFONT)
        self.label_Enter_information.place(relx=0.2, rely=0.4, anchor=tk.CENTER)
    
        self.ButtonBack = ctk.CTkButton(master=self, text="Back", command= lambda : self.back(), fg_color="yellow", text_color="black")
        self.ButtonBack.place(relx=0.2, rely=0.8, anchor=tk.CENTER)

        self.label_Predicted_Price_Show = ctk.CTkLabel(master=self, text="Predicted Price Show", font=NORMALFONT)
        self.label_Predicted_Price_Show.place(relx=0.2, rely=0.6, anchor=tk.CENTER)


        self.ButtonUpload = ctk.CTkButton(master=self, text="Confirm", command=lambda: self.proceed(), fg_color="green", text_color="black")
        self.ButtonUpload.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

        ### Define Drag and Drop box
        self.drag_and_drop_widget = DragAndDropWidget(self, app=app)
        self.drag_and_drop_widget.place(relx=0.8, rely=0.5, anchor=tk.CENTER)

        self.label_Saved = ctk.CTkLabel(master=self, text="Saved Model", font=NORMALFONT)
        self.label_Saved.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.file_browser = FileBrowserWidget(self, self.saved_path, self.app.prediction_instance)
        self.file_browser.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Add the Confirm button after creating the FileBrowserWidget instance
        self.confirm_button = tk.Button(self, text="select", command=self.on_confirm_button_click)
        self.confirm_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    