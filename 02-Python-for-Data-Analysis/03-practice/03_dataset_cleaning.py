import pandas as pd

# Load Dataset:
df = pd.read_csv("00_dataset.csv")

print("\nInitial Dataset Shape: ")
print(df.shape)

print("\nMissing Values Before Cleaning: ")
print(df.isnull().sum())

# 1. Fill Missing Customer Names:
df["customer_name"] = df["customer_name"].fillna("Unknown")

# 2. Convert order_date to datetime:
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# 3. Correct Rows with Negative Rows:
df.loc[df["price"] < 0, "price"] = df.loc[df["price"] < 0, "price"].abs()

# 4. Fill Rows with Missing Quantity:
df.loc[df["quantity"].isnull(), "quantity"] = 1

# 5. Standardise Customer Names:
df["customer_name"] = df["customer_name"].str.strip().str.title()


print("\nDataset Shape After Cleaning: ")
print(df.shape)

print("\nMissing Values After Cleaning: ")
print(df.isnull().sum())

print("\nCleaned Dataset Preview: ")
print(df.head())


# Save Cleaned Dataset:
df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved as cleaned_dataset.csv")
