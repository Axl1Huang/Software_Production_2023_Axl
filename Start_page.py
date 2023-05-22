import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
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
    self.configure(bg="white")

    self.app = app

    NORMALFONT = app.styles.get("NORMALFONT")
    LARGEFONT = app.styles.get("LARGEFONT")
    MIDDLEFONT = app.styles.get("MIDDLEFONT")

    pil_image = Image.open("src\img\icons8-logo-250.png")
    ctk_image = ctk.CTkImage(pil_image)
    self.labelTitle = ctk.CTkLabel(master=self, text = "High Tech Old Factory Street", font = LARGEFONT, compound="left", image=ctk_image)
    self.labelTitle.place(relx=0.05, rely=0.1, anchor=tk.W)

    self.labelSoftWareName = ctk.CTkLabel(master=self, text = "Housing Price", font = ("Arial", 50))
    self.labelSoftWareName.place(relx=0.25, rely=0.3, anchor=tk.CENTER)

    self.labelSoftWareName = ctk.CTkLabel(master=self, text = "Prediction", font = ("Arial", 50))
    self.labelSoftWareName.place(relx=0.205, rely=0.38, anchor=tk.CENTER)
    
    # self.buttonStart = ctk.CTkButton(master=self, text="Start", command= lambda : self.proceed(),fg_color="white",text_color="black", shadow=True)
    # self.buttonStart.place(relx=0.2, rely=0.8, anchor=tk.SW)
    style = ThemedStyle()

    style.theme_use('default')
    style.configure("Shadow.TButton", font=("Arial", 12), background="white", foreground="black", relief="raised", borderwidth=3, lightcolor="white", darkcolor="gray", bordercolor="black", shadow=True, borderradius=30)
    self.buttonStart = ttk.Button(master=self, text="Start", command=self.proceed, style="Shadow.TButton")
    self.buttonStart.place(relx=0.12, rely=0.75, anchor=tk.SW)
    style = ttk.Style()
    style.configure("Shadow.TButton", padding=10) 

    self.labelSlogan = ctk.CTkLabel(master=self, text = "High Quality Forecast", font = ("Arial", 30))
    self.labelSlogan.place(relx=0.24, rely=0.55, anchor=tk.CENTER)

    self.Image = ctk.CTkImage(light_image=Image.open("src\img\First_page_image.png"),size=(550,400))
    self.labelImage = ctk.CTkLabel(master=self,text="",image=self.Image)
    self.labelImage.place(relx=0.96,rely=0.8,anchor = tk.SE)