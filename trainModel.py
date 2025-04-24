# File: trainModel.py
# Author: Arvid Möller
# Date: 2025-04-24
# Description: This program trains a extreme gradient boost (XGB) classifier model on data (saved in a .csv document) from invoices to be able to predict from which account the invoice drew money. The model and model info is then saved to pickle (.pkl) files named model[number].pkl and modelInfo[number].pkl respectivly, for later use. The following features are required in the training data: supplier, amount, department, account, cost_center, project_id, personnel, reference, tax_percentage, city, created_at, category. Target: account.
# Required files: void
# Required modules: os, glob, pickle, shap, numpy, pandas, xgboost, sklearn


import os
import glob
import pickle
import numpy as np # type: ignore
import pandas as pd # type: ignore
import xgboost as xgb # type: ignore
from sklearn import metrics # type: ignore
from sklearn.preprocessing import LabelEncoder # type: ignore
from sklearn.model_selection import train_test_split # type: ignore


# 
# 
# Paramiters: 
# 
# 
# Returns: 

# This function asks the user to choose a dataset to train the model on through a input loop. Only awnser that exists as .csv files in the dataset folder are accepted. 
# 
# Paramiters: void
# 
# Returns: The path to the choosen dataset.
def choose_dataset():
    user_input = input("Load which dataset (.csv)? \n")
    os.chdir(f"{os.getcwd()}/dataset")
    acceptedInput = glob.glob("*.csv")
    os.chdir("..")
    
    while not user_input in acceptedInput:
        user_input = input("Load which dataset? \n")

    return f"dataset/{user_input}"


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

# Label encodes all objects in the dataframe using scikit-learns label encoder by looping through all columns.
# 
# Paramiters:
# df: The dataframe to encode
# target_label: The feature name of the target column. Since targets must be numbers staring from 1, target_label is used to ensure that the target column gets encoded.
# 
# Return: 
# - df: The dataframe all objects encoded.
# - le_dict: A dictionary containing all label encoders used to encode the dataframe. 
def label_encode(df, target_label):
    le_dict = {}

    for column in df:
        if df[column].dtypes == object or column == target_label:           
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])
            le_dict[column] = le

    return df, le_dict


# Calculates and writes out the accuracy of the model as decimal numbers (0-1) using sci-kit learns metrics. 
# 
# Paramiters: 
# - target: The name of the target column.
# - features: All columns except the target column.
# 
# Returns: void
def accuracy(target, features):
    y_true = target
    y_pred = clf.predict(features)
    y_score = clf.predict_proba(features)
    y_true.shape, y_pred.shape, y_score.shape

    metrics.accuracy_score(y_true, y_pred)
    print(metrics.classification_report(y_true, y_pred))


# Asks the user if the model should be saved using a input loop. If so, the model and model info (the label encodning dictionary) is saved as separate pickle (.pkl) files named model[number].pkl and modelInfo[number].pkl. The number is determined by the number of other pickle files in the models folder. numbering starts at 0. 
# 
# Paramiters: 
# 
# 
# Returns: 
def save_model(clf, dict):
    user_input = input("Save model as .pkl? (y/n) \n")
    acceptedInput = ["y", "n"]
    while not user_input in acceptedInput:
        user_input = input("Save model as .pkl? (y/n) \n")

    if user_input == "n":
        return
    elif not os.path.exists("models"):
        os.mkdir("models")

    file_num = int(len(glob.glob("models/*.pkl"))/2)
    pickle.dump(clf, open(f"models/model{file_num}.pkl", "wb"))
    pickle.dump(dict, open(f"models/modelInfo{file_num}.pkl", "wb"))

df = pd.read_csv(choose_dataset())
df.info()

# Define a target column
target = "account"

# Divide time to individual columns
df = to_dateTime(df, "created_at")

# Encode columns with object values to int unsing a label encoder
df, le_dict = label_encode(df, target)

# Define feautres columns
features = df.drop(columns=[target]).columns

df.to_csv("test.csv")

# Make a training df and a valid df for training
n_valid = 0.2
train_df, valid_df = train_test_split(df, test_size=n_valid, random_state=1)
train_df.shape, valid_df.shape

# Paramiters for training the model
params = {
    'tree_method': 'approx',
    'objective': 'multi:softprob',
}
num_boost_round = 2000      # How many boosting stages to preform, higher number = better performace (usually)

# Train model
clf = xgb.XGBClassifier(n_estimators=num_boost_round, **params)
clf.fit(train_df[features], train_df[target], 
        eval_set=[(train_df[features], train_df[target]), (valid_df[features], valid_df[target])], 
        verbose=2);

# Calculate accuracy
accuracy(valid_df[target], valid_df[features])

# Save model and label encoder dictionary as .pkl
save_model(clf, le_dict)