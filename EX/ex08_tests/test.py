import solution


def test_part1_int_correct_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_int_incorrect_string():
    input_amount = -1
    res = solution.generate_list(input_amount, "string")
    expected_len = 0
    assert len(res) == expected_len

def test_part1_no_length():
    input_amount = 0
    result = solution.generate_list(input_amount, "string")
    expected_len = 0
    assert len(result) == expected_len

def test_part1_int_incorrect_int():
    input_amount = 3
    res = solution.generate_list(input_amount, "int")
    expected_len = 3
    assert len(res) == expected_len

def test_part1_int_incorrect_float():
    input_amount = 3
    res = solution.generate_list(input_amount, "float")
    expected_len = 3
    assert len(res) == expected_len

def test_part1_int_incorrect_list():
    input_amount = 3
    res = solution.generate_list(input_amount, "list")
    expected_len = 3
    assert len(res) == expected_len