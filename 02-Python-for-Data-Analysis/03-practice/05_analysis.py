import pandas as pd

# Load Cleaned Dataset:
df = pd.read_csv("cleaned_dataset.csv")

# Create Revenue Column:
df["revenue"] = df["price"] * df["quantity"]


# ----------------------------
# Total Revenue:
# ----------------------------
total_revenue = df["revenue"].sum()
print("\nTotal Revenue: ")
print(total_revenue)


# ----------------------------
# Highest Revenue Product:
# ----------------------------
revenue_by_product = df.groupby("product")["revenue"].sum().round(3).sort_values(ascending=False)
print("\nHighest Revenue Category: ")
print(revenue_by_product)


# ----------------------------
# Revenue by Date:
# ----------------------------
revenue_by_date = df.groupby("order_date")["revenue"].sum().round(3).sort_values(ascending=False)
print("\Revenue by Date: ")
print(revenue_by_date)


# ----------------------------
# Highest Revenue Date:
# ----------------------------
print("\nHighest Revenue Date: ")
print(revenue_by_date.head(1))
