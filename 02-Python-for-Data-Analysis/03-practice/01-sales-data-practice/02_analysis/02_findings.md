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

Note: 'order_date' is currently stored as **text** and will need to be converted to a datetime type during cleaning.

---

## Missing Values:
The dataset contains two missing values:
- customer_name: 1 missing value.
- quantity: 1 missing value.

---

## Duplicate Rows:
No duplicate rows were detected.

---

# Data Quality Issues and Decisions:
## 1. Missing Customer Name:
- One record contains a missing value in the 'customer_name' column. 
- The row still contains a valid email address and purchase information so removing the row would unnecessarily discard valid transaction data.

### Decision:
- The missing value will be replaced with **'Unknown'**.

---

## 2. Missing Quantity:
- One transaction for the product **Monitor** contains a missing value in the 'quantity' column.
- Inspection of other Monitor transactions shows that the quantity is consistently recorded as **1**.
- This indicates the missing value is likely a data entry omission.

### Decision:
- The missing quantity value will be replaced with **1**.

---

## 3. Negative Price Value:
- One row contains a negative price value **(-600)** for the product **Keyboard**.
- Inspection of other Keyboard entries shows that the correct price is consistently **600**.
- The negative value is therefore treated as a data entry error.

### Decision:
- The value will be corrected from **-600 to 600**.

---

## 4. Invalid Date Value:
- One record contains an invalid value in the 'order_date' column ('invalid_date').
- Because the correct date cannot be reliably inferred, the row cannot be used for time-based analysis.

### Decision:
- Rows with invalid dates will simply be excluded from time-based calculations unless dropping or deletion is necessary.
- The row will be retained so that the transaction remains part of revenue and product analysis.
- The value will be converted to a missing datetime value (NaT).

The issues will be addressed during the cleaning stage before performing analysis.

---
