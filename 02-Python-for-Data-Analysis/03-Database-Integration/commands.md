# Database Integration: Structured Command Reference.

This document provides a structured reference for commonly used psycopg2 commands.

---

## 1. Importing Libraries:
- **Command:** import psycopg2
- **Explanation:** Imports PostgreSQL adapter for Python.

---

## 2. Connecting to a Database:
- **Command:** psycopg2.connect()
- **Explanation:** Creates a connection to a database.
- **Example:**
```bash
	conn = psycopg2.connect(
	dbname="practice_db",
	user="thando",
	host="localhost",
	port="5432"
	)
```

---

## 3. Creating a Cursor:
- **Command:** conn.cursor()
- **Explanation:** Creates a cursor to execute SQL queries.
- **Example:**
```bash
	cur = conn.cursor()
```

---

## 4. Executing Queries:
- **Command:** cur.execute(query, parameters)
- **Explanation:** Runs an SQL query.
- **Example:**
```bash
	cur.execute(
		"INSERT INTO customer (full_name, email_address) VALUES (%s, %s)",
		("John Doe", "john@example.com")
	)
```

---

## 5. Fetching Data:
### 5.1. Returning a Single Row:
- **Command:** cur.fetchone()
- **Explanation:** Returns the next row.
- **Example:**
```bash
	row = cur.fetchone()
```

### 5.2. Returning All Rows:
- **Command:** cur.fetchall()
- **Explanation:** Returns all rows.
- **Example:**
```bash
	rows = cur.fetchall()
```

---

## 6. Committing Transactions:
- **Command:** conn.commit()
- **Explanation:** Saves changes to the database.

---

## 7. Rolling Back Transactions:
- **Command:** conn.rollback()
- **Explanation:** Reverts changes after an error.

---

## 8. Inserting Multiple Rows:
- **Command:** cur.executemany()
- **Explanation:** Executes a query for multiple rows.
- **Example:**
```bash
	data = [
		("Alice", "alice@example.com"),
		("Bob", "bob@example.com")
	]

	cur.executemany(
		"INSERT INTO customer (full_name, email_address) VALUES (%s, %s)",
		data
	)
```

---

## 9. Returning Inserted Values:
- **Command:** RETURNING column_name
- **Explanation:** Returns values from an INSERT.
- **Example:**
```bash
	cur.execute(
		"INSERT INTO customer (full_name) VALUES (%s) RETURNING customer_id",
		("Jane Doe",)
	)

	customer_id = cur.fetchone()[0]
```

---

## 20. Closing Connection:
- **Command:**
```bash
	cur.close()
	conn.close()
```
- **Explanation:** Closes cursor and connection.

---

## 11. Error Handling:
- **Command:** try / except / finally
- **Explanation:** Handles errors and maintains consistency.
- **Example:**
```bash
	try:
		cur.execute(...)
		conn.commit()
	except Exception as e:
		conn.rollback()
		print(e)
	finally:
		cur.close()
		conn.close()
```

---

## 12. Parametrised Queries:
- **Command:** %s placeholders
- **Explanation:** Safely passes values into queries.
- **Example:**
```bash
	cur.execute(
		"SELECT * FROM customer WHERE email_address = %s",
		("john@example.com",)
	)
```

---

## Notes:
- Use parametrised queries for safety.
- Always call **commit()** after changes.
- Use **rollback()** on errors.
- Close connections after use.
- Use **RETURNING** for foreign key workflows.
