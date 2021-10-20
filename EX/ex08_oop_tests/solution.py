"""Week 8 exercises, testing."""


class Factory:
    """Factory that bakes cakes."""

    def __init__(self):
        """Initialize the factory."""
        self.all_cakes = []

    def bake_cake(self, toppings: int, base: int) -> int:
        """
        Bake a cake in a factory giving out basic, medium and large cakes.

        :param toppings: How much toppings does the Factory have to work with
        :param base: How many cake bases does factory have.
        :return: Number of cakes the Factory produces.
        """
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
        """
        Get the n last cakes that factory made.

        :param n: How many of the last cakes you interested.
        :return: List of cakes that were made.
        """
        return self.all_cakes[len(self.all_cakes) - n: len(self.all_cakes)]

    def get_cakes_baked(self) -> list:
        """
        Get all the cakes that are currently present at the factory.

        :return:
        """
        return self.all_cakes

    def __str__(self):
        """How is factory called."""
        if len(self.all_cakes) == 1:
            return f"Factory with {len(self.all_cakes)} cake."
        else:
            return f"Factory with {len(self.all_cakes)} cakes."


class Cake:
    """A pretty cake."""

    def __init__(self, base_amount, toppings_amount):
        """
        Determine what kind of cake it is.

        :param base_amount: How big of a base it has.
        :param toppings_amount: How much toppings there is.
        """
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
        """Get the cake type."""
        return self.type_of_cake

    def __repr__(self):
        """How is the cake represented."""
        rep = f"Cake({self.type})"
        return rep

    def __eq__(self, other):
        """
        See if two cakes are the same.

        :param other: Cake you are comparing.
        :return: If they are the same cake or not.
        """
        return self.type == other.type


class WrongIngredientsAmountException(Exception):
    """The ingredients are wrong you doofus."""

    pass
