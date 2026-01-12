from utils.mongodb_connection import MongoDBConnection
from model.customer import Customer

class CustomerController:
    def __init__(self):
        connection = MongoDBConnection()  # instancia de conexión
        self.db = connection.get_database("school")  # base de datos
        self.collection = self.db["Customers"]       # colección

    def insert_customer(self, customer):
        self.collection.insert_one({"id": customer.id,"name": customer.name,"age": customer.age,"weight": customer.weight,"height": customer.height})

    def find_all_customers(self):
        customers = []
        for doc in self.collection.find():
            weight = doc.get("weight") or 0
            height = doc.get("height") or 0

            customers.append(Customer(id=doc.get("id"),name=doc.get("name"),age=doc.get("age"),weight=weight,height=height))
        return customers

    def calculate_total_weight_height(self, customers):
        total = 0
        for c in customers:
            total += c.weight * c.height
        return total
