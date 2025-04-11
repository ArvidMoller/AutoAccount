import glob
import pickle
import shap
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("predict.csv")

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

def label_decode(num, le_dict, column):
    le = le_dict[column]
    rNum = le.inverse_transform(num)

    return rNum

def feature_importance(model, df):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(df)

    shap.summary_plot(shap_values, df, plot_type = "bar", class_names=["4111", "4222", "4333", "4444", "4555"])

file_num = int((len(glob.glob("models/*.pkl"))/2)-1)

user_input = input(f"Load which model (0-{file_num}) \n")
while not user_input.isnumeric() or int(user_input) > file_num:
    user_input = input(f"Load which model (0-{file_num}) \n")

model_path = f"models/model{int(user_input)}.pkl"
info_path = f"models/modelInfo{int(user_input)}.pkl"

model = pickle.load(open(model_path, "rb"))
le_dict = pickle.load(open(info_path, "rb"))

target = "account"

if "created_at" in df.columns and not df["created_at"].isna().all():
    df = to_dateTime(df, "created_at")
else:
    df = df.drop(columns="created_at")

pred_df = label_encode(df, le_dict)
pred_df = df.drop(columns=target)

pred_df.to_csv("predTest.csv")

pred = label_decode(model.predict(pred_df), le_dict, target)
print(f"Account: {pred}")

feature_importance(model, pred_df)