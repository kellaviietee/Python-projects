"""Testing a cake factory."""
import random
import pytest
from solution import Factory, Cake, WrongIngredientsAmountException


@pytest.fixture
def factory() -> Factory:
    """
    Get me a factory.

    :return:
    """
    return Factory()


def test_produce_cake_only_basic(factory):
    """
    Test if the factory can make a basic cake.

    :param factory:
    :return:
    """
    amount = factory.bake_cake(1, 1)
    assert amount == 1


@pytest.mark.dependency()
def test_produce_cake_only_medium(factory):
    """
    Test if the factory can make a medium cake.

    :param factory:
    :return:
    """
    assert factory.bake_cake(2, 2) == 1
    assert factory.bake_cake(4, 4) == 2


@pytest.mark.dependency()
def test_produce_cake_only_large(factory):
    """
    Test if the factory can make a large cake.

    :param factory:
    :return:
    """
    assert factory.bake_cake(5, 5) == 1
    assert factory.bake_cake(10, 10) == 2


@pytest.mark.dependency(depends=["test_produce_cake_only_medium"])
def test_produce_cake_medium_remaining_ingredients_produce_mode_cakes(factory):
    """
    Will the factory make cakes after a medium cake.

    :param factory:
    :return:
    """
    assert factory.bake_cake(3, 3) != 1
    assert factory.bake_cake(5, 5) != 2


@pytest.mark.dependency(depends=["test_produce_cake_only_large"])
def test_produce_cake_large_remaining_ingredients_produce_more_cakes(factory):
    """
    Will the factory make a cake after a large cake.

    :param factory:
    :return:
    """
    assert factory.bake_cake(6, 6) != 1
    assert factory.bake_cake(11, 11) != 2


def test_produce_cake_get_cakes(factory):
    """
    Test if the factory hands out a cake.

    :param factory:
    :return:
    """
    factory.bake_cake(1, 1)
    assert len(factory.get_cakes_baked()) == 1
    cake = factory.get_last_cakes(1)[0]
    assert cake is not None
    assert type(cake) == Cake


def test_produce_cakes_get_last_cakes(factory):
    """
    See if factory gives out n of the last cakes.

    :param factory:
    :return:
    """
    amount = factory.bake_cake(3, 3)
    assert amount == 2
    cakes = factory.get_last_cakes(2)
    assert type(cakes) == list
    assert len(cakes) == 2
    cakes = factory.get_last_cakes(1)
    assert type(cakes) == list
    assert len(cakes) == 1


def test_produce_cakes_order_medium_before(factory):
    """
    See if the last cake was a medium one.

    :param factory:
    :return:
    """
    factory.bake_cake(3, 3)
    cakes = factory.get_last_cakes(2)
    assert cakes
    assert cakes[0].type == "medium"
    assert cakes[1].type != "medium"


def test_produce_cakes_order_large_before(factory):
    """
    See if the last cake was a large one.

    :param factory:
    :return:
    """
    factory.bake_cake(6, 6)
    cakes = factory.get_last_cakes(2)
    assert cakes[0].type == "large"
    assert cakes[1].type != "large"


@pytest.mark.dependency()
def test_get_cakes_correct_amount(factory):
    """
    Check if factory makes correct amount of cakes.

    :param factory:
    :return:
    """
    factory.bake_cake(9, 9)
    assert len(factory.get_cakes_baked()) == 3


@pytest.mark.dependency()
def test_get_last_cakes_correct_amount(factory):
    """
    Check if the factory gives out the right amount of previous cakes.

    :param factory:
    :return:
    """
    factory.bake_cake(9, 9)
    for i in range(0, 3):
        assert len(factory.get_last_cakes(i)) == i


@pytest.mark.dependency(depends=["test_get_cakes_correct_amount"])
def test_get_cakes_returns_cakes(factory):
    """
    See if all the cakes are in fact cakes.

    :param factory:
    :return:
    """
    factory.bake_cake(9, 9)
    assert all(type(cake) == Cake for cake in factory.get_cakes_baked())


@pytest.mark.dependency(depends=["test_get_cakes_correct_amount"])
def test_get_last_cakes_returns_cakes(factory):
    """
    See if the last ones of the cakes are indeed cakes.

    :param factory:
    :return:
    """
    factory.bake_cake(9, 9)
    assert all(type(cake) == Cake for cake in factory.get_last_cakes(4))


@pytest.mark.dependency(depends=["test_get_cakes_correct_amount", "test_get_last_cakes_correct_amount"])
def test_produce_cakes_order(factory):
    """
    Check if the cakes are indeed produced in the right order.

    :param factory:
    :return:
    """
    factory.bake_cake(8, 8)
    assert len(factory.get_cakes_baked()) == 3
    cakes = factory.get_last_cakes(3)
    assert cakes[2].type == "basic"
    assert cakes[1].type == "medium"
    assert cakes[0].type == "large"


def test_cake_basic():
    """
    Is the cake a basic one.

    :return:
    """
    basic_cake = Cake(1, 1)
    assert basic_cake.type == "basic"


def test_cake_medium():
    """
    Is the cake a medium one.

    :return:
    """
    medium_cake = Cake(2, 2)
    assert medium_cake.type == "medium"


def test_cake_large():
    """
    Is the cake a large one.

    :return:
    """
    large_cake = Cake(5, 5)
    assert large_cake.type == "large"


def test_cake_wrong_ingredients_throws_exception():
    """
    See that you can not make a cake with wrong amount of ingredients.

    :return:
    """
    for i in {i for i in range(1000)} - {1, 2, 5}:
        with pytest.raises(WrongIngredientsAmountException):
            Cake(i, i)


def test_cake_equals():
    """
    Test that one cake is the same as the other one.

    :return:
    """
    cake_basic_1 = Cake(1, 1)
    cake_basic_2 = Cake(1, 1)
    cake_medium_1 = Cake(2, 2)
    cake_medium_2 = Cake(2, 2)
    cake_large_1 = Cake(5, 5)
    cake_large_2 = Cake(5, 5)
    assert cake_basic_1 == cake_basic_2
    assert cake_medium_1 == cake_medium_2
    assert cake_large_1 == cake_large_2


def test_cake_repr():
    """
    Who is the representative of these cakes.

    :return:
    """
    cake_basic = Cake(1, 1)
    cake_medium = Cake(2, 2)
    cake_large = Cake(5, 5)
    assert cake_basic.__repr__() == "Cake(basic)"
    assert cake_medium.__repr__() == "Cake(medium)"
    assert cake_large.__repr__() == "Cake(large)"


def test_factory_str_amount(factory):
    """
    Is the factory saying it has the right amount of cakes.

    :param factory:
    :return:
    """
    num = random.randint(3, 1000)
    for x in [(1, 1) for _ in range(2, num)]:
        factory.bake_cake(*x)
    assert str(factory) == f"Factory with {num - 2} cakes."


def test_factory_str_single(factory):
    """
    If factory has a single cake it has a single one, not multiple cakes.

    :param factory:
    :return:
    """
    factory.bake_cake(1, 1)
    assert str(factory) == "Factory with 1 cake."
