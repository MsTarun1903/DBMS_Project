import mysql.connector

def connect_to_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Tarun@123",
        database="inventory_db"
    )
    return db