import pandas as pd
import numpy as np
import xgboost as xgb 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def label_encode(df, target_label):
    le_dict = {}

    for column in df:
        if df[column].dtypes == object or column == target_label:           
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])
            le_dict[column] = le

    return df, le_dict


df = pd.read_csv("historical_transactions.csv")

# Define a target column
target = "account"
features = df.drop(columns=[target]).columns

# Encode columns with object values to int unsing a label encoder
df, le_dict = label_encode(df, target)

# Make a training df and a valid df for training
n_valid = 0.2
train_df, valid_df = train_test_split(df, test_size=n_valid, random_state=1)
train_df.shape, valid_df.shape

params = {
    'tree_method': 'approx',
    'objective': 'multi:softprob',
}
num_boost_round = 100

clf = xgb.XGBClassifier(n_estimators=num_boost_round, **params)
clf.fit(train_df[features], train_df[target], 
        eval_set=[(train_df[features], train_df[target]), (valid_df[features], valid_df[target])], 
        verbose=2);

df.to_csv("test.csv")