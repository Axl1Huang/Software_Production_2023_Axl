import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD
from Start_page import first
from Upload import second
from Enter import third
from Result import forth
from prediction import prediction
import os, joblib, time


class App(tk.Tk):

    ################
    # APP SETTINGS #
    ################

    name = "House_prediction_by_HTOFS.Oy"
    width = 1024
    height = 768
    pages = [first, second, third, forth]
    initial_page = 1

    styles = {
        "LARGEFONT": ("Verdana", 35),
        "MIDDLEFONT": ("Verdana", 25),
        "NORMALFONT": ("Verdana", 15),
    }

    ######################
    # INITIALIZE THE APP #
    ######################
    def __init__(self, *args, **kwargs):
        TkinterDnD.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.geometry(f"{self.width}x{self.height}")
        self.title(self.name)
        self.resizable(False, False)
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.frames = {}
        self.shared_data = {
            "selected_columns": None,
            "uploaded_file_path": None,
            "model_path": None
        }
        self.prediction_instance = prediction(self)
        i: int = 1
        for F in self.pages:
            frame = F(container, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            i = i + 1

        # self.prediction_instance = prediction(self)

        self.show_page(self.initial_page)

    #############
    # FUNCTIONS #
    #############

    def show_page(self, page_number: int):
        frame = self.frames.get(page_number)
        if isinstance(frame, (second, third)):
            frame.prediction_instance = self.prediction_instance
            frame.configure_shared_data(self.shared_data)
        frame.tkraise()

    def get_page(self, page_number: int):
        return self.frames.get(page_number)
    def reset_page(self, page_number):
        self.frames[page_number].reset()
    def save_model(self):
        if hasattr(self, "prediction_instance") and self.prediction_instance.training_done:
            model = self.prediction_instance.model
            saved_models_folder = "src/saved_model"
            if not os.path.exists(saved_models_folder):
                os.makedirs(saved_models_folder)

            # Generate a unique file name based on timestamp
            timestamp = int(time.time())
            model_file_name = f"trained_model_{timestamp}.pkl"

            model_file_path = os.path.join(saved_models_folder, model_file_name)
            joblib.dump(model, model_file_path)
            messagebox.showinfo("Success", f"Model saved successfully at {model_file_path}")
        else:
            messagebox.showerror("Error", "There is no trained model available to save.")


if __name__ == "__main__":
    app = App()
    app.mainloop()



