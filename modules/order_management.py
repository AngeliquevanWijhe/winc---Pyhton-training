from datetime import datetime as dt

class PizzaOrder:
    def __init__(self, customer_name, pizza_type, toppings, order_time = None, is_delivered=False):
        self.customer_name = customer_name
        self.pizza_type = pizza_type
        self.toppings = toppings
        self.order_time = order_time if order_time else dt.now()
        self.is_delivered = is_delivered
   
    def __str__(self):
        """String representation for saving/printing."""
        toppings_str = ", ".join(self.toppings) if self.toppings else "None"
        return f"{self.customer_name} | {self.pizza_type} | {toppings_str} | {self.order_time.strftime('%Y-%m-%d %H:%M:%S')} | Delivered: {self.is_delivered}"

    @classmethod
    def create_order(cls):
        customer_name = input("What is your name?")
        pizza_type=input("Which pizza would you like?")
        toppings=input("Please select toppings (comma-seperated)").split(",")
                
        print("\n--- Order Summary ---")
        print(f"Customer: {customer_name}")
        print(f"Pizza: {pizza_type}")
        print(f"Toppings: {toppings}")
        return cls(customer_name, pizza_type, toppings)

    @staticmethod
    def save_orders_to_file(order_list, filename="orders.txt"):
        if not isinstance(order_list, list):
            raise ValueError("order_list must be a list of PizzaOrder objects.")

        try:
            with open(filename, "a", encoding="utf-8") as file:
                for order in order_list:
                    if isinstance(order, PizzaOrder):
                        file.write(str(order) + "\n")
                    else:
                        raise ValueError("All items in order_list must be PizzaOrder instances.")
            print(f"Orders saved successfully to {filename}")
        except Exception as e:
            print(f"Error saving orders: {e}")

def load_orders_from_file():
    orders = []

    try:
        with open('./orders.txt', 'r', encoding='utf-8') as file:
            for line in file:
                order_data = line.strip().split(" | ")

                if len(order_data) != 5:
                    continue

                customer_name = order_data[0]
                pizza_type = order_data[1]
                toppings = order_data[2].split(", ") if order_data[2] != "None" else []
                order_time = dt.strptime(order_data[3], '%Y-%m-%d %H:%M:%S')
                is_delivered = order_data[4].replace("Delivered: ", "") == 'True'

                order = PizzaOrder(
                    customer_name,
                    pizza_type,
                    toppings,
                    order_time,
                    is_delivered
                )

                orders.append(order)

    except FileNotFoundError:
        return []

    return orders

#Voorbeeld order laden
# orders = load_orders_from_file()
# print("Ingeladen orders:")

# for o in orders: 
#     print(o)
# print(orders)
  
 
#Voorbeeld order opslaan
# orders = []
# order1 = PizzaOrder.create_order()
# orders.append(order1)

# PizzaOrder.save_orders_to_file(orders)


  