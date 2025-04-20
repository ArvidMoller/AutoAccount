import os
import glob
import pickle
import numpy as np # type: ignore
import pandas as pd # type: ignore
import xgboost as xgb # type: ignore
from sklearn import metrics # type: ignore
from sklearn.preprocessing import LabelEncoder # type: ignore
from sklearn.model_selection import train_test_split # type: ignore


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

def label_encode(df, target_label):
    le_dict = {}

    for column in df:
        if df[column].dtypes == object or column == target_label:           
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])
            le_dict[column] = le

    return df, le_dict

def accuracy(target, features):
    y_true = target
    y_pred = clf.predict(features)
    y_score = clf.predict_proba(features)
    y_true.shape, y_pred.shape, y_score.shape

    metrics.accuracy_score(y_true, y_pred)
    print(metrics.classification_report(y_true, y_pred))

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

df = pd.read_csv("training_data.csv")


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