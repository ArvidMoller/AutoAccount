import glob
import pickle
import pandas as pd
import xgboost as xgb 

df = pd.read_csv("predict.csv")

def label_encode(df, target_label):
    le_dict = {}

    for column in df:
        if df[column].dtypes == object or column == target_label:           
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])
            le_dict[column] = le

    return df, le_dict

file_num = int((len(glob.glob("models/*.pkl"))/2)-1)

user_input = input(f"Load which model (0-{file_num}) \n")
while not user_input.isnumeric() or int(user_input) > file_num:
    user_input = input(f"Load which model (0-{file_num}) \n")

model_path = f"models/model{int(user_input)}.pkl"
info_path = f"models/modelInfo{int(user_input)}.pkl"

model = pickle.load(open(model_path, "rb"))
le_dict = pickle.load(open(info_path, "rb"))



# pred = model.predict(df)