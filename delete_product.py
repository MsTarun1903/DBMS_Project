from prettytable import PrettyTable
import mysql.connector
import tkinter as tk
from tkinter import messagebox

db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

cursor = db.cursor()

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

delete_product_button = tk.Button(root, text="Delete product", command=delete_product_gui)
display_products_button = tk.Button(root, text="Display products", command=display_products_gui)

delete_product_button.pack()
display_products_button.pack()

root.mainloop()

db.close()