import tkinter as tk
from tkinter import messagebox
from db import Database
from models import Customer


class Application(tk.Tk):


    def __init__(self):
        super().__init__()
        self.title("Система учёта заказов")


        self.create_widgets()

    def create_widgets(self):


        tk.Label(self, text="Имя клиента:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)
        tk.Label(self, text="Email клиента:").grid(row=1, column=0)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=1, column=1)

        tk.Label(self, text="Телефон клиента:").grid(row=2, column=0)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=2, column=1)

        tk.Button(self, text="Добавить клиента", command=self.add_customer).grid(row=3, columnspan=2)

    def add_customer(self):

        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if not name or not email or not phone:
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены.")
            return

        customer = Customer(name, email, phone)

        db = Database()
        db.add_customer(customer)

        messagebox.showinfo("Успех", "Клиент добавлен!")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
