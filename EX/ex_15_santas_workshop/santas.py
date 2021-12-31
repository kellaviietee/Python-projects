"""Santa's Workshop."""
import csv
import urllib.request
import urllib.parse
import urllib.error
import json

URL_ADDRESS = "http://api.game-scheduler.com:8089/gift?"


class Child:
    def __init__(self, name: str, nice=None, naughty=None, wishlist=None, country=None):
        self.country = country
        self.wishlist = wishlist
        self.naughty = naughty
        self.nice = nice
        self.name = name

    def __repr__(self):
        return f"{self.name} from {self.country}"


class ChildrenLists:
    def __init__(self, nice_filename: str, naughty_filename: str, wish_list):
        self.all_children = {}
        self.nice_children = self.read_list_from_file(nice_filename, "nice")
        self.naughty_children = self.read_list_from_file(naughty_filename, "naughty")
        self.wish_list = wish_list

    def read_list_from_file(self, filename: str, list_type: str) -> list[Child]:
        children = []
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # Loops over each line in file.
            for row in csv_reader:
                if row[0] not in self.all_children:
                    person = Child(row[0], country=row[1])
                    if list_type == "nice":
                        person.nice = True
                    if list_type == "naughty":
                        person.naughty = True
                    children.append(person)
                    self.all_children[row[0]] = person
                else:
                    person = self.all_children[row[0]]
                    if list_type == "nice":
                        person.nice = True
                    if list_type == "naughty":
                        person.naughty = True
                    children.append(person)
        return children


class Product:
    def __init__(self, name: str, material_cost: int, production_time: int, weight: int):
        self.weight = weight
        self.production_time = production_time
        self.material_cost = material_cost
        self.name = name

    def __repr__(self):
        return f"{self.name}: {self.weight}g"


class Warehouse:
    def __init__(self):
        self.products = {}

    def get_product_from_factory(self, name: str) -> Product:
        query = urllib.parse.urlencode({"name": name})
        try:
            with urllib.request.urlopen(URL_ADDRESS + query) as f:
                contents = f.read()
                print(contents.decode("utf-8"))
                data = json.loads(contents.decode("utf-8"))
                if data["gift"] not in self.products:
                    new_product = Product(data["gift"], data["material_cost"],
                                          data["production_time"], data["weight_in_grams"])
                    data["gift"] = new_product
                    return new_product
                else:
                    return data["gift"]
        except urllib.error.HTTPError:
            return None


if __name__ == "__main__":
    new_warehouse = Warehouse()
    print(new_warehouse.get_product_from_factory("new phone"))
    children_list = ChildrenLists("ex15_nice_list.csv", "ex15_naughty_list.csv", "ex15_wish_list")

