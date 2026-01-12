
import tkinter as tk
from tkinter import ttk, messagebox
from ec.edu.espe.fitnessgym.controller.customer_controller import CustomerController

class GUICustomer:
    def __init__(self, root):
        self.controller = CustomerController()
        self.root = root
        self.root.title("Customers Fitness Gym")

        # Tabla
        self.table = ttk.Treeview(root, columns=("ID","Name","Age","Weight","Height","BMI"), show='headings')
        for col in self.table["columns"]:
            self.table.heading(col, text=col)
        self.table.pack()

        # Botón cargar
        self.btn_load = tk.Button(root, text="Cargar Clientes", command=self.load_customers)
        self.btn_load.pack(pady=10)

        # Botón calcular total
        self.btn_total = tk.Button(root, text="Calcular Total", command=self.calculate_total)
        self.btn_total.pack(pady=10)

    def load_customers(self):
        self.table.delete(*self.table.get_children())  # limpiar tabla
        customers = self.controller.find_all_customers()
        for c in customers:
            bmi = c.calculate_bmi()
            self.table.insert("", "end", values=(c.id, c.name, c.age, c.weight, c.height, round(bmi,2)))

    def calculate_total(self):
        customers = self.controller.find_all_customers()
        total = self.controller.calculate_total_weight_height(customers)
        messagebox.showinfo("Total peso × altura", f"Total: {total:.2f}")


