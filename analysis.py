import pandas as pd

df = pd.read_csv("hr_attrition_clean.csv")

cols = ["Department", "JobRole", "JobLevel", "OverTime", "BusinessTravel", "MaritalStatus",
        "AgeBand", "TenureBand", "IncomeBand", "StockOptionLevel",
        "JobSatisfactionLabel", "EnvironmentSatisfactionLabel", "WorkLifeBalanceLabel"]

for col in cols:
    t = df.groupby(col)["AttritionFlag"].agg(Employees="count", AttritionRate="mean")
    t["AttritionRate"] = (t["AttritionRate"] * 100).round(1)
    print(t.sort_values("AttritionRate", ascending=False), "\n")

print((pd.crosstab(df["JobSatisfactionLabel"], df["EnvironmentSatisfactionLabel"],
                   values=df["AttritionFlag"], aggfunc="mean") * 100).round(1))
