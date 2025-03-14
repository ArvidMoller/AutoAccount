import pandas as pd
import numpy as np
import xgboost as xgb 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def label_encode(df):
    col_arr = []

    for column in df:
        if df[column].dtypes == object:
            col_arr.append(column)

    le = LabelEncoder()
    df[col_arr] = df[col_arr].apply(le.fit_transform)

    return df

df = pd.read_csv("historical_transactions.csv")
features = df.head(0)

# Define a target column
target = df["account"]

# Encode columns with object values to int unsing a label encoder
df = label_encode(df)

# Make a training df and a valid df for training
n_valid = 40
train_df, valid_df = train_test_split(df, test_size=n_valid, random_state=1)
train_df.shape, valid_df.shape


params = {
    'tree-method': 'approx',
    'objective': 'multi:softprob',
}
num_boost_round = 10

clf = xgb.XGBClassifier(n_estimators=num_boost_round, **params)
clf.fit(train_df[features], train_df[target], 
        eval_set=[(train_df[features], train_df[target]), (valid_df[features], valid_df[target])], 
        verbose=2);

# df.to_csv("test.csv")

# train_df.info()
# valid_df.info()
# print(target)
# print(features)