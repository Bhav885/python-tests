import csv
import mysql.connector

# ========== CONNECT TO MYSQL ==========
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # change to your MySQL username
        password="Bhavana@1102",           # change to your MySQL password
        database="ecommerce_db"
    )

# ========== READ CUSTOMERS FROM CSV ==========
def read_customers_from_csv(file_name):
    customers = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers.append(row)
    return customers

# ========== INSERT CUSTOMERS ==========
def insert_customers(customers):
    conn = get_connection()
    cursor = conn.cursor()
    for c in customers:
        cursor.execute("""
            INSERT INTO customers (name, email, city)
            VALUES (%s, %s, %s)
        """, (c['name'], c['email'], c['city']))
    conn.commit()
    conn.close()
    print("✅ Customers inserted successfully!")

# ========== INSERT ORDERS ==========
def insert_orders():
    conn = get_connection()
    cursor = conn.cursor()
    orders = [
        (1, "Laptop", 75000, "2025-10-22"),
        (2, "Mobile", 30000, "2025-10-21"),
        (3, "Headphones", 2500, "2025-10-20"),
    ]
    cursor.executemany("""
        INSERT INTO orders (customer_id, product_name, amount, order_date)
        VALUES (%s, %s, %s, %s)
    """, orders)
    conn.commit()
    conn.close()
    print("✅ Orders inserted successfully!")

# ========== BASIC CRUD OPERATIONS ==========
def basic_queries():
    conn = get_connection()
    cursor = conn.cursor()

    print("\n--- SELECT ---")
    cursor.execute("SELECT * FROM customers")
    for row in cursor.fetchall():
        print(row)

    print("\n--- UPDATE ---")
    cursor.execute("UPDATE customers SET city='Hyderabad' WHERE name='Priya'")
    conn.commit()

    # print("\n--- DELETE ---")
    # cursor.execute("DELETE FROM customers WHERE name='Arjun'")
    # conn.commit()

    conn.close()
    print("✅ Basic queries executed successfully!")

# ========== JOIN QUERY ==========
def join_query():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.name, c.email, o.product_name, o.amount
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
    """)
    print("\n--- JOIN (Customers + Orders) ---")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# ========== VIEW + STORED PROCEDURE ==========
def view_and_procedure_demo():
    conn = get_connection()
    cursor = conn.cursor()

    print("\n--- VIEW: Active Customers ---")
    cursor.execute("SELECT * FROM active_customers")
    for row in cursor.fetchall():
        print(row)

    print("\n--- CALLING STORED PROCEDURE ---")
    cursor.callproc("AddCustomer", ("Meena", "meena@gmail.com", "Kolkata"))
    conn.commit()
    print("✅ Stored procedure executed successfully!")

    conn.close()

if __name__ == "__main__":
    # 1️⃣ Read customers from CSV and insert into MySQL
    customers = read_customers_from_csv("customers.csv")  # Make sure this CSV exists
    insert_customers(customers)

    # 2️⃣ Insert sample orders
    insert_orders()

    # 3️⃣ Execute basic CRUD operations
    basic_queries()

    # 4️⃣ Execute JOIN query
    join_query()

    # 5️⃣ Demonstrate VIEW and stored procedure
    view_and_procedure_demo()
