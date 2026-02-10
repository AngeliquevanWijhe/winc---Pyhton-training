
from datetime import datetime as dt

class PizzaOrder:
    def __init__(self, customer_name, pizza_type, toppings, order_time=None, is_delivered=False):
        """Initialize a pizza order."""
        self.customer_name = customer_name
        self.pizza_type = pizza_type
        self.toppings = toppings
        self.order_time = order_time if order_time else dt.now()
        self.is_delivered = is_delivered

    def __str__(self):
        """String representation for saving/printing."""
        toppings_str = ", ".join(self.toppings) if self.toppings else "None"
        return f"{self.customer_name} | {self.pizza_type} | {toppings_str} | {self.order_time.strftime('%Y-%m-%d %H:%M:%S')} | Delivered: {self.is_delivered}+/n"

    @classmethod
    def create_order(order):
        """Create a PizzaOrder interactively from user input."""
        customer_name = input("What is your name? ").strip()
        pizza_type = input("Which pizza would you like? ").strip()
        toppings = input("Please select toppings (comma-separated): ").strip().split(",")
        toppings = [t.strip() for t in toppings if t.strip()]  # Clean up list
        return order(customer_name, pizza_type, toppings)

    @staticmethod
    def save_orders_to_file(order_list, filename="orders.txt"):
        """Save a list of PizzaOrder objects to a file."""
        if not isinstance(order_list, list):
            raise ValueError("order_list must be a list of PizzaOrder objects.")

        try:
            with open(filename, "w", encoding="utf-8") as file:
                for order in order_list:
                    if isinstance(order, PizzaOrder):
                        file.write(str(order) + "\n")
                    else:
                        raise ValueError("All items in order_list must be PizzaOrder instances.")
            print(f"✅ Orders saved successfully to {filename}")
        except Exception as e:
            print(f"❌ Error saving orders: {e}")


# Example usage:
if __name__ == "__main__":
    orders = []
    order1 = PizzaOrder.create_order()
    orders.append(order1)

    # Save to file
    PizzaOrder.save_orders_to_file(orders)


