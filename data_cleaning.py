import pandas as pd
import numpy as np

df = pd.read_csv("employees.csv")
# BEFORE CLEANING

before_rows = len(df)

before_missing = df.isnull().sum().sum()

before_duplicates = df.duplicated().sum()

print("Original Dataset")
print(df)

print("\nDataset Information")
print(df.info())

print("\nDataset Shape")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

# STEP 2: HANDLE MISSING VALUES

# Fill missing Age with median
df["age"] = df["age"].fillna(df["age"].median())

# Fill missing Salary with median
df["salary"] = df["salary"].fillna(df["salary"].median())

# Standardise city names before finding mode
df["city"] = df["city"].str.strip().str.title()

# Fill missing City with mode
df["city"] = df["city"].fillna(df["city"].mode()[0])

# Check missing values again
print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nUpdated Dataset")
print(df)
# Convert joining_date into datetime

# STEP 3: FIX DATA TYPES

# Convert joining date into datetime
df["joining_date"] = pd.to_datetime(df["joining_date"])

# Convert age into integer
df["age"] = df["age"].astype(int)

# Standardise names
df["name"] = df["name"].str.strip().str.title()


# STEP 4: REMOVE DUPLICATES

df = df.drop_duplicates()


# CHECK RESULTS

print("\nUpdated Dataset")
print(df)

print("\nUpdated Data Types")
print(df.dtypes)

print("\nDuplicates After Cleaning")
print(df.duplicated().sum())

# STEP 4: DETECT OUTLIERS USING IQR

# Calculate Q1
Q1 = df["salary"].quantile(0.25)

# Calculate Q3
Q3 = df["salary"].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate lower boundary
lower_limit = Q1 - (1.5 * IQR)

# Calculate upper boundary
upper_limit = Q3 + (1.5 * IQR)

# Find outliers
outliers = df[
    (df["salary"] < lower_limit) |
    (df["salary"] > upper_limit)
]

# Display results
print("\nOutlier Detection")

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

print("\nDetected Outliers")
print(outliers[["name", "salary"]])
# AFTER CLEANING

after_rows = len(df)

after_missing = df.isnull().sum().sum()

after_duplicates = df.duplicated().sum()
summary = pd.DataFrame({

    "Metric": ["Rows", "Missing Values", "Duplicates"],

    "Before": [
        before_rows,
        before_missing,
        before_duplicates
    ],

    "After": [
        after_rows,
        after_missing,
        after_duplicates
    ]

})

print(summary)
df.to_csv("clean_data.csv", index=False)

summary.to_csv("cleaning_summary.csv", index=False)
df.to_csv("clean_data.csv", index=False)

summary.to_csv("cleaning_summary.csv", index=False)

print("\nFiles saved successfully!")