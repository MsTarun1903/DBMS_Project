import mysql.connector
from prettytable import PrettyTable
import tkinter as tk
from tkinter import messagebox

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
    return f"{cursor.rowcount} record(s) inserted."

def update_product(product_id, name, price, quantity, category_id, supplier_id):
    sql = "UPDATE products SET name = %s, price = %s, quantity = %s, category_id = %s, supplier_id = %s WHERE id = %s"
    val = (name, price, quantity, category_id, supplier_id, product_id)
    cursor.execute(sql, val)
    db.commit()
    return f"{cursor.rowcount} record(s) updated."

def delete_product(product_id):
    sql = "DELETE FROM products WHERE id = %s"
    val = (product_id,)
    cursor.execute(sql, val)
    db.commit()
    return f"{cursor.rowcount} record(s) deleted."

def display_products():
    cursor.execute("SELECT * FROM products")
    result = cursor.fetchall()
    return result

def print_table(result):
    table = PrettyTable()
    table.field_names = [i[0] for i in cursor.description]
    for row in result:
        table.add_row(row)
    return str(table)


def add_product_gui():
    def submit():
        message = add_product(name_entry.get(), float(price_entry.get()), int(quantity_entry.get()), int(category_id_entry.get()), int(supplier_id_entry.get()))
        messagebox.showinfo("Success", message)

    window = tk.Toplevel(root)
    window.title("Add product")
    window.geometry("500x500")
    window.configure(bg="light blue")

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
    # ... rest of your add_product_gui function ...

def update_product_gui():
    def submit():
        message = update_product(int(product_id_entry.get()), name_entry.get(), float(price_entry.get()), int(quantity_entry.get()), int(category_id_entry.get()), int(supplier_id_entry.get()))
        messagebox.showinfo("Success", message)

    window = tk.Toplevel(root)
    window.title("Update product")
    window.geometry("500x500")

    product_id_label = tk.Label(window, text="Product ID")
    product_id_entry = tk.Entry(window)
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

    product_id_label.pack()
    product_id_entry.pack()
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

    # ... rest of your update_product_gui function ...
def delete_product_gui():
    def submit():
        message = delete_product(int(product_id_entry.get()))
        messagebox.showinfo("Success", message)

    window = tk.Toplevel(root)
    window.title("Delete product")
    window.geometry("500x500")

    product_id_label = tk.Label(window, text="Product ID")
    product_id_entry = tk.Entry(window)
    submit_button = tk.Button(window, text="Submit", command=submit)

    product_id_label.pack()
    product_id_entry.pack()
    submit_button.pack()

    # ... rest of your delete_product_gui function ...

def display_products_gui():
    window = tk.Toplevel(root)
    window.title("Display products")
    window.geometry("500x500")

    products = display_products()
    table = print_table(products)
    table_label = tk.Label(window, text=table, justify="left", font=("Courier", 10))

    table_label.pack()

root = tk.Tk()
root.geometry("500x500")

title_label = tk.Label(root, text="INVENTORY MANAGEMENT SYSTEM", font=("Arial", 20))
title_label.pack(pady=10)

add_product_button = tk.Button(root, text="Add product", command=add_product_gui, bg='light blue', fg='black')
update_product_button = tk.Button(root, text="Update product", command=update_product_gui, bg='light green', fg='black')
delete_product_button = tk.Button(root, text="Delete product", command=delete_product_gui, bg='light yellow', fg='black')
display_products_button = tk.Button(root, text="Display products", command=display_products_gui, bg='light gray', fg='black')

add_product_button.pack(pady=10)
update_product_button.pack(pady=10)
delete_product_button.pack(pady=10)
display_products_button.pack(pady=10)



root.mainloop()

db.close()
