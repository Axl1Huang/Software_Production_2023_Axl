import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
import os
import joblib
import time
from tkinter import messagebox

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

  prediction_instance = None
  
  #############
  # FUNCTIONS #
  #############
  def update_labels(self):
    if self.prediction_instance.training_done:
        if self.prediction_instance.user_result is not None:
            self.label_result.configure(text=f"The prediction of price based on your input is: {self.prediction_instance.user_result:.2f}")
        else:
            self.label_result.configure(text="The prediction of price based on your input is not available.")
        
        if self.prediction_instance.model_acc is not None:
            self.label_Model_accuracy.configure(text=f"The accuracy of Model Accuracy based on your selected is: {self.prediction_instance.model_acc:.2f}")
        else:
            self.label_Model_accuracy.configure(text="The accuracy of the model is not available.")
        
        if self.prediction_instance.user_column is not None:
            self.label_user_column.configure(text=f"The columns you selected for training are:{self.prediction_instance.user_column}")
        else:
            self.label_user_column.configure(text="No columns selected for training.")
    else:
        self.after(1000, self.update_labels_after_training)


  def update_labels_after_training(self):
    if self.prediction_instance.training_done:
        self.update_labels()
    else:
        self.after(1000, self.update_labels_after_training)

  def back(self):
    self.app.show_page(3)

  def save_model(self):
    if self.prediction_instance and self.prediction_instance.training_done:
        model = self.prediction_instance.model
        saved_models_folder = "src/saved_model"
        if not os.path.exists(saved_models_folder):
            os.makedirs(saved_models_folder)
        timestamp = int(time.time())
        model_file_name = f"trained_model_{timestamp}.pkl"
        
        model_file_path = os.path.join(saved_models_folder, model_file_name)
        joblib.dump(model, model_file_path)
        messagebox.showinfo("Success", f"Model saved successfully at {model_file_path}")
    else:
        messagebox.showerror("Error", "There is no trained model available to save.")
  
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent)
    self.app = app
    NORMALFONT = app.styles.get("NORMALFONT")
    LARGEFONT = app.styles.get("LARGEFONT")

    self.prediction_instance = self.app.prediction_instance

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
    
    self.ButtonSave = ctk.CTkButton(master=self, text="Save Model", command=lambda: self.save_model(), fg_color="yellow", text_color="black")
    self.ButtonSave.place(relx=0.6, rely=0.8, anchor=tk.CENTER)

    self.label_result = ctk.CTkLabel(master=self, font = NORMALFONT)  
    self.label_result.place(relx=0.7, rely=0.3, anchor=tk.CENTER)

    self.label_Model_accuracy = ctk.CTkLabel(master=self, font = NORMALFONT)  
    self.label_Model_accuracy.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

    self.label_user_column = ctk.CTkLabel(master=self, font = NORMALFONT)  
    self.label_user_column.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

    self.update_labels_after_training() 