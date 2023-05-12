import customtkinter as ctk
from prediction import prediction
import threading
import tkinter as tk
from tkinter import ttk


class third(tk.Frame):
    label_upload_Area:ctk.CTkLabel = None
    label_Enter_information:ctk.CTkLabel = None
    label_Predicted_Price_Show:ctk.CTkLabel = None
    labelTitle: ctk.CTkLabel = None
    def configure_shared_data(self, shared_data):
        self.user_select_column = shared_data.get("selected_columns", [])
        if self.user_select_column:
            self.create_entry_boxes()
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent)
        self.app = app
        self.entry_boxes = {}
        self.user_select_column = self.app.shared_data["selected_columns"]
        print(self.app.shared_data)
        LARGEFONT = app.styles.get("LARGEFONT")
        NORMALFONT = app.styles.get("NORMALFONT")
        self.labelTitle = ctk.CTkLabel(master=self, text="Enter Information", font=LARGEFONT)
        self.labelTitle.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.ButtonBack = ctk.CTkButton(master=self, text="Back", command=lambda: self.back(), fg_color="yellow",
                                        text_color="black")
        self.ButtonBack.place(relx=0.2, rely=0.8, anchor=tk.CENTER)

        self.ButtonPredcition = ctk.CTkButton(master=self, text="Star Prediction", command=lambda: self.proceed(),
                                              fg_color="green", text_color="black")
        self.ButtonPredcition.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        self.label_upload_Area = ctk.CTkLabel(master=self, text = "Upload Area", font = NORMALFONT)
        self.label_upload_Area.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

        self.label_Enter_information = ctk.CTkLabel(master=self, text = "Enter Information", font = NORMALFONT)
        self.label_Enter_information.place(relx=0.2, rely=0.4, anchor=tk.CENTER)

        self.label_Predicted_Price_Show = ctk.CTkLabel(master=self, text="Predicted Price Show", font=NORMALFONT)
        self.label_Predicted_Price_Show.place(relx=0.2, rely=0.6, anchor=tk.CENTER)


        if self.user_select_column:
            self.create_entry_boxes()

    def back(self):
        self.reset_page()
        self.app.reset_page(2)
        self.app.show_page(2)

    def reset_page(self):
        self.remove_entry_boxes()
        self.user_select_column = []

    def remove_entry_boxes(self):
        for column, entry_box in self.entry_boxes.items():
            entry_box.destroy()
        self.entry_boxes.clear()

    def create_entry_boxes(self):
        selected_columns = self.user_select_column
        self.entry_boxes = {}
        entry_box_specs = {
            "zip_code": (0.5, 0.3),
            "house_size": (0.65, 0.3),
            "acre_lot": (0.8, 0.3),
            "bed": (0.75, 0.5),
            "bath": (0.6, 0.5),
        }

        for index, column in enumerate(selected_columns):
            if column.lower() == "price":  
                continue

            if column in entry_box_specs:
                x, y = entry_box_specs[column]
            else:
                y = 0.3 + index * 0.1
                x = 0.5

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

    def get_input_values(self):
        input_values = {}
        for column, entry_box in self.entry_boxes.items():
            input_values[column] = entry_box.get()
        return input_values

    def validate_input_values(self, input_values):
        for column, value in input_values.items():
            try:
                float(value)
            except ValueError:
                return False
        return True


    def show_error_dialog(self, message):
        error_dialog = tk.messagebox.showerror("Error", message)

    def clear_entry_boxes(self):
        for column, entry_box in self.entry_boxes.items():
            entry_box.delete(0, tk.END)
    def show_alert_window(self):
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

    def run_training_and_close_alert(self, pred_instance):
        self.app.prediction_instance.training()
        self.alert_window.destroy()
        self.app.show_page(4)

    def proceed(self):
        input_values = self.get_input_values()
        if not self.validate_input_values(input_values):
            self.show_error_dialog("Please enter valid numeric values for all input fields.")
            self.clear_entry_boxes()
            return

        self.app.prediction_instance.user_input = input_values  # Set user_input in the Prediction instance

        if self.app.frames[2].drag_and_drop_widget.path or self.app.frames[2].file_browser.get_selected_file_path():
            self.uploaded_file_path = self.app.frames[2].drag_and_drop_widget.path
            self.model_file_path = self.app.frames[2].file_browser.get_selected_file_path()

            # Get the selected columns from the FileBrowserWidget
            selected_columns = self.app.frames[2].file_browser.get_selected_columns()

            # Assign the required values for prediction instance
            self.app.prediction_instance.selected_columns = selected_columns
            self.app.prediction_instance.uploaded_file_path = self.uploaded_file_path
            self.app.prediction_instance.model_file_path = self.model_file_path

            if hasattr(self.app, 'selected_model_path') and self.app.selected_model_path:
                self.app.prediction_instance.load_model(self.app.selected_model_path)

            self.show_alert_window()

            # Run training in a separate thread
            training_thread = threading.Thread(target=self.run_training_and_close_alert, args=(self.app.prediction_instance,), daemon=True)
            training_thread.start()
        else:
            messagebox.showerror("Error", "Please Drag a csv file or selected trained model.")
