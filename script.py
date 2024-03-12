import mysql.connector
from prettytable import PrettyTable

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tarun@123",
    database="inventory_db"
)
cursor = db.cursor()

def add_product(name, price, quantity, category_id, supplier_id):
    sql = "INSERT INTO products (name, price, quantity, category_id, supplier_id) VALUES (%s, %s, %s, %s, %s)"
    val = (name, price, quantity, category_id, supplier_id)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record(s) inserted.")

def display_products():
    cursor.execute("SELECT * FROM products")
    result = cursor.fetchall()
    print_table(result)

def display_categories():
    cursor.execute("SELECT * FROM categories")
    result = cursor.fetchall()
    print_table(result)

def display_suppliers():
    cursor.execute("SELECT * FROM suppliers")
    result = cursor.fetchall()
    print_table(result)

def display_customers():
    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()
    print_table(result)

def display_orders():
    cursor.execute("SELECT * FROM orders")
    result = cursor.fetchall()
    print_table(result)

def print_table(result):
    table = PrettyTable()
    table.field_names = [i[0] for i in cursor.description]
    for row in result:
        table.add_row(row)
    print(table)

add_product("Laptop", 1000, 10, 1, 1)
display_products()

db.close()