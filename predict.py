# File: predict.py
# Author: Arvid Möller
# Date: 2025-04-24
# Description: This program pedicts the account from which a invoice drew money from based on info from the invoice (supplier, amount, department, account, cost_center, project_id, personnel, reference, tax_percentage, city, created_at, category) using a machine learning . 
# Required files: model[number].pkl, modelInfo[number].pkl
# Required modules: glob, pickle, shap, numpy, pandas, matplotlib

import glob
import pickle
import shap # type: ignore
import numpy as np # type: ignore
import pandas as pd # type: ignore
# from flask import Flask # type: ignore
import matplotlib.pyplot as plt # type: ignore


# Changes the format of time from YY:MM:DD HH:MM to individuall cells in the dataframe.
# 
# Paramiters: 
# - df: The dataframe in which the datetime is stored
# - col: What column the datetime is in.
# 
# Returns: The dataframe with Y, M, D, H and M in sperarate columns.  
def to_dateTime(df, col):
    time = ["year", "month", "day", "hour", "minute"]

    df[col] = pd.to_datetime(df[col], errors="coerce")
    
    for i in time:
        try:  
            df[f"created_at_{i}"] = getattr(df[col].dt, i)
        except:
            print(f"{i} is missing")

    df = df.drop(columns=[col])

    return df


# Label encodes all objects in the dataframe using scikit-learns label encoder by looping through all columns. The labels are the same as in trainModel.py.
# 
# Paramiters:
# df: The dataframe to encode
# le_dict: A dictionary containing the label encoders used in trainModel.py. The encoders are loaded for each column. 
# 
# Return: The dataframe all objects encoded.
def label_encode(df, le_dict):
    cols_to_drop = []

    for column in df:
        if df[column].dtypes == object:
            try:
                le = le_dict[column]
                df[column] = le.transform(df[column])
            except Exception as e:
                print(f"Column {e} wasn't able to be encoded. Column was dropped.")
                cols_to_drop.append(column)

    if cols_to_drop:
        df = df.drop(columns=[cols_to_drop])

    return df


# Makes the prediction using xgboost built in prediction function, decodes it, prints it out in the terminal and then makes a feature importence graph using feature_importance function. 
#
# Paramiters: 
# model: The model.
# pred_df: The preprocessed dataframe with the values the prediction is based on.
# le_dict:  A dictionary containing the label encoders used in trainModel.py.
# target: The target column.
#
# Returns: void
def make_prediction(model, pred_df, le_dict, target):
    # Make a prediction with loaded model
    pred = model.predict(pred_df)

    # Decode predicted value and print in terminal
    pred_decoded = label_decode(pred, le_dict, target)
    print(f"Account: {pred_decoded}")

    # Make a bar chart for feature importence
    feature_importance(model, pred_df, pred, 1)

# Decodes a values that has previously been label encoded using the label_encode.
# 
# Paramiters:
# num: The value to decode.
# le_dict: A dictionary containing the label encoders used in trainModel.py.
# column: The column in the dataframe num is in. 
# 
# Returns: The decoded num.
def label_decode(num, le_dict, column):
    le = le_dict[column]
    rNum = le.inverse_transform(num)

    return rNum


# Creates a feature importence graph using SHAP and saves it as a image so it can be displayed in the next.js app. Positive SHAP-value in graph means feature increased probability of predicted class. Negative SHAP-value in graph means feature decreased probability of predicted class. 
# 
# Paramiters:
# model: The model loaded from the pickle file.
# df: The dataframe with the data the prediction was based on.
# pred: The predicted value.
# predicted_rows: Number of predicted rows. 
#
# Returns: void
def feature_importance(model, df, pred, predicted_rows):
    # Configure SHAP
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(df)

    # Get index of predicted class in list of classes
    class_index = pred[0]

    # Get SHAP-data for the predicted class
    shap_vals_instance_class = shap_values[predicted_rows-1, :, class_index]

    # Create explain-object for SHAP
    predExplainer = shap.Explanation(
        values=shap_vals_instance_class,
        base_values=explainer.expected_value[class_index],
        feature_names=["Supplier", "Amount", "Department", "Cost Center", "Project ID", "Personnel", "Reference", "Tax Procentage", "City", "Category", "Year Issued", "Month Issued", "Day Issued", "Hour Issued", "Minute Issued"]
    )

    # Create graph
    shap.plots.bar(predExplainer, show=False)
    # Save as .png
    plt.savefig("xgb_front/public/shap_bar.png", bbox_inches='tight')
    plt.close()


# Load dataframe with input data
df = pd.read_csv("predict.csv")

# Get number of model files (from 0) in /models
file_num = int((len(glob.glob("models/*.pkl"))/2)-1)

# Input loop for choosing a model to use
user_input = input(f"Load which model (0-{file_num}) \n")
while not user_input.isnumeric() or int(user_input) > file_num:
    user_input = input(f"Load which model (0-{file_num}) \n")

# Get model and model info path
model_path = f"models/model{int(user_input)}.pkl"
info_path = f"models/modelInfo{int(user_input)}.pkl"

# Load model and model info
model = pickle.load(open(model_path, "rb"))
le_dict = pickle.load(open(info_path, "rb"))

# Define target
target = "account"

# Convert "created_at" from YY:MM:DD HH:MM to separate columns if "created_at" has a value. Else, remove "created_at" column. 
if "created_at" in df.columns and not df["created_at"].isna().all():
    df = to_dateTime(df, "created_at")
else:
    df = df.drop(columns="created_at")

# Encode input dataframe with the same encoder as the training data and remove the target column
pred_df = label_encode(df, le_dict)
pred_df = df.drop(columns=target)

# Save predared dataframe to .csv for debugging
pred_df.to_csv("predTest.csv")

make_prediction(model, pred_df, le_dict, target)