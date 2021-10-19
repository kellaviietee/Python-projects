def generate_list(input_amount, data_type):
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