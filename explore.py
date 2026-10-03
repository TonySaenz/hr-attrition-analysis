import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
print(df.shape)
print(df.dtypes)
print("Missing:", df.isna().sum().sum(), "Duplicates:", df.duplicated().sum())
print(df.nunique().sort_values().head(5))
print(df["Attrition"].value_counts(normalize=True))
