"""Here be exercises."""
import math


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Check if the conditions are right for studying.

    :param time: Time of day in 24 hour.
    :param coffee_needed: Is student drinking coffee or not.
    :return:
    """
    if 18 <= time <= 24:
        return True
    elif (5 <= time <= 17) and coffee_needed:
        return True
    elif 1 <= time <= 4:
        return False
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == 5 and c == 5:
        return 10
    elif a == b and b == c:
        return 5
    elif a != b and a != c:
        return 1
    else:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if small_baskets + 5 * big_baskets < ordered_amount:
        return -1
    else:
        needed_big = math.floor(ordered_amount / 5)
        how_many_are_covered = min(needed_big, big_baskets)
        remaining_amount = ordered_amount - 5 * how_many_are_covered
        if remaining_amount > small_baskets:
            return -1
        else:
            return min(small_baskets, remaining_amount)


print(fruit_order(10, 0, 9))
