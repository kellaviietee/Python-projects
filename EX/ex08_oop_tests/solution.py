class Factory:
    def __init__(self):
        pass

    def bake_cake(self, toppings: int, base: int) -> int:
        cake_types = [5, 2, 1]
        how_many_cakes = 0
        ingredients = base
        for cake_type in cake_types:
            while ingredients >= cake_type:
                how_many_cakes += 1
                all_cakes.append(Cake)
                ingredients -= cake_type
        return how_many_cakes

    def get_last_cakes(self, n: int) -> list:
        pass

    def get_cakes_baked(self) -> list:
        pass

    def __str__(self):
        pass


class Cake:

    def __init__(self, base_amount, toppings_amount):
        pass

    @property
    def type(self):
        return self

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass


class WrongIngredientsAmountException(Exception):
    pass
