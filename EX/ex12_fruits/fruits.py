"""Fruits delivery application."""


class Product:
    """Product class."""

    def __init__(self, name, price):
        """
        Product constructor.

        Expected name and price parameters.
        """
        self.name = name
        self.price = price


class Order:
    """Order class."""

    def __init__(self, customer: str = "customer", products: dict = {}):
        """
        Order constructor.

        Expected default customer parameter starting from Part 3. Also, products dictionary
        is expected to be created and products names set as a helper.
        """
        self.customer = customer
        self.products = products

    def get_products(self):
        return self.products

    def get_products_string(self) -> str:
        """
        Method for converting products to a string.

        The template for a single product conversion into a string is 'product_name: product_amount kg'.
        If there are several products in the resulting string, separate them with a comma and space, but in the end
        of such long string there should be no comma, nor string. Example:
        'Avocado: 2 kg, Orange: 1 kg, Papaya: 3 kg, Cherry tomato: 2 kg'
        """
        pass

    def add_product(self, product):
        """Method for adding a single product to the dictionary."""
        current_products = self.get_products()
        if product[0] in current_products:
            self.products[product[0]] += product[1]
        else:
            self.products[product[0]] = product[1]

    def add_products(self, products):
        """Method for adding several products to the dictionary."""
        for product in products:
            current_products = self.get_products()
            if product[0] in current_products:
                self.products[product[0]] += product[1]
            else:
                self.products[product[0]] = product[1]


class App:
    """
    App class.

    Represents our app, which should remember, which customer ordered what (starting from Part 3).
    Also, this is the place (interface) from where orders should be composed.
    """

    def __init__(self):
        """App constructor, no arguments expected."""
        self.customers = []
        self.products = self.import_products("pricelist.txt")

    def find_product_by_name(self, name: str):
        all_products = self.products
        for product in all_products:
            if product.name == name:
                return product

    def get_products(self) -> list:
        """Getter for products list."""
        return self.products

    def get_orders(self) -> list:
        """Getter for orders list."""
        pass

    def import_products(self, filename: str) -> list[Product]:
        """
        Import products from a file, return list of Product objects.

        Filename is an argument here.
        """
        product_list = []
        with open(filename) as f:  # Opens file with name of "test.txt"
            data = f.read()  # Reads all the lines from the file and saves it as a string.
        data_list = data.splitlines()
        for item in data_list:
            name_price = item.split(" -")
            new_product = Product(name_price[0], float(name_price[1]))
            product_list.append(new_product)
        return product_list

    def order_products(self):
        """Order products in general.

        The parameter is list of products. Create a new order, then add passed products to
        this order, then add this order to the orders list.
        Products here is list of tuples.
        """
        pass

    def order(self, name: str, orders: tuple):
        """
        Method for ordering products for a customer.

        Products here is list of tuples.
        """
        pass

    def add_customer(self, customer):
        """Method for adding a customer to the list."""
        self.customers.append(customer)

    def add_customers(self, customers: list):
        """Method for adding several customers to the list."""
        for customer in customers:
            self.customers.append(customer)

    def show_all_orders(self) -> str:
        """
        Method for returning all orders for all customers.

        If is_summary is true, add totals for each customer
        and also global total price.
        """
        pass

    def calculate_total(self) -> float:
        """Method for calculating total price for all customer's orders."""
        pass

    def calculate_summary(self):
        """Method for printing a summary of all orders with totals and the total for all customers' all orders."""
        pass


class Customer:
    """Customer to implement."""

    def __init__(self, name: str, address: str, orders: list = []):
        """App constructor, no arguments expected."""
        self.name = name
        self.address = address
        self.orders = orders

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_orders(self):
        return self.orders


if __name__ == '__main__':
    app = App()
    # Adding default customers to our app.
    app.add_customers([Customer("Anton", "home"), Customer("Rubber Duck", "home-table"), Customer("Svetozar", "Dorm 1"),
                       Customer("Toivo", "Dorm 2"), Customer("Muhhamad", "Muhha's lair"), Customer("test", "TEST")])
    # Ordering some food for everyone.
    app.order("Anton", [("Avocado", 2), ("Orange", 1), ("Papaya", 3), ("Cherry tomato", 2)])
    app.order("Anton", [("Avocado", 4), ("Orange", 2), ("Papaya", 3), ("Cherry tomato", 2)])
    app.order("Rubber Duck", [("Mango Irwin", 6)])
    app.order("Svetozar", [("Lemon", 1)])
    app.order("Svetozar", [("Grapefruit", 10)])
    app.order("Muhhamad", [("Grenades", 13), ("Cannon", 1), ("Red pepper", 666)])
    app.order("Toivo", [("Granadilla", 3), ("Chestnut", 3), ("Pitaya(Dragon Fruit)", 3)])
    # Checking products dictionary format (we want numeric price, not string).
    print(app.get_products())
    print("=======")
    # Checking how all orders and summary look like.
    print(app.show_all_orders(False))
    print("=======")
    print(app.show_all_orders(True))
    print("=======")
    app.calculate_summary()
