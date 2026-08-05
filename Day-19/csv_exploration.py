import pandas as pd

df = pd.read_csv("student.csv")

print("Complete Dataset")
print(df)

print("\nFirst 3 Rows")
print(df.head(3))

print("\nLast 2 Rows")
print(df.tail(2))

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nInformation")
df.info()

print("\nStatistics")
print(df.describe())