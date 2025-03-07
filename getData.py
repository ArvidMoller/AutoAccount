import pandas as pd
import numpy as np

def encodeDf(df):
    encodedDf = df.copy()

    for row in df.itertuples(index=True, name="Row"):
        for col in df.columns:
            value = str(getattr(row, col))

            encoded_bytes = value.encode('utf-8')
            encoded_int = int.from_bytes(encoded_bytes)

            encodedDf.replace(to_replace=value, value=encoded_int, inplace=True)

    return encodedDf

def decodeDf(df):
    decodedDf = df.copy()

    for row in df.itertuples(index=True, name="Row"):
        for col in df.columns:
            value = int(getattr(row, col))
            print(value)
            
            decoded_bytes = value.to_bytes((value.bit_length() + 7) // 8)
            decoded_str = decoded_bytes.decode('utf-8')

            decodedDf.replace(to_replace=value, value=decoded_str, inplace=True)

    return decodedDf

csvDf = pd.read_csv("historical_transactions.csv")
features = csvDf.head(0)

df = encodeDf(csvDf)
decodeDfTest = decodeDf(df)  


# encodedDf.info()
print(df)
print(decodeDfTest)
# print(features)