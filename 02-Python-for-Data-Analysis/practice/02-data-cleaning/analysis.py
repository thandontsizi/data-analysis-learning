import pandas as pd

# Load Dataset:
df = pd.read_csv("raw_data.csv")

# Cleaning Steps:
df["customer_name"] = df["customer_name"].fillna("Unknown")
df["customer_name"] = df["customer_name"].str.strip().str.title()
df["order_date"] = pd.to_datetime(df["order_date"])
df = df[df["price"] >= 0]
df = df.dropna(subset=["quantity"])

# Create Revenue Column:
df["revenue"] = df["price"] * df["quantity"]



# -------- ANALYSIS -------- #

print("\nTotal Revenue: ")
print(df["revenue"].sum())

print("\nRevenue by Product: ")
print(df.groupby("product")["revenue"].sum())

print("\nUnits Sold by Product: ")
print(df.groupby("product")["quantity"].sum())

print("\nRevenue by Customer: ")
print(df.groupby("customer_name")["revenue"].sum())

print("\nRevenue by Date: ")
print(df.groupby("order_date")["revenue"].sum())
