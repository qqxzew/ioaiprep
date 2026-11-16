import pandas as pd

df = pd.read_csv("cooking.csv")
print(df.isna().sum())
print(df["weight"].fillna(df["weight"].median()).isna().sum())
