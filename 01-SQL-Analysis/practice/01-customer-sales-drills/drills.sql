-- Customer Sales SQL Drills (Progressive Difficulty):
-- Rules:
-- 1. Write your answer under each prompt.
-- 2. Do not copy from portfolio repo or anywhere else.
-- 3. Run each query in psql and check the output.
-- 4. Keep it readable.

-- ==================================================================================
-- LEVEL 0: Warm-up (table familiarity).
-- ==================================================================================

-- L0.1: Show all customers (id, name, email).
-- Write query below:


-- L0.2: Show all products (id, name, price).
-- Write query below:


-- L0.3: Show all orders (order_id, customer_id, product_id, quantity, order_date).
-- Write query below:


-- ==================================================================================
-- LEVEL 1: Core Queries (same as portfolio).
-- ==================================================================================

-- L1.1: Total revenue generated from all orders.
-- Hint: JOIN orders to products, revenue = quantity * price.
-- Write query below:


-- L1.2: Total products by total quantity sold.
-- Hint: SUM(quantity), GROUP BY product.
-- Write query below:


-- L1.3: Top customers by total spend (highest first).
-- Hint: SUM(quantity * price), GROUP BY customer.
-- Write query below:

-- L1.4: Revenue by date (chronological).
-- Hint: GROUP BY order_date.
-- Write query below:


-- ===================================================================================
-- LEVEL 2: Same Ideas, Small Variations.
-- ===================================================================================

-- L2.1: Total revenue for a single day (pick a date you have in your data).
-- Hint: WHERE order_date = 'YYYY-MM-DD'.
-- Write query below:


-- L2.2: Total revenue for date range.
-- Hint: WHERE order_date BETWEEN 'YYYY-MM-DD' AND 'YYYY-MM-DD'.
-- Write query below:


-- L2.3: Show only orders with quantity >= 2.
-- Hint: WHERE quantity >= 2.
-- Write query below:


-- ====================================================================================
-- LEVEL 3: Filtering Groups (HAVING).
-- ====================================================================================

-- L3.1: Products with total_quantity_sold >= 2
-- Hint: HAVING SUM(quantity) >= 2.
-- Write query below:


-- L3.2: Customers who spent more than R1000.00 in total.
-- Hint: HAVING SUM(quantity * price) > 1000.
-- Write query below:


-- =====================================================================================
-- LEVEL 4: Verification Checks.
-- =====================================================================================

-- L4.1: Count rows in each table: customers, products, orders.
-- Hint: SELECT COUNT (*)
-- Write query below:


-- L4.2: Check for orphan orders (orders with customer_id not found in customers).
-- Hint: LEFT JOIN + WHERE customers.customer_id IS NULL.
-- Write query below:


-- L4.3: Check for orphan orders (orders with product_id not found in products).
-- Hint: LEFT JOIN + WHERE products.product_id IS NULL.
-- Write query below:


-- ======================================================================================
-- LEVEL 5: Presentation Polish (readability).
-- ======================================================================================

-- L5.1: Rewrite L1.3 (top customers) but include:
-- customer_name, total_spent, and number_of_orders.
-- Hint: COUNT(order_id) AS number_of_orders.
-- Write query below:
