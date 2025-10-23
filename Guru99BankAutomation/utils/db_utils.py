import mysql.connector

def get_customer_credentials(customer_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bhavana@1102",  # your MySQL password
        database="guru99"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT username, password FROM customers WHERE customer_id=%s", (customer_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_all_customers():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bhavana@1102",
        database="guru99"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    conn.close()
    return results
