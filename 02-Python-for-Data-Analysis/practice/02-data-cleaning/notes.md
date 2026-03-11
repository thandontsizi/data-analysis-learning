# Data Cleaning Notes:

## Cleaning Decisions:
- Filled missing customer_name values with "Unknown".
- Standardised customer_name capitalisation.
- Converted  order_date to datetime after manually fixing inconsistent formats.
- Removed rows with negative prices.
- Removed rows with missing quantities.
- Created a revenue column.

## Outcome:
- Dataset became cleaner and ready for analysis.
- Time-based analysis is now possible.
- Revenue can now be calculated reliably.
