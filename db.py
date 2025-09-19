import sqlite3
import json
import csv

class Database:


    def __init__(self, db_name='orders.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                email TEXT,
                                phone TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                                id INTEGER PRIMARY KEY,
                                customer_id INTEGER,
                                FOREIGN KEY (customer_id) REFERENCES customers (id))''')
        self.connection.commit()

    def add_customer(self, customer):

        self.cursor.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)",
                            (customer.name, customer.email, customer.phone))
        self.connection.commit()

    def export_to_csv(self, filename):

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Name', 'Email', 'Phone'])
            for row in self.cursor.execute("SELECT * FROM customers"):
                writer.writerow(row)

    def close(self):

        self.connection.close()
