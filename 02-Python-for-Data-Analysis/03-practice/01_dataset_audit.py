import pandas as pd

# Load Dataset:
df = pd.read_csv("00_dataset.csv")

print("\nDataset Shape: ")
print(df.shape)

print("\nColumns: ")
print(df.columns)

print("\nColumn Info: ")
print(df.info())

print("\nMissing Values: ")
print(df.isnull().sum())

print("\nDuplicate Rows: ")
print(df.duplicated().sum())

print("\nPreview: ")
print(df.head())
