from modelle.Classe import *
from repository.Repo import *

class RestaurantController:
    def __init__(self, dish_repo, cooked_dish_repo, drink_repo, customer_repo, order_repo):
        # Initialisiert den Controller mit Repositories für Gerichte, gekochte Gerichte, Getränke, Kunden und Bestellungen.
        self.dish_repo = dish_repo
        self.cooked_dish_repo = cooked_dish_repo
        self.drink_repo = drink_repo
        self.customer_repo = customer_repo
        self.order_repo = order_repo

    def add_dish(self, dish):
        # Fügt ein Gericht dem Repository hinzu.
        dishes = self.dish_repo.load()
        dishes.append(dish)
        self.dish_repo.save(dishes)

    def get_all_dishes(self):
        # Ruft alle Gerichte aus dem Repository ab.
        return self.dish_repo.load()

    def update_dish(self, dish_id, updated_dish):
        # Aktualisiert ein Gericht im Repository.
        dishes = self.dish_repo.load()
        for i, dish in enumerate(dishes):
            if dish.id == dish_id:
                dishes[i] = updated_dish
                break
        self.dish_repo.save(dishes)

    def delete_dish(self, dish_id):
        # Löscht ein Gericht aus dem Repository.
        dishes = self.dish_repo.load()
        dishes = [dish for dish in dishes if dish.id != dish_id]
        self.dish_repo.save(dishes)

    def add_cooked_dish(self, cooked_dish):
        # Fügt ein gekochtes Gericht dem Repository hinzu.
        cooked_dishes = self.cooked_dish_repo.load()
        cooked_dishes.append(cooked_dish)
        self.cooked_dish_repo.save(cooked_dishes)

    def get_all_cooked_dishes(self):
        # Ruft alle gekochten Gerichte aus dem Repository ab.
        return self.cooked_dish_repo.load()

    def update_cooked_dish(self, cooked_dish_id, updated_cooked_dish):
        # Aktualisiert ein gekochtes Gericht im Repository.
        cooked_dishes = self.cooked_dish_repo.load()
        for i, cooked_dish in enumerate(cooked_dishes):
            if cooked_dish.id == cooked_dish_id:
                cooked_dishes[i] = updated_cooked_dish
                break
        self.cooked_dish_repo.save(cooked_dishes)

    def delete_cooked_dish(self, cooked_dish_id):
        # Löscht ein gekochtes Gericht aus dem Repository.
        cooked_dishes = self.cooked_dish_repo.load()
        cooked_dishes = [cooked_dish for cooked_dish in cooked_dishes if cooked_dish.id != cooked_dish_id]
        self.cooked_dish_repo.save(cooked_dishes)

    def add_drink(self, drink):
        # Fügt ein Getränk dem Repository hinzu.
        drinks = self.drink_repo.load()
        drinks.append(drink)
        self.drink_repo.save(drinks)

    def get_all_drinks(self):
        # Ruft alle Getränke aus dem Repository ab.
        return self.drink_repo.load()

    def update_drink(self, drink_id, updated_drink):
        # Aktualisiert ein Getränk im Repository.
        drinks = self.drink_repo.load()
        for i, drink in enumerate(drinks):
            if drink.id == drink_id:
                drinks[i] = updated_drink
                break
        self.drink_repo.save(drinks)

    def delete_drink(self, drink_id):
        # Löscht ein Getränk aus dem Repository.
        drinks = self.drink_repo.load()
        drinks = [drink for drink in drinks if drink.id != drink_id]
        self.drink_repo.save(drinks)

    def add_customer(self, customer):
        # Fügt einen Kunden dem Repository hinzu.
        customers = self.customer_repo.load()
        customers.append(customer)
        self.customer_repo.save(customers)

    def get_all_customers(self):
        # Ruft alle Kunden aus dem Repository ab.
        return self.customer_repo.load()

    def update_customer(self, customer_id, updated_customer):
        # Aktualisiert einen Kunden im Repository.
        customers = self.customer_repo.load()
        for i, customer in enumerate(customers):
            if customer.id == customer_id:
                customers[i] = updated_customer
                break
        self.customer_repo.save(customers)

    def delete_customer(self, customer_id):
        # Löscht einen Kunden aus dem Repository.
        customers = self.customer_repo.load()
        customers = [customer for customer in customers if customer.id != customer_id]
        self.customer_repo.save(customers)

    def add_order(self, order):
        # Fügt eine Bestellung dem Repository hinzu.
        orders = self.order_repo.load()
        orders.append(order)
        self.order_repo.save(orders)

    def get_all_orders(self):
        # Ruft alle Bestellungen aus dem Repository ab.
        return self.order_repo.load()

    def update_order(self, order_id, updated_order):
        # Aktualisiert eine Bestellung im Repository.
        orders = self.order_repo.load()
        for i, order in enumerate(orders):
            if order.id == order_id:
                orders[i] = updated_order
                break
        self.order_repo.save(orders)

    def delete_order(self, order_id):
        # Löscht eine Bestellung aus dem Repository.
        orders = self.order_repo.load()
        orders = [order for order in orders if order.id != order_id]
        self.order_repo.save(orders)

    def search_customer_by_name(self, customers, name):
        return [customer for customer in customers if name.lower() in customer.name.lower()]

    def search_customer_by_address(self, customers, address):
        return [customer for customer in customers if address in customer.address]

    def generate_bill_string(self, order_id):
        # Placeholder implementation, replace with actual logic
        orders = self.order_repo.load()
        order = next((o for o in orders if o.id == order_id), None)

        if order:
            # Replace the following line with your actual logic to calculate the total amount
            total_amount = 100.00
            return f"Bill for Order ID {order_id}\nTotal Amount: ${total_amount:.2f}"
        else:
            return "Order not found."

    def save_order_instance(self, order):
        # Placeholder implementation, replace with actual logic
        orders = self.order_repo.load()
        orders.append(order)
        self.order_repo.save(orders)

    def load_order_instance(self, order_id):
        # Placeholder implementation, replace with actual logic
        orders = self.order_repo.load()
        order = next((o for o in orders if o.id == order_id), None)
        return order

    def load_and_convert_order_instance(self, order_id):
        # Placeholder implementation, replace with actual logic
        return self.load_order_instance(order_id)