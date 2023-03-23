import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image

class first(tk.Frame):
  
  ##############
  # COMPONENTS #
  ##############

  labelTitle: ctk.CTkLabel = None
  labelSoftWareName: ctk.CTkLabel = None
  labelSlogan: ctk.CTkLabel = None
  buttonStart : ctk.CTkButton = None
  Image:ctk.CTkImage = None
  labelImage:ctk.CTkLabel = None  
  #############
  # FUNCTIONS #
  #############
  def proceed(self):
    self.app.show_page(2)


  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent)
    self.app = app

    NORMALFONT = app.styles.get("NORMALFONT")
    LARGEFONT = app.styles.get("LARGEFONT")
    MIDDLEFONT = app.styles.get("MIDDLEFONT")


    self.labelTitle = ctk.CTkLabel(master=self, text = "High Tech Old Factory Street", font = LARGEFONT)
    self.labelTitle.place(relx=0.35, rely=0.2, anchor=tk.CENTER)

    self.labelSoftWareName = ctk.CTkLabel(master=self, text = "Housing Price Prediction", font = MIDDLEFONT)
    self.labelSoftWareName.place(relx=0.2, rely=0.4, anchor=tk.CENTER)
    
    self.buttonStart = ctk.CTkButton(master=self, text="Start", command= lambda : self.proceed(),fg_color="white",text_color="black")
    self.buttonStart.place(relx=0.2, rely=0.8, anchor=tk.SW)

    self.labelSlogan = ctk.CTkLabel(master=self, text = "High Quality Forecast", font = NORMALFONT)
    self.labelSlogan.place(relx=0.2, rely=0.6, anchor=tk.CENTER)

    self.Image = ctk.CTkImage(light_image=Image.open("src\img\First_page_image.png"),size=(400,400))
    self.labelImage = ctk.CTkLabel(master=self,text="",image=self.Image)
    self.labelImage.place(relx=0.8,rely=0.8,anchor = tk.SE)