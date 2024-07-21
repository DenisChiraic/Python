import json
from abc import ABC, abstractmethod
from modelle.Classe import *

class DataRepo(ABC):
    def __init__(self, file):
        # Initialisiert ein Datenrepository mit dem angegebenen Dateipfad.
        self.file = file

    @abstractmethod
    def save(self, data):
        # Speichert Daten im Repository.
        pass

    @abstractmethod
    def load(self):
        # Lädt Daten aus dem Repository.
        pass

    def read_file(self):
        # Liest den Inhalt der Datei.
        with open(self.file, 'r') as f:
            return f.read()

    def write_to_file(self, content):
        # Schreibt den Inhalt in die Datei.
        with open(self.file, 'w') as f:
            f.write(content)

    @abstractmethod
    def convert_to_string(self, data):
        # Konvertiert Daten in eine Stringrepräsentation.
        pass

    @abstractmethod
    def convert_from_string(self, content):
        # Konvertiert Stringrepräsentation in Daten.
        pass

class DishRepo(DataRepo):
    def save(self, dishes):
        # Speichert Gerichte im Repository.
        content = self.convert_to_string(dishes)
        self.write_to_file(content)

    def load(self):
        # Lädt Gerichte aus dem Repository.
        content = self.read_file()
        return self.convert_from_string(content)

    def convert_to_string(self, dishes):
        # Konvertiert Gerichte in JSON-Stringrepräsentation.
        serialized_dishes = [{'id': dish.id, 'name': dish.name, 'portion_size': dish.portion_size, 'price': dish.price} for dish in dishes]
        return json.dumps(serialized_dishes)

    def convert_from_string(self, content):
        # Konvertiert JSON-Stringrepräsentation in Gerichte.
        serialized_dishes = json.loads(content)
        dishes = [Dish(obj['id'], obj['name'], obj['portion_size'], obj['price']) for obj in serialized_dishes]
        return dishes
class CookedDishRepo(DataRepo):
    def save(self, cooked_dishes):
        # Speichert gekochte Gerichte im Repository.
        content = self.convert_to_string(cooked_dishes)
        self.write_to_file(content)

    def load(self):
        # Lädt gekochte Gerichte aus dem Repository.
        content = self.read_file()
        return self.convert_from_string(content)

    def convert_to_string(self, cooked_dishes):
        # Konvertiert gekochte Gerichte in JSON-Stringrepräsentation.
        serialized_cooked_dishes = [
            {'id': dish.id, 'name': dish.name, 'portion_size': dish.portion_size, 'price': dish.price, 'preparation_time': dish.preparation_time}
            for dish in cooked_dishes
        ]
        return json.dumps(serialized_cooked_dishes)

    def convert_from_string(self, content):
        # Konvertiert JSON-Stringrepräsentation in gekochte Gerichte.
        serialized_cooked_dishes = json.loads(content)
        cooked_dishes = [CookedDish(obj['id'], obj['name'], obj['portion_size'], obj['price'], obj['preparation_time'])
                         for obj in serialized_cooked_dishes]
        return cooked_dishes

class DrinkRepo(DataRepo):
    def save(self, drinks):
        # Speichert Getränke im Repository.
        content = self.convert_to_string(drinks)
        self.write_to_file(content)

    def load(self):
        # Lädt Getränke aus dem Repository.
        content = self.read_file()
        return self.convert_from_string(content)

    def convert_to_string(self, drinks):
        # Konvertiert Getränke in JSON-Stringrepräsentation.
        serialized_drinks = [
            {'id': drink.id, 'name': drink.name, 'portion_size': drink.portion_size, 'price': drink.price,
             'alcohol_content': drink.alcohol_content}
            for drink in drinks
        ]
        return json.dumps(serialized_drinks)

    def convert_from_string(self, content):
        # Konvertiert JSON-Stringrepräsentation in Getränke.
        serialized_drinks = json.loads(content)
        drinks = [Drink(obj['id'], obj['name'], obj['portion_size'], obj['price'], obj['alcohol_content'])
                  for obj in serialized_drinks]
        return drinks
class CustomerRepo(DataRepo):
    def save(self, customers):
        # Speichert Kunden im Repository.
        content = self.convert_to_string(customers)
        self.write_to_file(content)

    def load(self):
        # Lädt Kunden aus dem Repository.
        content = self.read_file()
        return self.convert_from_string(content)

    def convert_to_string(self, customers):
        # Konvertiert Kunden in JSON-Stringrepräsentation.
        serialized_customers = [{'id': customer.id, 'name': customer.name, 'address': customer.address}
                                for customer in customers]
        return json.dumps(serialized_customers)

    def convert_from_string(self, content):
        # Konvertiert JSON-Stringrepräsentation in Kunden.
        serialized_customers = json.loads(content)
        customers = [Customer(obj['id'], obj['name'], obj['address']) for obj in serialized_customers]
        return customers

class OrderRepo(DataRepo):
    def save(self, orders):
        # Speichert Bestellungen im Repository.
        content = self.convert_to_string(orders)
        self.write_to_file(content)

    def load(self):
        # Lädt Bestellungen aus dem Repository.
        content = self.read_file()
        return self.convert_from_string(content)

    def convert_to_string(self, orders):
        # Konvertiert Bestellungen in JSON-Stringrepräsentation.
        serialized_orders = [{'id': order.id, 'customer_id': order.customer_id, 'dish_ids': order.dish_ids,
                              'drink_ids': order.drink_ids} for order in orders]
        return json.dumps(serialized_orders)

    def convert_from_string(self, content):
        # Konvertiert JSON-Stringrepräsentation in Bestellungen.
        serialized_orders = json.loads(content)
        orders = []

        for obj in serialized_orders:
            # Überprüfen Sie, ob 'cooked_dish_ids' in den Daten vorhanden ist
            cooked_dish_ids = obj.get('cooked_dish_ids', [])

            order = Order(obj['id'], obj['customer_id'], obj['dish_ids'], cooked_dish_ids, obj['drink_ids'])
            orders.append(order)

        return orders