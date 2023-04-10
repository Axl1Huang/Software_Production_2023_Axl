import tkinter as tk
from tkinter import filedialog
import pandas as pd
import DDbox
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from Result import forth
class prediction():
    Model_acc = None
    User_result = None
    user_select_column = None
    def __init__(self,user_input,user_select_column,app,callback):
        self.user_input = user_input
        self.user_select_column = user_select_column
        self.app = app
        self.callback = callback
        self.training_done = False
    def get_test_and_train_data(self):
        forth.user_column = self.user_select_column
        self.test_data = pd.DataFrame([self.user_input])
        self.train_data = self.user_select_column
        print(self.test_data)
        print("train data: ",self.train_data)
    def traning(self):
        data = pd.read_csv("src/basic_data/house_zipcode_usa.csv")
        data = data[self.train_data]
        data = self.clean_data(data)
        X = data.drop(columns=["price"])
        Y = data["price"]
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
        print(X_train)
        print(X_test)
        model = RandomForestRegressor(n_estimators=200, max_depth=30, min_samples_split=10, min_samples_leaf=2, max_features=0.9, max_samples=0.9, bootstrap=True, random_state=52)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = r2_score(y_test,y_pred)
        user_pred = model.predict(self.test_data)
        self.callback(accuracy, user_pred,self.train_data)
        # print(prediction.Model_acc,prediction.User_result)
        self.training_done = True  # Set this attribute to True when the training is finished
    def clean_data(self,data):
        z_scores = np.abs((data - data.mean()) / data.std())
        threshold = 12
        outliers = z_scores > threshold
        data = data[~outliers.any(axis=1)]
        return data
    # def give_result(self):
    #     print(prediction.Model_acc,prediction.User_result,prediction.user_select_column)
    #     return prediction.Model_acc,prediction.User_result,prediction.user_select_column
    # def trainning_data(self):
if __name__ == "__main__":
    pred_instance = prediction(None, None)  # Create an instance of the prediction class
    pred_instance.traning()  # Call the traning method on the instance