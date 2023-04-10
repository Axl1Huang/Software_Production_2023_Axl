import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from prediction import prediction
import threading
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
  button_done: ctk.CTkButton = None
  #############
  # FUNCTIONS #
  #############
  def proceed(self):
    input_values = self.get_input_values()
    print(f"input_value:", input_values)
    def update_forth_page(accuracy, user_pred,user_column):
        forth_instance = self.app.get_page(4)
        forth_instance.model_acc = accuracy
        forth_instance.user_result = user_pred
        forth_instance.user_column = user_column
        forth_instance.update_labels()
     # Find the forth instance in app.pages
    pred = prediction(input_values, self.select_from_user,self.app,update_forth_page)
    pred.get_test_and_train_data()
    self.alert_window = tk.Toplevel(self)
    self.alert_window.title("Training in progress")
    self.alert_label = ttk.Label(self.alert_window, text="Waiting for training to finish...")
    self.alert_label.pack(padx=20, pady=20)

    # Set the initial size of the alert window
    self.alert_window.geometry("300x150")

    # Center the alert window on the screen
    self.alert_window.update_idletasks()
    width = self.alert_window.winfo_width()
    height = self.alert_window.winfo_height()
    x = (self.alert_window.winfo_screenwidth() // 2) - (width // 2)
    y = (self.alert_window.winfo_screenheight() // 2) - (height // 2)
    self.alert_window.geometry(f"{width}x{height}+{x}+{y}")

    # Disable user interaction with the main window and restrict closing the alert window
    self.alert_window.grab_set()
    self.alert_window.protocol("WM_DELETE_WINDOW", lambda: None)
    self.alert_window.transient(self.app)

    # Run training in a separate thread
    training_thread = threading.Thread(target=pred.traning, daemon=True)
    training_thread.start()

    # Check training status periodically
    self.check_training_status(pred)
  def back(self):
    self.reset_page()
    self.app.show_page(2)
  def reset_page(self):
    self.remove_entry_boxes()
    self.selected_columns = []
  def get_list_from_user(self,list):
     self.select_from_user = list
     print("check list: "+self.select_from_user)
  def remove_entry_boxes(self):
      for column, entry_box in self.entry_boxes.items():
        entry_box.destroy()
      self.entry_boxes.clear()
  def get_input_values(self):
      input_values = {}
      for column, entry_box in self.entry_boxes.items():
          input_values[column] = entry_box.get()
      return input_values
  def check_training_status(self, pred_instance):
    if not pred_instance.training_done:
        self.after(100, self.check_training_status, pred_instance)  # Check again in 100ms
    else:
        self.alert_label.config(text="Training Finished!")
        self.button_done = ctk.CTkButton(master=self.alert_window, text="Done", command=self.on_done_button_click, fg_color="green", text_color="black")
        self.button_done.pack(padx=20, pady=20)
  def on_done_button_click(self):
    self.button_done.destroy()
    self.alert_window.destroy()
    self.alert_window.grab_release()
    self.app.show_page(4)
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
      third.select_from_user = self.selected_columns