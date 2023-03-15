import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image

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
  #############
  # FUNCTIONS #
  #############
  def proceed(self):
    self.app.show_page(3)

  def back(self):
    self.app.show_page(1)
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent)
    self.app = app

    NORMALFONT = app.styles.get("NORMALFONT")
    LARGEFONT = app.styles.get("LARGEFONT")


    self.labelTitle = ctk.CTkLabel(master=self, text = "Upload Area", font = LARGEFONT)
    self.labelTitle.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    self.label_upload_Area = ctk.CTkLabel(master=self, text = "Upload Area", font = NORMALFONT)
    self.label_upload_Area.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

    self.label_Enter_information = ctk.CTkLabel(master=self, text = "Enter Information", font = NORMALFONT)
    self.label_Enter_information.place(relx=0.2, rely=0.4, anchor=tk.CENTER)
    
    self.ButtonBack = ctk.CTkButton(master=self, text="Back", command= lambda : self.back(),fg_color="yellow",text_color="black")
    self.ButtonBack.place(relx=0.2, rely=0.8, anchor=tk.CENTER)

    self.label_Predicted_Price_Show = ctk.CTkLabel(master=self, text = "Predicted Price Show", font = NORMALFONT)
    self.label_Predicted_Price_Show.place(relx=0.2, rely=0.6, anchor=tk.CENTER)

    self.ButtonUpload = ctk.CTkButton(master=self, text="Upload", command= lambda : self.proceed(),fg_color="green",text_color="black")
    self.ButtonUpload.place(relx=0.7, rely=0.8, anchor=tk.CENTER)
