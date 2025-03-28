import glob
import xgboost as xgb 

file_num = len(glob.glob("../models/*.json", recursive=True))

user_input = input(f"Load which model (0-{file_num}) \n")
while not user_input.isnumeric() or int(user_input) > file_num:
    user_input = input(f"Load which model (0-{file_num}) \n")

path = f"../models/model{int(user_input)}.json"
print(path)

loaded_model = xgb.XGBClassifier()
loaded_model.load_model(path)