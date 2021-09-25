def generate_list(amount: int, data_type: str) -> list:
    """Write a function that returns a list with amount elements of type data_type."""
    a = []
    if data_type == "int":
        b = 1
        for i in range(amount):
            a.append(b)
    if data_type == "float":
        b = 1.5
        for i in range(amount):
            a.append(b)
    if data_type == "string":
        b = ""
        for i in range(amount):
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
    hmm = []
    for key in what_we_need:
        hmm.append(generate_list(what_we_need[key], key))
    return hmm


# Part 2
print(generate_combined_list([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
print(generate_combined_list([(3, 'int'), (5, 'int')]))  # [0, 0, 0, 0, 0]
print(generate_combined_list([(3, 'int'), (5, 'int'), (4, 'int')]))  # [100, 80, 60, 40, 20]
print(generate_combined_list([(2, 'list'), (3, 'string')]))  # ["a", [], "a", [], "a"]
print(generate_combined_list([(2, 'float'), (3, 'dict')]))  # [{}, {}, {}, 3.14, 3.15]
