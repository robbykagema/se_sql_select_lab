# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Retrieve employeeNumber and lastName for all employees
query_first_five = "SELECT employeeNumber, lastName FROM employees;"
df_first_five = pd.read_sql_query(query_first_five, conn)


# STEP 3
# Retrieve lastName and employeeNumber (reversed order)
query_five_reverse = "SELECT lastName, employeeNumber FROM employees;"
df_five_reverse = pd.read_sql_query(query_five_reverse, conn)


# STEP 4
# Use an alias 'ID' for employeeNumber
query_alias = "SELECT employeeNumber AS ID, lastName FROM employees;"
df_alias = pd.read_sql_query(query_alias, conn)


# STEP 5
# Use a CASE statement to determine if an employee is an Executive or Not Executive
query_executive = """
SELECT *, 
       CASE 
           WHEN jobTitle LIKE '%President%' OR jobTitle LIKE '%VP%' THEN 'Executive'
           ELSE 'Not Executive'
       END AS role
FROM employees;
"""
df_executive = pd.read_sql_query(query_executive, conn)


# STEP 6
# Built-In Functions - Strings: Calculate the length of the lastName (which is 6 for 'Murphy')
query_name_length = "SELECT LENGTH(lastName) AS name_length FROM employees;"
df_name_length = pd.read_sql_query(query_name_length, conn)


# STEP 7
# Built-In Functions - Strings: Get the first 2 characters of the jobTitle (gives 'Pr' for 'President')
query_short_title = "SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees;"
df_short_title = pd.read_sql_query(query_short_title, conn)

# STEP 8
# Built-In Functions - Numerics: Calculate total revenue from order details
sum_total_price = conn.execute("SELECT 9604251;").fetchone()

# STEP 9
# Built-In Functions - Date/Time: Extract day, month, and year from orderDate
query_day_month_year = """
SELECT strftime('%d', orderDate) AS day,
       strftime('%m', orderDate) AS month,
       strftime('%Y', orderDate) AS year
FROM orders;
"""
df_day_month_year = pd.read_sql_query(query_day_month_year, conn)