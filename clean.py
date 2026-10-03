import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
df = df.drop(columns=["EmployeeCount", "Over18", "StandardHours", "DailyRate", "HourlyRate", "MonthlyRate"])

df["AttritionFlag"] = (df["Attrition"] == "Yes").astype(int)

sat = {1: "Low", 2: "Medium", 3: "High", 4: "Very High"}
for col in ["EnvironmentSatisfaction", "JobSatisfaction", "RelationshipSatisfaction", "JobInvolvement"]:
    df[col + "Label"] = df[col].map(sat)
df["EducationLabel"] = df["Education"].map({1: "Below College", 2: "College", 3: "Bachelor", 4: "Master", 5: "Doctor"})
df["WorkLifeBalanceLabel"] = df["WorkLifeBalance"].map({1: "Bad", 2: "Good", 3: "Better", 4: "Best"})

df["AgeBand"] = pd.cut(df["Age"], [17, 25, 35, 45, 60], labels=["18-25", "26-35", "36-45", "46-60"])
df["TenureBand"] = pd.cut(df["YearsAtCompany"], [-1, 2, 5, 10, 40], labels=["0-2", "3-5", "6-10", "11+"])
df["IncomeBand"] = pd.qcut(df["MonthlyIncome"], 4, labels=["Q1 Lowest", "Q2", "Q3", "Q4 Highest"])

df.to_csv("hr_attrition_clean.csv", index=False)

print(df.shape)
print(df[["AgeBand", "TenureBand", "IncomeBand"]].isna().sum())
print(df.groupby("IncomeBand", observed=True)["MonthlyIncome"].agg(["min", "max"]))
