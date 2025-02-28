import pandas as pd
import numpy as np

df = pd.read_excel("testArk.xlsx", "Blad1", index_col=None, na_values=["NA"])
csv = df.to_csv("data.csv")

csvDf = pd.read_csv("historical_transactions.csv")


print(csvDf)
# print(data.cvs)