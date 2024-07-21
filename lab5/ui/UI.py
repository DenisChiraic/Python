from modelle.Classe import Dish, CookedDish, Drink, Customer, Order
from repository.Repo import DishRepo, CookedDishRepo, DrinkRepo, CustomerRepo, OrderRepo
from controller.Controller import RestaurantController


class RestaurantUI:
    def __init__(self, controller):
        # Initialisiert das UI mit dem gegebenen Controller.
        self.controller = controller

    def display_menu(self):
        # Zeigt das Hauptmenü des Restaurant-Managementsystems an.
        print("Restaurant Management System")
        print("1. Dishes")
        print("2. Cooked Dishes")
        print("3. Drinks")
        print("4. Customers")
        print("5. Orders")
        print("0. Exit")

    def run(self):
        # Startet die Benutzeroberfläche und wartet auf Benutzereingaben.
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            # Verarbeitet die Benutzerauswahl basierend auf dem Hauptmenü.
            if choice == '1':
                self.manage_dishes()
            elif choice == '2':
                self.manage_cooked_dishes()
            elif choice == '3':
                self.manage_drinks()
            elif choice == '4':
                self.manage_customers()
            elif choice == '5':
                self.manage_orders()
            elif choice == '0':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_dishes(self):
        # Verwaltet die Gerichtsverwaltungsfunktionen.
        dish_id = None
        while True:
            print("\nDish Management")
            print("1. Add Dish")
            print("2. View All Dishes")
            print("3. Update Dish")
            print("4. Delete Dish")
            print("0. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                # Fügt ein neues Gericht hinzu.
                dish = Dish(
                    obj_id=int(input("Enter Dish ID: ")),
                    name=input("Enter Dish Name: "),
                    portion_size=int(input("Enter Portion Size: ")),
                    price=float(input("Enter Price: "))
                )
                self.controller.add_dish(dish)
                print("Dish added successfully!")
            elif choice == '2':
                # Zeigt alle Gerichte an.
                dishes = self.controller.get_all_dishes()
                print("All Dishes:")
                for dish in dishes:
                    print(f"ID: {dish.id}, Name: {dish.name}, Portion Size: {dish.portion_size}, Price: {dish.price}")
            elif choice == '3':
                # Aktualisiert ein vorhandenes Gericht.
                dish_id = int(input("Enter Dish ID to update: "))
                updated_dish = Dish(obj_id=dish_id,
                                    name=input("Enter New Dish Name: "),
                                    portion_size=int(input("Enter New Portion Size: ")),
                                    price=float(input("Enter New Price: ")))
                self.controller.update_dish(dish_id, updated_dish)
                print("Dish updated successfully!")
            elif choice == '4':
                # Löscht ein Gericht.
                dish_id = int(input("Enter Dish ID to delete: "))
                self.controller.delete_dish(dish_id)
                print("Dish deleted successfully!")
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")


    def manage_cooked_dishes(self):
        # Verwaltet die Funktionen für gekochte Gerichte.
        while True:
            print("\nCooked Dish Management")
            print("1. Add Cooked Dish")
            print("2. View All Cooked Dishes")
            print("3. Update Cooked Dish")
            print("4. Delete Cooked Dish")
            print("0. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                # Fügt ein neues gekochtes Gericht hinzu.
                cooked_dish = CookedDish(
                    obj_id=int(input("Enter Cooked Dish ID: ")),
                    name=input("Enter Cooked Dish Name: "),
                    portion_size=int(input("Enter Portion Size: ")),
                    price=float(input("Enter Price: ")),
                    preparation_time=int(input("Enter Preparation Time: "))
                )
                self.controller.add_cooked_dish(cooked_dish)
                print("Cooked Dish added successfully!")
            elif choice == '2':
                # Zeigt alle gekochten Gerichte an.
                cooked_dishes = self.controller.get_all_cooked_dishes()
                print("All Cooked Dishes:")
                for cooked_dish in cooked_dishes:
                    print(f"ID: {cooked_dish.id}, Name: {cooked_dish.name}, "
                          f"Portion Size: {cooked_dish.portion_size}, Price: {cooked_dish.price}, "
                          f"Preparation Time: {cooked_dish.preparation_time}")
            elif choice == '3':
                # Aktualisiert ein vorhandenes gekochtes Gericht.
                cooked_dish_id = int(input("Enter Cooked Dish ID to update: "))
                updated_cooked_dish = CookedDish(obj_id=cooked_dish_id,
                                                 name=input("Enter New Cooked Dish Name: "),
                                                 portion_size=int(input("Enter New Portion Size: ")),
                                                 price=float(input("Enter New Price: ")),
                                                 preparation_time=int(input("Enter New Preparation Time: ")))
                self.controller.update_cooked_dish(cooked_dish_id, updated_cooked_dish)
                print("Cooked Dish updated successfully!")
            elif choice == '4':
                # Löscht ein gekochtes Gericht.
                cooked_dish_id = int(input("Enter Cooked Dish ID to delete: "))
                self.controller.delete_cooked_dish(cooked_dish_id)
                print("Cooked Dish deleted successfully!")
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_drinks(self):
        # Verwaltet die Getränke-Managementfunktionen.
        while True:
            print("\nDrink Management")
            print("1. Add Drink")
            print("2. View All Drinks")
            print("3. Update Drink")
            print("4. Delete Drink")
            print("0. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                # Fügt ein neues Getränk hinzu.
                drink = Drink(
                    obj_id=int(input("Enter Drink ID: ")),
                    name=input("Enter Drink Name: "),
                    portion_size=int(input("Enter Portion Size: ")),
                    price=float(input("Enter Price: ")),
                    alcohol_content=float(input("Enter Alcohol Content: "))
                )
                self.controller.add_drink(drink)
                print("Drink added successfully!")
            elif choice == '2':
                # Zeigt alle Getränke an.
                drinks = self.controller.get_all_drinks()
                print("All Drinks:")
                for drink in drinks:
                    print(f"ID: {drink.id}, Name: {drink.name}, Portion Size: {drink.portion_size}, "
                          f"Price: {drink.price}, Alcohol Content: {drink.alcohol_content}")
            elif choice == '3':
                # Aktualisiert ein vorhandenes Getränk.
                drink_id = int(input("Enter Drink ID to update: "))
                updated_drink = Drink(obj_id=drink_id,
                                      name=input("Enter New Drink Name: "),
                                      portion_size=int(input("Enter New Portion Size: ")),
                                      price=float(input("Enter New Price: ")),
                                      alcohol_content=float(input("Enter New Alcohol Content: ")))
                self.controller.update_drink(drink_id, updated_drink)
                print("Drink updated successfully!")
            elif choice == '4':
                # Löscht ein Getränk.
                drink_id = int(input("Enter Drink ID to delete: "))
                self.controller.delete_drink(drink_id)
                print("Drink deleted successfully!")
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_customers(self):
        # Verwaltet die Kundenmanagementfunktionen.
        while True:
            print("\nCustomer Management")
            print("1. Add Customer")
            print("2. View All Customers")
            print("3. Update Customer")
            print("4. Delete Customer")
            print("0. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                # Fügt einen neuen Kunden hinzu.
                customer = Customer(obj_id=int(input("Enter Customer ID: ")),
                                    name=input("Enter Customer Name: "),
                                    address=input("Enter Customer Address: "))
                self.controller.add_customer(customer)
                print("Customer added successfully!")
            elif choice == '2':
                # Zeigt alle Kunden an.
                customers = self.controller.get_all_customers()
                print("All Customers:")
                for customer in customers:
                    print(f"ID: {customer.id}, Name: {customer.name}, Address: {customer.address}")
            elif choice == '3':
                # Aktualisiert einen vorhandenen Kunden.
                customer_id = int(input("Enter Customer ID to update: "))
                updated_customer = Customer(obj_id=customer_id,
                                            name=input("Enter New Customer Name: "),
                                            address=input("Enter New Customer Address: "))
                self.controller.update_customer(customer_id, updated_customer)
                print("Customer updated successfully!")
            elif choice == '4':
                # Löscht einen Kunden.
                customer_id = int(input("Enter Customer ID to delete: "))
                self.controller.delete_customer(customer_id)
                print("Customer deleted successfully!")
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_orders(self):
        # Verwaltet die Bestellungsmanagementfunktionen.
        while True:
            print("\nOrder Management")
            print("1. Add Order")
            print("2. View All Orders")
            print("3. Update Order")
            print("4. Delete Order")
            print("0. Back to Main Menu")

            choice = input("Enter your choice: ")

            try:
                if choice == '1':
                    # Fügt eine neue Bestellung hinzu.
                    dish_ids = [int(id) for id in input("Enter Dish IDs (comma-separated): ").split(',')]
                    cooked_dish_ids = [int(id) for id in input("Enter Cooked Dish IDs (comma-separated): ").split(',')]
                    drink_ids = [int(id) for id in input("Enter Drink IDs (comma-separated): ").split(',')]
                    order = Order(
                        obj_id=int(input("Enter Order ID:")),
                        customer_id=int(input("Enter Customer ID:")),
                        dish_ids=dish_ids,
                        cooked_dish_ids=cooked_dish_ids,
                        drink_ids=drink_ids
                    )
                    self.controller.add_order(order)
                    print("Order added successfully!")
                elif choice == '2':
                    # Zeigt alle Bestellungen an.
                    orders = self.controller.get_all_orders()
                    print("All Orders:")
                    for order in orders:
                        print(f"ID: {order.id}, Customer ID: {order.customer_id}, "
                              f"Dish IDs: {order.dish_ids}, Cooked Dish IDs: {order.cooked_dish_ids}, Drink IDs: {order.drink_ids}")
                elif choice == '3':
                    # Aktualisiert eine Bestellung an.
                    order_id = int(input("Enter Order ID to update: "))
                    dish_ids = [int(id) for id in input("Enter New Dish IDs (comma-separated): ").split(',')]
                    cooked_dish_ids = [int(id) for id in
                                       input("Enter New Cooked Dish IDs (comma-separated): ").split(',')]
                    drink_ids = [int(id) for id in input("Enter New Drink IDs (comma-separated): ").split(',')]
                    updated_order = Order(
                        obj_id=order_id,
                        customer_id=int(input("Enter New Customer ID: ")),
                        dish_ids=dish_ids,
                        cooked_dish_ids=cooked_dish_ids,
                        drink_ids=drink_ids
                    )
                    self.controller.update_order(order_id, updated_order)
                    print("Order updated successfully!")
                elif choice == '4':
                    # Löscht eine Bestellung.
                    order_id = int(input("Enter Order ID to delete: "))
                    self.controller.delete_order(order_id)
                    print("Order deleted successfully!")
                elif choice == '0':
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
