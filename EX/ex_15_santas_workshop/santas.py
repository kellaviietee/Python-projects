"""Santa's Workshop."""
import csv
import urllib.request
import urllib.parse
import json

URL_ADDRESS = " http://api.game-scheduler.com:8089/gift?"


class Product:
    def __init__(self, name: str, material_cost: int, production_time: int, weight: int):
        self.weight = weight
        self.production_time = production_time
        self.material_cost = material_cost
        self.name = name


def get_product_from_factory(name: str) -> Product:
    query = urllib.parse.urlencode({"name": name})
    with urllib.request.urlopen(URL_ADDRESS + query) as f:
        contents = f.read()
        print(contents.decode("utf-8"))
        data = json.loads(contents.decode("utf-8"))
        new_product = Product(data["gift"], data["material_cost"], data["production_time"], data["weight_in_grams"])
        return new_product


class Warehouse:
    def __init__(self, nice_filename: str, naughty_filename: str, wish_filename: str):
        self.nice_list = self.read_list_from_file(nice_filename)
        self.naughty_list = self.read_list_from_file(naughty_filename)
        self.wish_list = self.read_list_from_file(wish_filename)

    def read_list_from_file(self, filename: str) -> list:
        person_data = []
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # Loops over each line in file.
            for row in csv_reader:
                # Prints the list of strings in that line.
                person_data.append(row)
        return person_data


if __name__ == "__main__":
    new_warehouse = Warehouse("ex15_nice_list.csv", "ex15_naughty_list.csv", "ex15_wish_list.csv")
    get_product_from_factory("swimming flippers")
