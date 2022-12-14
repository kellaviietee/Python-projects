# -*- coding: utf-8 -*-
"""ID code."""
import math


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


def is_valid_birth_number(birth_number: int) -> bool:
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """
    if 0 < birth_number < 1000:
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

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-J??rve, Narva, P??rnu,
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
        return "Kohtla-J??rve"
    elif (birth_number >= 271) and (birth_number <= 370):
        return "Tartu"
    elif (birth_number >= 371) and (birth_number <= 420):
        return "Narva"
    elif (birth_number >= 421) and (birth_number <= 470):
        return "P??rnu"
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
    if len(id_code) != 11:
        return False
    if not check_if_id_has_letters_in_it(id_code):
        return False
    if is_valid_gender_number(int(id_code[0])):
        if is_valid_year_number(int(id_code[1:3])):
            if is_valid_month_number(int(id_code[3:5])):
                if is_valid_day_number(int(id_code[0]), int(id_code[1:3]), int(id_code[3:5]), int(id_code[5:7])):
                    if is_valid_birth_number(int(id_code[7:10])):
                        if is_valid_control_number(id_code):
                            return True
    return False


def check_if_id_has_letters_in_it(id_code: str) -> bool:
    """
    Check if  given ID code contains only numbers.

    :param id_code:
    :return: bool
    """
    for char in id_code:
        try:
            int(char)
        except ValueError:
            return False
    return True


def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """
    if not is_id_valid(id_code):
        return "Given invalid ID code!"
    else:
        gender = get_gender(int(id_code[0]))
        day = id_code[5:7]
        month = id_code[3:5]
        full_year = get_full_year(int(id_code[0]), int(id_code[1:3]))
        birth_place = get_birth_place(int(id_code[7:10]))
        return f"This is a {gender} born on {day}.{month}.{full_year} in {birth_place}."


def generate_id_code(start_id_code: str, control_number: str, weight: int = -1) -> str:
    """
    Generate full id-code based on the given numbers.
    Given the first 7 numbers (gender + day of birth) and the control sum,
    find the birth number.
    The returned id code should contain the given numbers (first 7 and the last)
    and a birth number so that the id code is valid.
    The given numbers themselves are valid (ie there's no wrong day etc).

    The optional step parameter.

    If the third argument is not passed to the function, there are no limits.
    If the third argument is 1,
    the result id code should come after the first round of weights.
    This means that after calculating the sum with the first weights
    and taking the modulo of 11, the result cannot be 10.
    If the third argument is 2,
    the result id code should come after the second round of weights.
    But the modulo of the sum cannot be 10 with the second round weights.
    If the third argument is 3,
    the result id code should come when the second round calculation
    results with 10 (meaning the control number is 0).

    There are usually several possible id codes, any will do.

    generate_id_code("3910606", "1") => "39106060041" or "39106068921" etc
    generate_id_code("3910702", "5") => "39107020035"
    generate_id_code("3910702", "5", 1) => "39107020095"
    generate_id_code("6010607", "0", 2) => "60106078620"
    generate_id_code("5050505", "0", 3) => "50505053660"

    """
    first_class_weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    second_class_weights = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    if weight == -1:
        total_sum = 0
        for pos in range(0, 7):
            num = first_class_weights[pos] * int(start_id_code[pos])
            total_sum += num
        remain = (total_sum - int(control_number)) % 11
        if 0 < remain < 3:
            remain += 11
        equal_dist = math.floor(remain / 3)
        print(equal_dist, equal_dist, remain - 2 * equal_dist)
        final_id_code = start_id_code + str(equal_dist) + str(equal_dist) + str(remain - 2 * equal_dist) + control_number
        return final_id_code
    if weight == 1:
        total_sum = 0
        for pos in range(0, 7):
            num = first_class_weights[pos] * int(start_id_code[pos])
            total_sum += num
        remain = (total_sum - int(control_number)) % 11
        print(remain)



if __name__ == '__main__':
    generate_id_code("3910606", "1", 1)
