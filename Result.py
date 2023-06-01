import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
import os
import joblib
import time
from tkinter import messagebox
from tkinter import Tk, Label, Canvas, PhotoImage

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
                result_text = f"{self.prediction_instance.user_result:.2f}"
                self.label_result.configure(text=result_text, font = ("Courier New", 20))
            else:
                self.label_result.configure(text="The prediction of price based on your input is not available.")
        
            if self.prediction_instance.model_acc is not None:
                self.label_Model_accuracy.configure(text=f"{self.prediction_instance.model_acc*100:.0f}%", font=("Courier New", 16))
            else:
                self.label_Model_accuracy.configure(text="The accuracy of the model is not available.")
        
            if self.prediction_instance.user_column is not None:
                self.label_user_column.configure(text=f"The columns you selected are:\n{self.prediction_instance.user_column}")
            else:
                self.label_user_column.configure(text="No columns selected for training.")
        else:
            self.after(1000, self.update_labels)

  def back(self):
    self.app.reset_page(4)
    self.app.show_page(3)

  def save_model(self):
    if self.prediction_instance and self.prediction_instance.training_done:
        model = self.prediction_instance.model
        selected_columns = self.app.shared_data['selected_columns']  # Directly access 'selected_columns' from shared_data
        uploaded_file_path = self.app.shared_data.get("uploaded_file_path")
        target_column = self.app.shared_data["target_column"]
        print(target_column)
        saved_models_folder = "src/saved_model"
        if not os.path.exists(saved_models_folder):
            os.makedirs(saved_models_folder)
        timestamp = int(time.time())
        model_file_name = f"trained_model_{timestamp}.pkl"
        
        model_file_path = os.path.join(saved_models_folder, model_file_name)
        
        model_data = {
            'model': model,
            'selected_columns': selected_columns,
            'uploaded_file_path':uploaded_file_path,
            "target_column":target_column
        }
        
        joblib.dump(model_data, model_file_path)
        messagebox.showinfo("Success", f"Model saved successfully at {model_file_path}")
        print(self.app.shared_data)
    else:
        messagebox.showerror("Error", "There is no trained model available to save.")
  def reset(self):
        self.prediction_instance.model_acc = None
        self.prediction_instance.user_column = None
        self.prediction_instance.user_result = None
        self.prediction_instance.training_done = False  
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent)
    self.configure(bg="white")
    self.app = app
    NORMALFONT = app.styles.get("NORMALFONT")
    LARGEFONT = app.styles.get("LARGEFONT")

    self.prediction_instance = self.app.prediction_instance

    self.labelTitle = ctk.CTkLabel(master=self, text = "Predicted Price Show", font = LARGEFONT)
    self.labelTitle.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    pil_image = Image.open("src\img\icons8-home-24.png")
    ctk_image = ctk.CTkImage(pil_image)
    self.label_upload_Area = ctk.CTkLabel(master=self, text="Home Page", font=NORMALFONT, compound="left", image=ctk_image)
    self.label_upload_Area.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

    pil_image = Image.open("src\img\icons8-upload-24.png")
    ctk_image = ctk.CTkImage(pil_image)
    self.label_upload_Area = ctk.CTkLabel(master=self, text="Upload Area", font=NORMALFONT, compound="left", image=ctk_image)
    self.label_upload_Area.place(relx=0.2, rely=0.33, anchor=tk.CENTER)

    pil_image = Image.open("src\img\icons8-enter-24 (1).png")
    ctk_image = ctk.CTkImage(pil_image)
    self.label_Enter_information = ctk.CTkLabel(master=self, text="Enter Information", font=NORMALFONT, compound="left", image=ctk_image)
    self.label_Enter_information.place(relx=0.22, rely=0.46, anchor=tk.CENTER)

    pil_image = Image.open("src\img\icons8-eye-32.png")
    ctk_image = ctk.CTkImage(pil_image)
    self.label_Predicted_Price_Show = ctk.CTkLabel(master=self, text="Predicted Price Show", font=NORMALFONT, compound="left", image=ctk_image)
    self.label_Predicted_Price_Show.place(relx=0.23, rely=0.59, anchor=tk.CENTER)

    pil_image = Image.open("src\img\icons8-back-24.png")
    ctk_image = ctk.CTkImage(pil_image)
    self.ButtonBack = ctk.CTkButton(master=self, text="Back", command= lambda : self.back(), fg_color="light yellow", text_color="black", compound="left", image=ctk_image)
    self.ButtonBack.place(relx=0.2, rely=0.75, anchor=tk.CENTER)
    
    self.ButtonSave = ctk.CTkButton(master=self, text="Save Model", command=lambda: self.save_model(), fg_color="#D6DFE8", text_color="black")
    self.ButtonSave.place(relx=0.64, rely=0.81, anchor=tk.CENTER)

    # blue_box = tk.Frame(self, bg="#91E9FD", width=350, height=350)
    # blue_box.place(relx=0.65, rely=0.4, anchor=tk.CENTER)
    # blue_box_text = ctk.CTkLabel(master=blue_box, text="The prediction of price is", command= ("Arial", 20))
    # blue_box_text(relx=0.66, rely=0.43, anchor=tk.CENTER)
    # small_blue_box = tk.Frame(self, bg="#C2EFFA", width=200, height=200)
    # small_blue_box.place(relx=0.7, rely=0.55, anchor=tk.CENTER)

    blue_box = tk.Frame(self, bg="#91E9FD", width=350, height=350,borderwidth=10, relief=tk.RAISED)
    blue_box.place(relx=0.65, rely=0.4, anchor=tk.CENTER)
    self.biue_box_text = tk.Label(blue_box, text="Predicted Price and Accuracy:", bg="#91E9FD", fg="white", font = ("Arial", 15))
    self.biue_box_text.place(x=35, y=45)
    small_blue_box = tk.Frame(self, bg="#C2EFFA", width=200, height=200)
    small_blue_box.place(relx=0.65, rely=0.45, anchor=tk.CENTER)
    # self.canvas = Canvas(self, width=200, height=200, bg="#C2EFFA", highlightthickness=0)
    # self.canvas.place(x=60, y=60)
    self.label_result = ctk.CTkLabel(master=small_blue_box, font = NORMALFONT)  
    self.label_result.place(relx=0.52, rely=0.45, anchor=tk.CENTER)

    self.label_Model_accuracy = ctk.CTkLabel(master=small_blue_box, font = NORMALFONT)  
    self.label_Model_accuracy.place(relx=0.52, rely=0.65, anchor=tk.CENTER)

    self.label_user_column = ctk.CTkLabel(master=self, font = NORMALFONT)  
    self.label_user_column.place(relx=0.64, rely=0.71, anchor=tk.CENTER)

    self.prediction_instance = self.app.prediction_instance
    self.prediction_instance.forth_instance = self

    self.update_labels()