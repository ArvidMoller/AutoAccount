import glob
import pickle
import shap # type: ignore
import numpy as np # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

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

# + in graph: Feature that increases probability of predicted class
# - in graph: Feature that decreases probability of predicted class
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
    # Spara som .png
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

# Convert "created_at" from YY:MM:DD:HH:MM to separate columns if "created_at" has a value. Else, remove "created_at" column. 
if "created_at" in df.columns and not df["created_at"].isna().all():
    df = to_dateTime(df, "created_at")
else:
    df = df.drop(columns="created_at")

# Encode input dataframe with the same encoder as the training data and remove the target column
pred_df = label_encode(df, le_dict)
pred_df = df.drop(columns=target)

# Save predared dataframe to .csv for debugging
pred_df.to_csv("predTest.csv")

# Make a prediction with loaded model
pred = model.predict(pred_df)

# Decode predicted value and print in terminal
pred_decoded = label_decode(pred, le_dict, target)
print(f"Account: {pred_decoded}")

# Make a bar chart for feature importence
feature_importance(model, pred_df, pred, 1)