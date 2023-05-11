import os
import pandas as pd
import numpy as np
from joblib import dump, load
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import tkinter as tk
from tkinter import ttk
import joblib

class prediction():
    def __init__(self, app, user_input=None, user_select_column=None, uploaded_file_path=None, forth_instance=None):
        self.app = app
        self.user_input = user_input if user_input is not None else {}
        self.user_select_column = user_select_column if user_select_column is not None else []
        self.uploaded_file_path = uploaded_file_path if uploaded_file_path is not None else ""
        self.forth_instance = forth_instance
        self.training_done = False
        self.model = None
        self.model_input_columns = []
        self.user_result = None
        self.model_acc = None  # Model accuracy
        self.user_column = None  # User selected columns

    def get_test_and_train_data(self):
        if not self.user_input:
            print("User input is empty.")
            return
        self.test_data = pd.DataFrame([self.user_input])
        self.train_data = self.user_select_column

    def training(self):
        if not self.app.shared_data.get("uploaded_file_path"):
            tk.messagebox.showerror(title="Error", message="Please upload a CSV file before starting the training.")
            return

        file_path = self.app.shared_data.get("uploaded_file_path")
        print(f"Training with file: {file_path}")

        data = pd.read_csv(file_path)

        # Add the selected columns from app.shared_data
        selected_columns = self.app.shared_data.get("selected_columns", [])
        data = data[selected_columns]

        X = data.drop(columns=["price"])
        y = data["price"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        self.model = RandomForestRegressor(n_estimators=200, max_depth=30, min_samples_split=10, min_samples_leaf=2, max_features=0.9, max_samples=0.9, bootstrap=True, random_state=52)
        self.model.fit(X_train, y_train)

        # Get model accuracy using r2_score
        y_pred = self.model.predict(X_test)
        self.model_acc = r2_score(y_test, y_pred)

        # Set user_column to the selected columns
        self.user_column = selected_columns

        self.get_test_and_train_data()
        print(f"test_data: {self.test_data}")
        if self.test_data.empty:
            print("Test data is empty. Skipping prediction.")
            return
        user_pred = self.model.predict(self.test_data)
        self.user_result = user_pred[0] if len(user_pred) > 0 else None
        self.training_done = True
        if self.forth_instance:
            self.forth_instance.update_labels()

    def save_model(self, file_path='trained_model.joblib'):
        model_data = {
            'model': self.model,
            'selected_columns': self.user_select_column
        }
        dump(model_data, file_path)


    def load_model(self, model_path):
        loaded_model_data = joblib.load(model_path)
        if isinstance(loaded_model_data, dict) and 'model' in loaded_model_data and 'selected_columns' in loaded_model_data:
            self.model = loaded_model_data['model']
            self.user_select_column = loaded_model_data['selected_columns']
        else:
            raise TypeError("The loaded model data should be a dictionary containing a 'model' and 'selected_columns' keys.")


if __name__ == "__main__":
    pred_instance = prediction()  # Create an instance of the Prediction class
    pred_instance.training()