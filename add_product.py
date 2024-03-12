import mysql.connector
from prettytable import PrettyTable
import tkinter as tk
from tkinter import messagebox

db = mysql.connector(
    host="localhost",
    user="root",
    password="Tarun@123",
    database="inventory_db"
)
cursor = db.cursor()

def add_product(cursor, db, name, price, quantity, category_id, supplier_id):
    sql = "INSERT INTO products (name, price, quantity, category_id, supplier_id) VALUES (%s, %s, %s, %s, %s)"
    val = (name, price, quantity, category_id, supplier_id)
    cursor.execute(sql, val)
    db.commit()
    return f"{cursor.rowcount} record(s) inserted."

def display_products(cursor):
    cursor.execute("SELECT * FROM products")
    result = cursor.fetchall()
    return result

def print_table(cursor, result):
    table = PrettyTable()
    table.field_names = [i[0] for i in cursor.description]
    for row in result:
        table.add_row(row)
    return str(table)

def add_product_gui():
    def submit():
        message = add_product(cursor, db, name_entry.get(), float(price_entry.get()), int(quantity_entry.get()), int(category_id_entry.get()), int(supplier_id_entry.get()))
        messagebox.showinfo("Success", message)

    window = tk.Toplevel(root)
    window.title("Add product")
    window.geometry("500x500")

    name_label = tk.Label(window, text="Name")
    name_entry = tk.Entry(window)
    price_label = tk.Label(window, text="Price")
    price_entry = tk.Entry(window)
    quantity_label = tk.Label(window, text="Quantity")
    quantity_entry = tk.Entry(window)
    category_id_label = tk.Label(window, text="Category ID")
    category_id_entry = tk.Entry(window)
    supplier_id_label = tk.Label(window, text="Supplier ID")
    supplier_id_entry = tk.Entry(window)
    submit_button = tk.Button(window, text="Submit", command=submit)

    name_label.pack()
    name_entry.pack()
    price_label.pack()
    price_entry.pack()
    quantity_label.pack()
    quantity_entry.pack()
    category_id_label.pack()
    category_id_entry.pack()
    supplier_id_label.pack()
    supplier_id_entry.pack()
    submit_button.pack()

def display_products_gui():
    window = tk.Toplevel(root)
    window.title("Display products")
    window.geometry("500x500")

    products = display_products(cursor)
    table = print_table(cursor, products)
    table_label = tk.Label(window, text=table, justify="left", font=("Courier", 10))

    table_label.pack()

root = tk.Tk()
root.geometry("500x500")

add_product_button = tk.Button(root, text="Add product", command=add_product_gui)
display_products_button = tk.Button(root, text="Display products", command=display_products_gui)

add_product_button.pack()
display_products_button.pack()

root.mainloop()

db.close()