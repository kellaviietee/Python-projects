class Factory:
    def __init__(self):
        self.all_cakes = []

    def bake_cake(self, toppings: int, base: int) -> int:
        cake_types = [5, 2, 1]
        how_many_cakes = 0
        ingredients = base
        for cake_type in cake_types:
            while ingredients >= cake_type:
                if cake_type == 5:
                    new_cake = Cake(5, 5)
                    self.all_cakes.append(new_cake)
                if cake_type == 2:
                    new_cake = Cake(2, 2)
                    self.all_cakes.append(new_cake)
                if cake_type == 1:
                    new_cake = Cake(1, 1)
                    self.all_cakes.append(new_cake)
                how_many_cakes += 1
                ingredients -= cake_type
        return how_many_cakes

    def get_last_cakes(self, n: int) -> list:
        return self.all_cakes[len(self.all_cakes) - n: len(self.all_cakes)]

    def get_cakes_baked(self) -> list:
        return self.all_cakes

    def __str__(self):
        if len(self.all_cakes) == 1:
            return f"Factory with {len(self.all_cakes)} cake."
        else:
            return f"Factory with {len(self.all_cakes)} cakes."


class Cake:

    def __init__(self, base_amount, toppings_amount):
        if (base_amount, toppings_amount) == (1, 1):
            self.type_of_cake = "basic"
        elif (base_amount, toppings_amount) == (2, 2):
            self.type_of_cake = "medium"
        elif (base_amount, toppings_amount) == (5, 5):
            self.type_of_cake = "large"
        else:
            raise WrongIngredientsAmountException(Exception)

    @property
    def type(self):
        return self.type_of_cake

    def __repr__(self):
        rep = f"Cake({self.type})"
        return rep

    def __eq__(self, other):
        return self.type == other.type


class WrongIngredientsAmountException(Exception):
    pass
