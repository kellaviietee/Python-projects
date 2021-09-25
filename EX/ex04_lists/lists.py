def generate_list(amount: int, data_type: str) -> list:
    """Write a function that returns a list with amount elements of type data_type."""
    a = []
    if data_type == "int":
        for i in range(amount):
            b = 1 + i
            a.append(b)
    if data_type == "float":
        for i in range(amount):
            b = 1.5 + float(i)
            a.append(b)
    if data_type == "string":
        for i in range(amount):
            b = "hello" * i
            a.append(b)
    if data_type == "list":
        b = []
        for i in range(amount):
            a.append(b)
    if data_type == "tuple":
        b = ()
        for i in range(amount):
            a.append(b)
    if data_type == "dict":
        b = {}
        for i in range(amount):
            a.append(b)
    if data_type == "set":
        b = set()
        for i in range(amount):
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


# Part 3
print(generate_combined_list_unique([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
print(generate_combined_list_unique([(2, 'int'), (2, 'float'), (1, 'int')]))  # [43, 93, 4.3, 2.1]
