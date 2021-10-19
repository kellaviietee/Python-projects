"""Week 8 exercises."""


def generate_list(input_amount, data_type):
    """
    New stuff to test.

    :param input_amount:
    :param data_type:
    :return:
    """
    a = []
    if data_type == "int":
        for i in range(input_amount):
            b = 1 + i
            a.append(b)
    if data_type == "float":
        for i in range(input_amount):
            b = 1.5 + float(i)
            a.append(b)
    if data_type == "string":
        for i in range(input_amount):
            b = "hello" * i
            a.append(b)
    if data_type == "list":
        for i in range(input_amount):
            b = [i]
            a.append(b)
    if data_type == "tuple":
        for i in range(input_amount):
            b = (i,)
            a.append(b)
    if data_type == "dict":
        for i in range(input_amount):
            b = {i: i}
            a.append(b)
    if data_type == "set":
        for i in range(input_amount):
            b = set()
            b.add(i)
            a.append(b)
    return a


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
