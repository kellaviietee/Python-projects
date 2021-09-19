# -*- coding: utf-8 -*-
"""ID code."""


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.

    :param text: string
    :return: string
    """
    id_code = ""
    for char in text:
        try:
            integer = int(char)
            id_code += str(integer)
        except ValueError:
            print("not an integer")
            continue
    if len(id_code) > 11:
        return "Too many numbers!"
    if len(id_code) < 11:
        return "Not enough numbers!"
    if len(id_code) == 11:
        return id_code


def is_valid_gender_number(gender_number: int) -> bool:
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    if (gender_number < 1) or (gender_number > 6):
        return False
    else:
        return True


def get_gender(gender: int) -> str:
    """
    Find a persons gender from given first number of ID - code.

    :param gender:
    :return: string
    """
    if gender % 2 == 0:
        return "female"
    else:
        return "male"


def is_valid_year_number(year_number: int) -> bool:
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    if (year_number >= 0) and year_number < 100:
        return True
    else:
        return False


def is_valid_month_number(month_number: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    if (month_number > 0) and (month_number < 13):
        return True
    else:
        return False


def is_valid_birth_number(birth_number: int):
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """
    if birth_number > 0:
        return True
    else:
        return False


def is_leap_year(year: int) -> bool:
    """
    Check in given value is a leap year.

    :param year:
    :return: bool
    """
    if year % 400 == 0:
        return True
    if (year % 400 != 0) and (year % 100 == 0):
        return False
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


def get_birth_place(birth_number: int) -> str:
    """
    Find the place where the person was born.

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-Järve, Narva, Pärnu,
    and undefined. Lastly if the number is incorrect the function must return
    the following 'Wrong input!'
    :param birth_number: int
    :return: str
    """
    if (birth_number >= 1) and (birth_number <= 10):
        return "Kuressaare"
    elif (birth_number >= 11) and (birth_number <= 20):
        return "Tartu"
    elif (birth_number >= 21) and (birth_number <= 220):
        return "Tallinn"
    elif (birth_number >= 221) and (birth_number <= 270):
        return "Kohtla-Järve"
    elif (birth_number >= 271) and (birth_number <= 370):
        return "Tartu"
    elif (birth_number >= 371) and (birth_number <= 420):
        return "Narva"
    elif (birth_number >= 421) and (birth_number <= 470):
        return "Pärnu"
    elif (birth_number >= 471) and (birth_number <= 710):
        return "Tallinn"
    elif (birth_number >= 711) and (birth_number <= 999):
        return "undefined"
    else:
        return "Wrong input!"


def get_full_year(gender_number: int, year_number: int) -> int:
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year_number: int
    :return: int
    """
    if gender_number == 1 or gender_number == 2:
        return 1800 + year_number
    elif gender_number == 3 or gender_number == 4:
        return 1900 + year_number
    else:
        return 2000 + year_number


def is_valid_control_number(id_code: str) -> bool:
    """
    Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    total = 0
    first_class_weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    second_class_weights = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    for pos in range(len(id_code) - 1):
        additive = int(id_code[pos]) * (first_class_weights[pos])
        total += additive
    remain = total % 11
    if remain == 10:
        total = 0
        for pos in range(len(id_code) - 1):
            additive = int(id_code[pos]) * (second_class_weights[pos])
            total += additive
        remain = total % 11
        if remain == 10:
            remain = 0
    if remain == int(id_code[10]):
        return True
    else:
        return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """
    Check if given value is correct for day number in ID code.

    Also, consider leap year and which month has 30 or 31 days.

    :param gender_number: int
    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    gender = get_gender(gender_number)
    full_year = get_full_year(gender, year_number)
    leap_year = is_leap_year(full_year)
    if month_number < 1 or month_number > 12:
        return False
    else:
        if month_number == 2:
            if leap_year:
                if day_number <= month_days[month_number - 1] + 1:
                    return True
            elif not leap_year:
                if day_number <= month_days[month_number - 1]:
                    return True
            return False
        else:
            if day_number <= month_days[month_number - 1]:
                return True
            else:
                return False


def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).

    Complete other functions before starting to code this one.
    You should use the functions you wrote before in this function.
    :param id_code: str
    :return: boolean
    """
    pass


def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """
    pass


if __name__ == '__main__':
    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True
