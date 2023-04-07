import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image

class third(tk.Frame):
  
  ##############
  # COMPONENTS #
  ##############

  labelTitle: ctk.CTkLabel = None
  label_upload_Area:ctk.CTkLabel = None
  label_Enter_information:ctk.CTkLabel = None
  label_Predicted_Price_Show:ctk.CTkLabel = None
  ButtonBack : ctk.CTkButton = None
  ButtonPredcition : ctk.CTkButton = None
  ZipEnter : ctk.CTkEntry = None
  HouseSizeEnter : ctk.CTkEntry = None
  AcreLotEnter : ctk.CTkEntry = None
  NumOfBedEnter : ctk.CTkEntry = None
  NumOfBathEnter : ctk.CTkEntry = None
  select_from_user = None
  #############
  # FUNCTIONS #
  #############
  def proceed(self):
    self.app.show_page(4)

  def back(self):
    self.app.show_page(2)
  def get_list_from_user(self,list):
     self.select_from_user = list
     print(self.select_from_user)
    #  print(self.selected_columns)
  def __init__(self, parent, app,selected_columns=None):
    tk.Frame.__init__(self, parent)
    self.app = app
    self.selected_columns=selected_columns or []
    NORMALFONT = app.styles.get("NORMALFONT")
    LARGEFONT = app.styles.get("LARGEFONT")


    self.labelTitle = ctk.CTkLabel(master=self, text = "Enter Information", font = LARGEFONT)
    self.labelTitle.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    self.label_upload_Area = ctk.CTkLabel(master=self, text = "Upload Area", font = NORMALFONT)
    self.label_upload_Area.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

    self.label_Enter_information = ctk.CTkLabel(master=self, text = "Enter Information", font = NORMALFONT)
    self.label_Enter_information.place(relx=0.2, rely=0.4, anchor=tk.CENTER)
    
    self.ButtonBack = ctk.CTkButton(master=self, text="Back", command= lambda : self.back(),fg_color="yellow",text_color="black")
    self.ButtonBack.place(relx=0.2, rely=0.8, anchor=tk.CENTER)

    self.label_Predicted_Price_Show = ctk.CTkLabel(master=self, text = "Predicted Price Show", font = NORMALFONT)
    self.label_Predicted_Price_Show.place(relx=0.2, rely=0.6, anchor=tk.CENTER)

    self.ButtonPredcition = ctk.CTkButton(master=self, text="Star Prediction", command= lambda : self.proceed(),fg_color="green",text_color="black")
    self.ButtonPredcition.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    ### Setting Enter Box###
    # self.ZipEnter = ctk.CTkEntry(master=self,placeholder_text="Zip_code",width=120,height=25,border_width=2,border_color="yellow",corner_radius=10)
    # self.ZipEnter.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    # self.HouseSizeEnter = ctk.CTkEntry(master=self,placeholder_text="House_Size",width=120,height=25,border_width=2,border_color="yellow",corner_radius=10)
    # self.HouseSizeEnter.place(relx=0.65, rely=0.3, anchor=tk.CENTER)

    # self.AcreLotEnter = ctk.CTkEntry(master=self,placeholder_text="Acre_Lot",width=120,height=25,border_width=2,border_color="yellow",corner_radius=10)
    # self.AcreLotEnter.place(relx=0.8, rely=0.3, anchor=tk.CENTER)

    # self.NumOfBedEnter = ctk.CTkEntry(master=self,placeholder_text="Bed_room_number",width=120,height=25,border_width=2,border_color="yellow",corner_radius=10)
    # self.NumOfBedEnter.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

    # self.NumOfBathEnter = ctk.CTkEntry(master=self,placeholder_text="Bath_room_number",width=120,height=25,border_width=2,border_color="yellow",corner_radius=10)
    # self.NumOfBathEnter.place(relx=0.6, rely=0.5, anchor=tk.CENTER)
  def create_entry_boxes(self):
      entry_box_specs = {
          "zip_code": (0.5, 0.3),
          "house_size": (0.65, 0.3),
          "acre_lot": (0.8, 0.3),
          "bed": (0.75, 0.5),
          "bath": (0.6, 0.5),
      }

      self.entry_boxes = {}
      for column in self.selected_columns:
          if column in entry_box_specs:
              x, y = entry_box_specs[column]
              entry_box = ctk.CTkEntry(
                  master=self,
                  placeholder_text=column,
                  width=120,
                  height=25,
                  border_width=2,
                  border_color="yellow",
                  corner_radius=10,
              )
              entry_box.place(relx=x, rely=y, anchor=tk.CENTER)
              self.entry_boxes[column] = entry_box