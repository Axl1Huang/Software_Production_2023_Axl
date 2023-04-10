import tkinter as tk
from tkinter import filedialog
import pandas as pd
import DDbox
class prediction():
    def __init__(self,user_input,user_select_column):
        self.user_input = user_input
        self.user_select_column = user_select_column
    def get_test_and_train_data(self):
        self.test_data = pd.DataFrame([self.user_input])
        self.train_data = self.user_select_column
        print(self.test_data)
        print("train data: ",self.train_data)
    def traning(self):
        data = pd.read_csv("src/basic_data/house_zipcode_usa.csv")
        data = data[self.train_data]
        print(data.head(5))
    # def trainning_data(self):
if __name__ == "__main__":
    pred_instance = prediction(None, None)  # Create an instance of the prediction class
    pred_instance.traning()  # Call the traning method on the instance