import pandas as pd

# Load dataset:
df = pd.read_csv("raw_data.csv")

print("Initial Dataset Shape: ")
print(df.shape)

print("\nMissing Values Before Cleaning: ")
print(df.isnull().sum())


# Cleaning Data:
# 1. Handle Missing Customer Names:
df["customer_name"] = df["customer_name"].fillna("Unknown")

# 2. Standardise Customer Name Format:
df["customer_name"] = df["customer_name"].str.strip().str.title()

# 3. Convert order_date to datetime:
df["order_date"] = pd.to_datetime(df["order_date"])

# 4. Remove Rows with Negative Prices:
df = df[df["price"] >= 0]

# 5. Handle Missing Quantity:
# For this dataset, we drop rows where quantity is missing:
df = df.dropna(subset=["quantity"])

# 6. Create Revenue Column:
df["revenue"] = df["price"] * df["quantity"]


print("\nDataset Shape After Cleaning: ")
print(df.shape)

print("\nMissing Values After Cleaning: ")
print(df.isnull().sum())

print("\nPreview of Cleaned Dataset: ")
print(df.head())


