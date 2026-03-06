# Python Data Analysis: Structured Command Reference.
This document provides a structured reference for commonly used pandas commands.

All examples assume a dataset with the following columns:
- order_id.
- customer_name.
- email.
- product.
- price.
- quantity.
- order_date.

---

# 1. Importing Libraries:
## Import pandas:
- Command: import pandas as pd
- Explanation: Imports the pandas library which is used for data manipulation and analysis in Python.

---

# 2. Loading Data:
## Loading a CSV File:
- Command: pd.read_csv()
- Explanation: Reads a CSV file and loads it into a pandas DataFrame.
- Example: df = pd.read_csv("raw_data.csv")
 
## Loading an Excel File:
- Command: pd.read_excel()
- Explanation: Reads an Excel file and loads it into a pandas DataFrame.
- Example: df = pd.read_excel("sales_data.xlsx")

---

# 3. Inspecting Data:
## Viewing First Rows:
- Command: df.head()
- Explanation: Displays the first rows of the dataset to preview its structure and values.
- Example: df.head(10) - Shows first 10 rows.

## Viewing Last Rows:
- Command: df.tail()
- Explanation: Displays the last rows of a dataset.
- Example: df.tail(10) - Shows last 10 rows.

## Inspecting Dataset Structure:
- Command: df.info()
- Explanation: Displays column names, data types, and the number of non-null values.

## Summary Statistics:
- Command: df.describe()
- Generates summary statistics for numeric columns such as mean, minimum, and maximum.

---

# 4. Data Quality Checks:
## Checking Missing Values:
- Command: df.isnull()
- Explanation: Detects missing values in a dataset.
- Example: df.isnull().sum()
	### Checking missing values in a specific column:
	- df["quantity'].isnull().sum()

## Checking Duplicate Rows:
- Command: df.duplicated()
- Explanation: Identifies duplicate rows in the dataset.
- Example: df.duplicated().sum()
	### View duplicated rows:
	- df[df.duplicated()]

## Checking Unique Values:
- Command: df.unique()
- Explanation: Displays unique values within a column.
- Example: df["product"].unique()

## Counting Value Frequency:
- Command: value_counts()
- Explanation: Counts how frequently each value appears in a column.
- Example: df["products'].value_counts()

---

# 5. Cleaning Data:
## Removing Missing Values:
- Command: df.dropna()
- Explanation: Removes rows containing missing values.
- Example: df = df.dropna()

## Filling Missing Values:
- Command: df.fill.na()
- Explanation: Replaces missing values with specified value.
- Example: df["quantity"] = df["quantity"].fillna(0)

## Removing Duplicate Rows:
- Command: df.drop_duplicates()
- Explanation: Removes duplicate rows from the dataset.
- Example: df = df.drop_duplicates()

## Standardising Text:
- Command:.str.strip.str.title()
- Explanation: Removes extra spaces and standardises capitalisation in text columns.
- Example: df["customer_name"] = df["customer_name"].str.strip().str.title()

---

# 6. Data Type Conversion:
## Checking Data Types:
- Command: df.dtypes
- Explanation: Displays the data type of each column.

## Converting to Datetime:
- Command: pd.to_datetime()
- Explanation: Converts text-based date values into proper datetime format.
- Example: df["order_date"] = pd.to_datetime(df["order_date"])

## Converting to Numeric:
- Command: pd.to_numeric()
- Explanation: Converts values to numeric format and handles invalid entries.
- Example: df["price"] = pd.to_mumeric(df["price"], errors="coerce")

---

# 7. Filtering Data:
## Filtering Rows with Boolean Indexing:
- Command: df[condition]
- Explanation: Filters rows by passing a boolean condition inside square brackets.
- Example:
	### Orders where quantity is greater than 1:
	- df[df["quantity"] > 1]

## Filtering with Multiple Conditions:
- Command: df[(condition1) & (condition2)]
- Explanation: Filters rows using multiple conditions.
- Example:
	### Orders where price is above R1000 AND quantity is at least 1:
	- df[(df["price"] > 1000) & (df["quantity"] >= 1)]

## Filtering with OR Conditions:
- Command: df[(condition1) | (condition2)]
- Explanation: Filters rows where either condition is true.
- Example:
	### Orders where product is Laptop OR Monitor:
	- df[(df["product"] == "Laptop") | (df["product"] == "Monitor")]


## Filtering by Membership (IN):
- Command: df[column].isin(list)
- Explanation: Filters rows where a column value is contained in a provided list.
- Example:
	### Orders where product is one of the listed items:
	- df[df["product"].isin(["Mouse", "Keyboard", "USB-C Cable"])]

## Filtering Missing Values:
- Command: df[column].isna()
- Explanation: Filterrs rows where a column value is missing (NaN).
- Example:
	### Rows where quantity is missing:
	- df[df["quantity"].isna()]

## Filtering Non-Missing Values:
- Command: df[column].notna()
- Explanation: Filters rows where value is not missing.
- Example:
	### Rows where email is present:
	- df[df["email"].notna()]

## Filtering by String Contains:
- Command: df[column].str.contains("text", case=..., na=...)
- Explanation: Filters rows where a string column contains a substring. Useful for messy text fields.
- Example:
	### Customers whose name contains "Brian" (case insensitive):
	- df[df["customer_name"].str.contains("brian", case=False, na=False)]

## Filtering by Date Range:
- Command: df[(df[date_col] >= start) & (df[date_col] <= end)]
- Explanation: Filters rows within a date range. The date column should be datetime reliable results.
- Example:
	### Ensure the column is datetime first:
	- df["order_date"] = pd.tp.datetime(df["order_date"])
	### Filter between two dates:
	- df[(df["order_date"] >= "2026-02-01") & (df["order_date"] <= "2026-02-10")]

---

# 8. Aggregation and Analysis:
## Grouping Data:
- Command: df.groupby()
- Explanation: Groups rows based on the values of a column.
- Example: df.groupby("product")

## Summing Values by Group:
- Command: df.groupby(column)[value_column].sum()
- Explanation: Groups rows by a column and calculates the sum of another column within each group.
- Example:
	### Total quantity sold per product:
	- df.groupby("product")["quantity"].sum()

## Calculating Mean Values by Group:
- Command: df.groupby(column)[value_column].mean()
- Explanation: Groups rows by a column and calculates the average value within each group.
- Example:
	### Average product price per product category:
	- df.groupby("product")["price"].mean()

## Counting Rows by Group:
- Command: df.groupby(column).size()
- Explanation: Counts how many rows exist in each group.
- Example: 
	### Number of orders per product:
	- df.groupby("product").size()

## Creating a Calculated Column:
- Command: df[new_column] = calculation
- Explanation: Creates a new column based on calculations using existing columns.
- Example:
	### Create a revenue column:
	- df["revenue"] = df["price"] * df["quantity"]

## Multiple Aggregations with agg():
- Command: df.groupby(column).agg({column: function})
- Explanation: Applies multiple aggregation functions to grouped data.
- Example: df.groupby("product").agg({"quantity": "sum"})

## Sorting Aggregated Results:
- Command: .sort_values()
- Explanation: Sorts the results of an aggregation to highlight highest or lowest values.
- Example: df.groupyby("product")["quantity"].sum().sort_values(ascending=False)

---

# 9. Validation Checks:
## Checking Dataset Shape:
- Command: df.shape
- Explanation: Returns the number of rows and columns in the dataset.
