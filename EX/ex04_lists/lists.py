"""Exercises of week four."""


def generate_list(amount: int, data_type: str) -> list:
    """Write a function that returns a list with amount elements of type data_type."""
    a = []
    if data_type == "int":
        a = generate_enough_ints(amount)
    if data_type == "float":
        a = generate_enough_floats(amount)
    if data_type == "string":
        a = generate_enough_strings(amount)
    if data_type == "list":
        a = generate_enough_lists_in_list(amount)
    if data_type == "tuple":
        a = generate_enough_tuples_in_list(amount)
    if data_type == "dict":
        a = generate_enough_dicts_in_list(amount)
    if data_type == "set":
        a = generate_enough_sets_in_list(amount)
    return a


def generate_enough_ints(amount: int):
    """
    Generate a list of integers.

    :param amount: how many integers in a list.
    :return:
    """
    int_list = []
    for i in range(amount):
        b = 1 + i
        int_list.append(b)
    return int_list


def generate_enough_floats(amount: int):
    """
    Generate a list of floats.

    :param amount: how many floats in a list.
    :return:
    """
    int_list = []
    for i in range(amount):
        b = 1.5 + i
        int_list.append(b)
    return int_list


def generate_enough_strings(amount: int):
    """
    Generate a list of strings.

    :param amount: how many lists in a list.
    :return:
    """
    int_list = []
    for i in range(amount):
        b = "hello" * i
        int_list.append(b)
    return int_list


def generate_enough_lists_in_list(amount: int):
    """
    Generate a list of lists.

    :param amount: how many lists in a list.
    :return:
    """
    int_list = []
    for i in range(amount):
        b = [i]
        int_list.append(b)
    return int_list


def generate_enough_tuples_in_list(amount: int):
    """
    Generate a list of tuples.

    :param amount: how many tuples in a list.
    :return:
    """
    int_list = []
    for i in range(amount):
        b = (i,)
        int_list.append(b)
    return int_list


def generate_enough_dicts_in_list(amount: int):
    """
    Generate a list of dictionaries.

    :param amount: how many dictionaries in a list.
    :return:
    """
    int_list = []
    for i in range(amount):
        b = {i: i}
        int_list.append(b)
    return int_list


def generate_enough_sets_in_list(amount: int):
    """
    Generate a list of sets.

    :param amount: how many sets in a list.
    :return:
    """
    int_list = []
    for i in range(amount):
        b = set()
        b.add(i)
        int_list.append(b)
    return int_list


def generate_combined_list(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains at least 'amount' of elements of type 'data_type'.
    """
    what_we_need = {}
    for item in inputs:
        if item[1] in what_we_need.keys():
            if item[0] > what_we_need[item[1]]:
                what_we_need[item[1]] = item[0]
            else:
                continue
        else:
            what_we_need[item[1]] = item[0]
    combined_list = []
    for key in what_we_need:
        combined_list += (generate_list(what_we_need[key], key))
    return combined_list


def generate_combined_list_unique(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains at least 'amount' of elements of type 'data_type'.
    Data types used in this function are 'int', 'float' and 'str' (string).
    The returned list can contain only unique elements.
    """
    what_we_need = {}
    for item in inputs:
        if item[1] in what_we_need.keys():
            if item[0] > what_we_need[item[1]]:
                what_we_need[item[1]] = item[0]
            else:
                continue
        else:
            what_we_need[item[1]] = item[0]
    combined_list = []
    for key in what_we_need:
        combined_list += (generate_list(what_we_need[key], key))
    return combined_list


def generate_combined_list_unique_advanced(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains at least 'amount' of elements of type 'data_type'.
    All the data types from the first function are used here.
    The returned list can contain only unique elements.
    """
    what_we_need = {}
    for item in inputs:
        if item[1] in what_we_need.keys():
            if item[0] > what_we_need[item[1]]:
                what_we_need[item[1]] = item[0]
            else:
                continue
        else:
            what_we_need[item[1]] = item[0]
    combined_list = []
    for key in what_we_need:
        combined_list += (generate_list(what_we_need[key], key))
    return combined_list


# Part 4
print(generate_list(5, "set"))
