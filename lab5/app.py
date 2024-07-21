from ui.UI import RestaurantUI
from controller.Controller import RestaurantController
from repository.Repo import DishRepo, CookedDishRepo, DrinkRepo, CustomerRepo, OrderRepo

def main():
    # Erstelle Instanzen der Repository-Klassen für verschiedene Datenarten (Gerichte, gekochte Gerichte, Getränke, Kunden, Bestellungen)
    dish_repo = DishRepo('dishes.json')
    cooked_dish_repo = CookedDishRepo('cooked_dishes.json')
    drink_repo = DrinkRepo('drinks.json')
    customer_repo = CustomerRepo('customers.json')
    order_repo = OrderRepo('orders.json')

    # Erstelle eine Instanz des Controllers und übergebe die erstellten Repository-Instanzen
    controller = RestaurantController(dish_repo, cooked_dish_repo, drink_repo, customer_repo, order_repo)

    # Erstelle eine Instanz der Benutzeroberflächenklasse und übergebe die Controller-Instanz
    restaurant_ui = RestaurantUI(controller)

    # Starte die Benutzeroberfläche
    restaurant_ui.run()


main()
