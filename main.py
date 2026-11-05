import sqlite3 
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# # ------------ Get all data ------------
# employees = pd.read_sql("""
# SELECT *
#   FROM employees;
# """, conn)

# print(employees)

# # ------------ Filter data by lastName  ------------
# employees = pd.read_sql("""
# SELECT *
#   FROM employees
#   WHERE lastName = "Patterson";
# """, conn)

# print(employees)

# # ------------ Select employees with 5 letters in their first name ------------
# employees_with_5_letters = pd.read_sql("""
# SELECT *, length(firstName) AS name_length
#   FROM employees
#   WHERE name_length = 5
# """, conn)

# print(employees_with_5_letters)

# # ------------ Select employees with first name that has the initial L ------------
# employees_with_initial_L = pd.read_sql("""
# SELECT *, substr(firstName, 1, 1) AS first_initial
#   FROM employees
#   WHERE first_initial = "L"
# """, conn)

# print(employees_with_initial_L)

# # ------------ Select order details where price rounded to nearest integer is $30 ------------
# rounded_price = pd.read_sql("""
# SELECT *, CAST(round(priceEach) AS INTEGER) AS rounded_price_int
#   FROM orderDetails
#   WHERE rounded_price_int = 30
# """, conn)

# print(rounded_price)

# # ------------ Select orders placed in January ------------
# january_orders = pd.read_sql("""
# SELECT *, strftime("%m", orderDate) AS month
#     FROM orders
#     WHERE month = "01"
# """, conn)

# print(january_orders)


# ------------ Select orders that were shipped late ------------
orders_shipped_late = pd.read_sql("""
SELECT *, julianday(shippedDate) - julianday(requiredDate) AS days_late
    FROM orders
    WHERE days_late > 0
""", conn)

print(orders_shipped_late)

conn.close()