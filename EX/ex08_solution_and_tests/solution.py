"""Here be exercises"""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
   Check if the conditions are right for studying.

   :param time: Study time in 24h clock time
   :param coffee_needed: is the coffee needed
   :return: Return True if students study in given circumstances.
   """
    if time is None or coffee_needed is None:
        return False
    if (18 <= time <= 24) and not coffee_needed:
        return True
    elif (5 <= time <= 17) and coffee_needed:
        return True
    elif 1 <= time <= 4:
        return False
