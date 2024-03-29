import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
class Page1(tk.Frame):
  
  ##############
  # COMPONENTS #
  ##############

  labelTitle1 : ctk.CTkLabel = None
  labelTitleDescription : ctk.CTkLabel = None
  labelSelectedFile : ctk.CTkLabel = None
  buttonSelectFile : ctk.CTkButton = None
  buttonStart : ctk.CTkButton = None
  Image:ctk.CTkImage = None
  # labelDragBox : ctk.CTkLabel = None

  ###################
  # STATE VARIABLES #
  ###################

  #############
  # FUNCTIONS #
  #############

  def selectFile(self):
    # Example of how to open a file dialog and get the selected file path
    self.app.selectedFilePath = ctk.filedialog.askopenfile(title="Open File", filetypes=(("Open a .csv file", "*.csv"), ("All files", "*.*"))).name
    # Example of how to update text for a label
    self.labelSelectedFile.configure(text = f"We have selected a file: {self.app.selectedFilePath}")
  
  def proceed(self):
    # Here you could now validate the file and then add any state variables to the app which page 2 or other pages can then access
    # Like this: self.app.someThing = "someValue"
    # Then in the page 2, you could access self.app.someThing and it would contain that same value

    # Example of how to switch pages
    self.app.show_page(2)
  # def handleDrop(self):

  #######################
  # INITIALIZE THE PAGE #
  #######################
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent)
    self.app = app

    NORMALFONT = app.styles.get("NORMALFONT")
    LARGEFONT = app.styles.get("LARGEFONT")
    
    # Label for title
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
    self.labelTitle1 = ctk.CTkLabel(master=self, text="Example Page 1", font = LARGEFONT)
    self.labelTitle1.place(relx=0.5, rely=0.07, anchor=tk.CENTER)

    # Label for description
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
    self.labelTitleDescription = ctk.CTkLabel(master=self, font = LARGEFONT, text="High Tech Old Factory Street")
    self.labelTitleDescription.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    # Label for selected file
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
    self.selectedFilePath = ctk.CTkLabel(master=self, text = "Drop Csv File here", font = NORMALFONT)
    self.selectedFilePath.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    # Button to select a file, calls the selectFile function inside this class
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkButton
    self.buttonSelectFile = ctk.CTkButton(master=self, text="Select File", command = lambda : self.selectFile())
    self.buttonSelectFile.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    # Button to continue to the next page, calls the proceed function inside this class
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkButton
    self.buttonStart = ctk.CTkButton(master=self, text="Start", command= lambda : self.proceed(),fg_color="white",text_color="black")
    self.buttonStart.place(relx=0.2, rely=0.8, anchor=tk.SW)
