"""Here be exercises"""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
   Check if the conditions are right for studying.

   :param time: Study time in 24h clock time
   :param coffee_needed: is the coffee needed
   :return: Return True if students study in given circumstances.
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
    elif a != b and a != c and b != c:
        return 1
    else:
        return 0

