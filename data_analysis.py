import pandas as pd

df = pd.read_csv("students.csv")

print("===== FULL DATA =====")
print(df)

print("\n===== BASIC ATTRIBUTES =====")
print("Shape (Rows, Columns):", df.shape)
print("Column Names:", df.columns.tolist())
print("\nData Types:")
print(df.dtypes)

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

print("\n===== NAME AND MARKS =====")
print(df[["Name", "Marks"]])

df["Pass"] = df["Marks"] >= 75

print("\n===== DATA WITH PASS COLUMN =====")
print(df)

print("\n===== GENDER COUNT =====")
print(df["Gender"].value_counts())

print("\n===== DEPARTMENT WISE AVERAGE MARKS =====")
print(df.groupby("Department")["Marks"].mean())
