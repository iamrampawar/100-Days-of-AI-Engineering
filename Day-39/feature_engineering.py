import pandas as pd
from sklearn.preprocessing import StandardScaler
# Sample dataset
data = {
    "Name": ["Ram", "Amit", "Sneha", "Rahul"],
    "Age": [20, 21, None, 22],
    "City": ["Mumbai", "Pune", "Mumbai", "Delhi"],
    "Salary": [50000, 60000, 55000, None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

print("\nAfter Handling Missing Values:")
print(df)

# One-Hot Encoding
df = pd.get_dummies(df, columns=["City"], dtype=int)

print("\nAfter One-Hot Encoding:")
print(df)

# Feature Scaling
scaler = StandardScaler()

df[["Age", "Salary"]] = scaler.fit_transform(
    df[["Age", "Salary"]]
)

print("\nAfter Feature Scaling:")
print(df)