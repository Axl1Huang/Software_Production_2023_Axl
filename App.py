import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD
from Start_page import first
from Upload import second
from Enter import third
from Result import forth

class App(tk.Tk):

  ################
  # APP SETTINGS #
  ################

  name = "Hosue_prediction_by_HTOFS.Oy"                      # Name of the app
  width = 1024                             # Width of the app window
  height = 768                             # Height of the app window
  pages = [ first,second,third,forth]           # Pages of the app
  initial_page = 1                          # Initial page to show, from 1 to upwards

  # Custom styles for the app
  styles = {
    "LARGEFONT": ("Verdana", 35),
    "MIDDLEFONT": ("Verdana", 25),
    "NORMALFONT": ("Verdana", 15),
  }

  ###################
  # STATE VARIABLES #
  ###################

  # Global selected option example
  selectedFilePath = ""

  #############
  # FUNCTIONS #
  #############
  def csv_file_check_and_call_thrid_page(self, file_path, selected_columns):
      self.selectedFilePath = file_path
      self.selectedColumns = selected_columns
      print(f"CSV file uploaded: {file_path}")
      print(selected_columns)



  # Show a certain page, from 1 to upwards
  def show_page(self, page_number : int):
    self.frames.get(page_number).tkraise()
  
  # Get a certain page, from 1 to upwards
  def get_page(self, page_number : int):
    return self.frames.get(page_number)

  ######################
  # INITIALIZE THE APP #
  ######################
  def __init__(self, *args, **kwargs):
    TkinterDnD.Tk.__init__(self, *args, **kwargs)
    
    # creating a container
    container = tk.Frame(self) 
    # container.config(bg="white")
    container.pack(side = "top", fill = "both", expand = True)
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)
    self.geometry(f"{self.width}x{self.height}")
    self.title(self.name)
    self.resizable(False, False)

    # Theme settings for the app
    # https://github.com/TomSchimansky/CustomTkinter/wiki/Themes
    ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    # Create all the pages
    self.frames = {}
    i : int = 1
    for F in self.pages:
        frame = F(container, self)
        self.frames[i] = frame
        frame.grid(row = 0, column = 0, sticky ="nsew")
        i = i + 1
    # Initial page to show
    self.show_page(self.initial_page)