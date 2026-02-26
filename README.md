# CSV File Guide

## Introduction
This guide explains how to:
- Create a CSV file
- Read a CSV file
- Manipulate rows and columns
- Find basic attributes
- Detect and handle null values  
using Python and the Pandas library.

---

## 1️⃣ Import Library

```python
import pandas as pd
```

---

## 2️⃣ Creating a CSV File

```python
data = {
    "Name": ["Vishal", "Arun", "Kiran"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

print("CSV file created successfully")
```

---

## 3️⃣ Reading a CSV File

```python
df = pd.read_csv("students.csv")
print(df)
```

---

## 4️⃣ Basic Attributes of DataFrame

```python
print(df.shape)        # (rows, columns)
print(df.columns)      # Column names
print(df.head())       # First 5 rows
print(df.tail())       # Last 5 rows
print(df.info())       # Data types
print(df.describe())   # Statistical summary
```

---

## 5️⃣ Selecting Rows and Columns

### Select a Single Column

```python
print(df["Name"])
```

### Select Multiple Columns

```python
print(df[["Name", "Marks"]])
```

### Select Row by Index

```python
print(df.loc[0])
```

---

## 6️⃣ Adding a New Column

```python
df["Grade"] = ["A", "A+", "B"]
print(df)
```

---

## 7️⃣ Deleting a Column

```python
df.drop("Grade", axis=1, inplace=True)
print(df)
```

---

## 8️⃣ Finding Null Values

```python
print(df.isnull())
print(df.isnull().sum())   # Count null values
```

---

## 9️⃣ Handling Null Values

### Fill Null Values

```python
df.fillna(0, inplace=True)
```

### Drop Rows with Null Values

```python
df.dropna(inplace=True)
```

---

## Conclusion

Using Pandas, we can:
- Create CSV files
- Read CSV files
- Manipulate rows and columns
- Find basic attributes
- Detect and handle null values efficiently.
