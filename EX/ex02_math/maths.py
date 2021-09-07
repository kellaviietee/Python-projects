"""Math."""
import math


def ects(ects, weeks):
    """
    Implement a function to know how many hours are needed per week if each ECTS is 26 hours.

    If it's not possible in time then return a string "Impossible!".

    Examples:
    1. ects(30, 12) == 65
    2. ects(1, 1) == 26
    3. ects(1, 0) == "Impossible!"
    """
    if weeks <= 0:
        return "Impossible!"
    total_hours_per_week = 7 * 24
    total_hours_for_ects = ects * 26
    hours_per_week = total_hours_for_ects / weeks
    if hours_per_week > total_hours_per_week:
        return "Impossible!"
    else:
        return hours_per_week


def average(a, b, c, d):
    """
    Implement a function that has 4 numeric parameters.

    Each parameter must be multiplied by number of its position
    in the function (x, y, z = 1, 2, 3). Calculate and return the average.

    Examples:
    1. average(0, 0, 0, 4) === 4
    2. average(1, 2, 3, 4) == 7.5
    3. average(5, 0, 5, 1) == 6
    """
    return (1 * a + 2 * b + 3 * c + 4 * d) / 4


def clock(days, hours, minutes, seconds):
    """
    Implement a function that has 4 numeric parameters.

    The values are: days, hours, minutes, seconds. Calculate how many minutes are in total and return the value.

    Examples:
    1. clock(1, 24, 60, 60) === 2941
    3. clock(0, 0, 0, 60) == 1
    3. clock(0, 0, 1, 60) == 2
    """
    return days * 24 * 60 + hours * 60 + minutes + math.floor(seconds / 60)
