import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
class forth(tk.Frame):
  
  ##############
  # COMPONENTS #
  ##############

  labelTitle: ctk.CTkLabel = None
  label_upload_Area:ctk.CTkLabel = None
  label_Enter_information:ctk.CTkLabel = None
  label_Predicted_Price_Show:ctk.CTkLabel = None
  label_result:ctk.CTkLabel = None
  label_user_column:ctk.CTkLabel = None
  label_Model_accuracy:ctk.CTkLabel =None
  ButtonBack : ctk.CTkButton = None
  ButtonSave : ctk.CTkButton = None
  user_result=0
  model_acc=0
  user_column= None
  #############
  # FUNCTIONS #
  #############
  def update_labels(self):
    self.label_result.configure(text=f"The prediction of price based on your input is: {self.user_result}")
    self.label_Model_accuracy.configure(text=f"The accuracy of Model Accuracy based on your selected is: {self.model_acc:2f}")
    self.label_user_column.configure(text=f"The columns you selected for training are:{self.user_column}")
  def back(self):
    self.app.show_page(3)
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent)
    self.app = app
    NORMALFONT = app.styles.get("NORMALFONT")
    LARGEFONT = app.styles.get("LARGEFONT")


    self.labelTitle = ctk.CTkLabel(master=self, text = "Predicted Price Show", font = LARGEFONT)
    self.labelTitle.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    self.label_upload_Area = ctk.CTkLabel(master=self, text = "Upload Area", font = NORMALFONT)
    self.label_upload_Area.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

    self.label_Enter_information = ctk.CTkLabel(master=self, text = "Enter Information", font = NORMALFONT)
    self.label_Enter_information.place(relx=0.2, rely=0.4, anchor=tk.CENTER)
    
    self.ButtonBack = ctk.CTkButton(master=self, text="Back", command= lambda : self.back(),fg_color="yellow",text_color="black")
    self.ButtonBack.place(relx=0.2, rely=0.8, anchor=tk.CENTER)

    self.label_Predicted_Price_Show = ctk.CTkLabel(master=self, text = "Predicted Price Show", font = NORMALFONT)
    self.label_Predicted_Price_Show.place(relx=0.2, rely=0.6, anchor=tk.CENTER)
    
    self.ButtonSave = ctk.CTkButton(master=self, text="Save Model", command= lambda : self.back(),fg_color="yellow",text_color="black")
    self.ButtonSave.place(relx=0.6, rely=0.8, anchor=tk.CENTER)


    self.label_result = ctk.CTkLabel(master=self, text = f"The prediction of price based on your input is:{self.user_result:2f}", font = NORMALFONT)
    self.label_result.place(relx=0.7, rely=0.3, anchor=tk.CENTER)

    self.label_Model_accuracy = ctk.CTkLabel(master=self, text = f"The accuracy of Model Accuracy based on your selected is:{self.model_acc:.2f}", font = NORMALFONT)
    self.label_Model_accuracy.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

    self.label_user_column = ctk.CTkLabel(master=self, text = f"The columns you selected for training are:{self.user_column}", font = NORMALFONT)
    self.label_user_column.place(relx=0.7, rely=0.5, anchor=tk.CENTER)
    