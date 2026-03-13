import pandas as pd

# Load Cleared Dataset:
df = pd.read_csv("cleaned_dataset.csv")

print("\nDataset Shape: ")
print(df.shape)

print("\nPreview: ")
print(df.head())

df["price"] = df["price"].round(2)
df["quantity"] = df["quantity"].round(2)

# --------------------------------------
# Summary Stastics:
# --------------------------------------
print("\nSummary Statistics: ")
print(df.describe())

# --------------------------------------
# Category Distribution:
# --------------------------------------
print("\nCategory Distribution: ")
print(df["category"].value_counts())

# --------------------------------------
# Revenue Column:
# --------------------------------------
df["revenue"] = df["price"] * df["quantity"]

print("\nRevenue Preview: ")
print(df[["product", "price", "quantity", "revenue"]].head())

# --------------------------------------
# Revenue by Product:
# --------------------------------------
revenue_by_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Product: ")
print(revenue_by_product)

# --------------------------------------
# Revenue by Category:
# --------------------------------------
revenue_by_category = df.groupby("category")["revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Category: ")
print(revenue_by_category)

# --------------------------------------
# Top Customers by Revenue:
# --------------------------------------
revenue_by_customer = df.groupby("customer_name")["revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Customer: ")
print(revenue_by_customer)

# --------------------------------------
# Save Dataset with Revenue Column:
# --------------------------------------
df.to_csv("eda_dataset.csv", index=False)

print("\nEDA dataset saved as eda_dataset.csv.")
