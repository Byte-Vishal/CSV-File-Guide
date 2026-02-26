import pandas as pd

# Create Data
data = {
    "Name": ["Vishal", "Arun", "Kiran"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("students.csv", index=False)

# Read CSV
df = pd.read_csv("students.csv")

print("Data:")
print(df)

print("\nBasic Attributes:")
print("Shape:", df.shape)
print("Columns:", df.columns)

print("\nNull Values:")
print(df.isnull().sum())
