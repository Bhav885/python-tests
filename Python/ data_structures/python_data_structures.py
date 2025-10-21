# python_data_structures.py

# Reading customer data from CSV
import csv

customers = []

with open("customers_list.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        customers.append(row)

print("Customer Details:")
for c in customers:
    print(c)

# Using Python data structures
customer_names = [c['name'] for c in customers]   # List
customer_ids = tuple(c['id'] for c in customers)  # Tuple
customer_emails = set(c['email'] for c in customers)  # Set
customer_dict = {c['id']: c for c in customers}   # Dictionary

print("\nList of Names:", customer_names)
print("Tuple of IDs:", customer_ids)
print("Set of Emails:", customer_emails)
print("Dictionary of Customers:", customer_dict)
