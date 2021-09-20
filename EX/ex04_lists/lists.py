def generate_list(amount: int, data_type: str) -> list:
    """Write a function that returns a list with amount elements of type data_type."""
    a = []
    if amount == 0:
        return  a
    if data_type == "int":
        b = int
        for i in range(amount):
            a.append(b)
    if data_type == "float":
        b = float
        for i in range(amount):
            a.append(b)
    if data_type == "str":
        b = str
        for i in range(amount):
            a.append(b)
    if data_type == "list":
        b = list
        for i in range(amount):
            a.append(b)
    if data_type == "tuple":
        b = tuple
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


print(generate_list(5, "dict"))
