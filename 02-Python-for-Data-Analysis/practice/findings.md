# Dataset Findings:

## Dataset Shape:
The dataset contains **12 rows** and **8 columns**.

---

## Columns:
- order_id
- customer_name
- email
- product
- category
- price
- quantity
- order_date

---

## Data Types:
- order_date: integer
- customer_name: text
- email: text
- product: text
- price: integer
- quantity: float
- order_date: text

Note: 'order_date' is currently stored as **text** and may need to be converted to a datetime type during cleaning.

---

## Duplicate Rows:
No duplicate rows were detected.

---

## Data Quality Issues Identified:
Based on inspection of the dataset:
1. One missing **customer_name** value.
2. One missing **quantity** value.
3. A **negative price value (-600)** exists in the dataset.
4. One **invalid date value ("invalid_date")** exists in the 'order_date' column.

The issues will be addressed during the cleaning stage before performing analysis.
