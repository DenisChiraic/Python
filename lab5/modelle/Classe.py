from abc import ABC, abstractmethod
from functools import reduce


class Identifiable(ABC):
    def __init__(self, obj_id):
        # Initialisiert ein Objekt mit einer eindeutigen ID.
        self.id = obj_id


class Dish(Identifiable):
    def __init__(self, obj_id, name, portion_size, price):
        # Initialisiert ein Gerichtsobjekt mit ID, Namen, Portionsgröße und Preis.
        super().__init__(obj_id)
        self.name = name
        self.portion_size = portion_size
        self.price = price



class CookedDish(Dish):
    def __init__(self, obj_id, name, portion_size, price, preparation_time):
        # Initialisiert ein gekochtes Gerichtsobjekt mit ID, Namen, Portionsgröße, Preis und Zubereitungszeit.
        super().__init__(obj_id, name, portion_size, price)
        self.preparation_time = preparation_time



class Drink(Dish):
    def __init__(self, obj_id, name, portion_size, price, alcohol_content):
        # Initialisiert ein Getränkeobjekt mit ID, Namen, Portionsgröße, Preis und Alkoholgehalt.
        super().__init__(obj_id, name, portion_size, price)
        self.alcohol_content = alcohol_content


class Customer(Identifiable):
    def __init__(self, obj_id, name, address):
        # Initialisiert ein Kundenobjekt mit ID, Namen und Adresse.
        super().__init__(obj_id)
        self.name = name
        self.address = address

class Order:
    def __init__(self, obj_id, customer_id, dish_ids, cooked_dish_ids, drink_ids):
        # Initialisiert eine Bestellung mit ID, Kunden-ID und Listen von Gerichts-, gekochten Gerichts- und Getränke-IDs.
        self.id = obj_id
        self.customer_id = customer_id
        self.dish_ids = dish_ids
        self.cooked_dish_ids = cooked_dish_ids
        self.drink_ids = drink_ids

    def format_object(self, item_name, item_id, items):
        # Formatieren eines Objekts (Gericht oder Getränk) mit Namen und Preis.
        return f"{item_name} - {next(item.price for item in items if item.id == item_id)}"

    def generate_invoice(self, dishes, drinks):
        # Generierung der Rechnung unter Verwendung von Namen und IDs von ausgewählten Gerichten und Getränken.
        dish_names = [dish.name for dish in dishes if dish.id in self.dish_ids or dish.id in self.cooked_dish_ids]
        drink_names = [drink.name for drink in drinks if drink.id in self.drink_ids]

        # Mapping: Formatieren von Gerichten und Getränken in Stringrepräsentationen.
        formatted_dishes = map(lambda x: self.format_object(*x),
                               zip(dish_names, self.dish_ids, [dishes] * len(self.dish_ids)))

        formatted_drinks = map(lambda x: self.format_object(*x),
                               zip(drink_names, self.drink_ids, [drinks] * len(self.drink_ids)))

        # Zusammenführung aller formatierten Objekte in eine Liste von Strings.
        all_objects_strings = list(formatted_dishes) + list(formatted_drinks)

        # Erstellung der Rechnung mit ID, formatierten Objekten und Gesamtkosten.
        invoice_string = f"Order ID: {self.order_id}\n"
        invoice_string += "\n".join(all_objects_strings)
        invoice_string += f"\nTotal Cost: {self.calculate_cost(dishes, drinks)} €"

        return invoice_string

    def calculate_cost(self, dishes, drinks):
        # Berechnung der Gesamtkosten unter Verwendung der Preise von ausgewählten Gerichten und Getränken.
        dish_prices = [dish.price for dish in dishes if dish.id in self.dish_ids or dish.id in self.cooked_dish_ids]
        drink_prices = [drink.price for drink in drinks if drink.id in self.drink_ids]

        # Zusammenführung aller Preise.
        all_prices = dish_prices + drink_prices

        # Berechnung der Gesamtkosten unter Verwendung von functools.reduce.
        total_cost = reduce(lambda x, y: x + y, all_prices, 0)

        return total_cost

    def __eq__(self, other):
        if not isinstance(other, Order):
            return False

        return (
                self.id == other.id and
                self.customer_id == other.customer_id and
                self.dish_ids == other.dish_ids and
                self.cooked_dish_ids == other.cooked_dish_ids and
                self.drink_ids == other.drink_ids
        )