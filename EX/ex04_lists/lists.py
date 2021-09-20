def generate_list(amount: int, data_type: str) -> list:
    """Write a function that returns a list with amount elements of type data_type."""
    a = []
    b = type(data_type)
    print(b)
    for i in range(amount):
        a.append(b)
    return a


print(generate_list(5, 5))
