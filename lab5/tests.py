from modelle.Classe import Dish, Customer, Order
from repository.Repo import *
from controller.Controller import RestaurantController

def test_add_dish():
    dish_repo = DishRepo("dishes.JSON")
    controller = RestaurantController(dish_repo, None, None, None, None)

    dish = Dish(5, "New Dish", 300, 14.99)
    controller.add_dish(dish)

    dishes = controller.get_all_dishes()

    assert any(
        d.id == dish.id and d.name == dish.name and d.portion_size == dish.portion_size and d.price == dish.price for d
        in dishes)

def test_search_customer_by_name():
    # Test searching for a customer by name
    customer_repo = CustomerRepo("customers.JSON")
    controller = RestaurantController(None, None, None, customer_repo, None)

    customers = controller.get_all_customers()
    result = controller.search_customer_by_name(customers, "John")
    expected_result = [Customer(1, "John Doe", "123 Main St")]

    assert any("John" in r.name for r in result)

def test_search_customer_by_address():
    customer_repo = CustomerRepo("customers.json")
    controller = RestaurantController(None, None, None, customer_repo, None)

    customers = controller.get_all_customers()
    result = controller.search_customer_by_address(customers, "456")
    expected_result = [Customer(2, "Jane Smith", "456 Oak Ave")]

    assert any("456" in r.address for r in result)


def test_update_customer_name():
    customer_repo = CustomerRepo("customers.JSON")
    controller = RestaurantController(None, None, None, customer_repo, None)

    customers = controller.get_all_customers()
    updated_customer = Customer(1, "John Updated", "123 Main St")

    controller.update_customer(updated_customer.id, updated_customer)

    customers = controller.get_all_customers()


    assert any(
        customer.id == updated_customer.id and
        customer.name == updated_customer.name and
        customer.address == updated_customer.address
        for customer in customers
    )
def test_generate_bill_string():

    controller = RestaurantController(
        DishRepo("dishes.json"),
        CookedDishRepo("cooked_dishes.json"),
        DrinkRepo("drinks.json"),
        CustomerRepo("customers.json"),
        OrderRepo("orders.json")
    )

    order_id = 1

    bill_string = controller.generate_bill_string(order_id)


    assert "Total Amount:" in bill_string

def test_save_and_load_order_instance():
    controller = RestaurantController(DishRepo("dishes.json"), CookedDishRepo("cooked_dishes.JSON"),
                                     DrinkRepo("drinks.json"), CustomerRepo("customers.JSON"), OrderRepo("orders.JSON"))

    sample_order = Order(99, 1, [1, 2], [], [1])

    controller.save_order_instance(sample_order)

    loaded_order = controller.load_order_instance(sample_order.id)


    assert loaded_order == sample_order


def test_load_and_convert_order_instance():

    controller = RestaurantController(DishRepo("dishes.json"), CookedDishRepo("cooked_dishes.JSON"),
                                     DrinkRepo("drinks.json"), CustomerRepo("customers.JSON"), OrderRepo("orders.JSON"))

    sample_order = Order(99, 1, [1, 2], [], [1])

    controller.save_order_instance(sample_order)

    loaded_and_converted_order = controller.load_and_convert_order_instance(sample_order.id)

    assert loaded_and_converted_order == sample_order


if __name__ == "__main__":
    test_add_dish()
    test_search_customer_by_name()
    test_search_customer_by_address()
    test_update_customer_name()
    test_generate_bill_string()
    test_save_and_load_order_instance()
    test_load_and_convert_order_instance()

