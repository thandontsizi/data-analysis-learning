# Tests (Database Integration):
This file tests understanding of psycopg2 and database interaction using Python.

---

## 1. Basic Implementation:
1. Write a script to connect to a PostgreSQL database.
2. Create a table and insert one row into it.
3. Retrieve all rows from a table using psycopg2.
4. Insert multiple rows using executemany().
5. Insert a row and return its generated ID.
6. Close the cursor and the connection properly.

---

## 2. Conceptual Understanding:
1. What is the role of a cursor in psycopg2?
2. Why is conn.commit() required after inserting data?
3. What happens if commit() is not called?
4. What is the difference between fetchone() and fetchall()?
5. What does rollback() do?
6. Why are parametrised queries important?
7. What problem does RETURNING solve?

---

## 3. Scenario-Based Exercises:
1. You run an insert script but no data appears in your database. What could be the problem be?
2. Your script crashes after inserting some rows. How would you ensure the database stays consistent?
3. A UNIQUE constraint error occurs during insertion. How would you handle it in Python?
4. You need to generate and insert 10,000 rows efficiently. What approach would you use?
5. You are inserting user-generated input into a query. What is the risk and how would you prevent it?
6. Your connection is left open across multiple scripts. What problems could this cause?
7. You need to insert data into multiple related tables (Customer -> Order -> Order_Item). What order should INSERT follow and why?
8. You need to insert an order and immediately use its ID for Order_Item records. How would you do this?

---

## 4. Practical Challenge:
- Write a script that:
	- Connects to a database.
	- Inserts a new customer.
	- Retrieves the customer_id using RETURNING.
	- Inserts a related order using that customer_id.
	- Commits the transaction.
	- Handles errors using rollback().
	- Closes the connection properly.

---
