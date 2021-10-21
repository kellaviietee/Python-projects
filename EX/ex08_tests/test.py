"""Tests of week 8."""
import solution


def test_part1_int_correct_len():
    """Something."""
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_int_correct_len_type():
    """Something."""
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    for i in range(5):
        assert type(res[i]) == str


def test_part1_int_incorrect_string():
    """Something."""
    input_amount = -1
    res = solution.generate_list(input_amount, "string")
    expected_len = 0
    assert len(res) == expected_len


def test_part1_no_length():
    """Something."""
    input_amount = 0
    result = solution.generate_list(input_amount, "string")
    expected_len = 0
    assert len(result) == expected_len


def test_part1_int_incorrect_int():
    """Something."""
    input_amount = 3
    res = solution.generate_list(input_amount, "int")
    expected_len = 3
    assert len(res) == expected_len


def test_part1_int_incorrect_float():
    """Something."""
    input_amount = 3
    res = solution.generate_list(input_amount, "float")
    expected_len = 3
    assert len(res) == expected_len


def test_part1_int_incorrect_list():
    """Something."""
    input_amount = 3
    res = solution.generate_list(input_amount, "list")
    expected_len = 3
    assert len(res) == expected_len


def test_part1_int_incorrect_tuple():
    """Something."""
    input_amount = 3
    res = solution.generate_list(input_amount, "tuple")
    expected_len = 3
    assert len(res) == expected_len


def test_part1_int_incorrect_dict():
    """Something."""
    input_amount = 3
    res = solution.generate_list(input_amount, "dict")
    expected_len = 3
    assert len(res) == expected_len


def test_part1_int_incorrect_set():
    """Something."""
    input_amount = 3
    res = solution.generate_list(input_amount, "set")
    expected_len = 3
    assert len(res) == expected_len


def test_part1_big_numbers():
    """Something."""
    input_amount = 30000
    res = solution.generate_list(input_amount, "list")
    expected_len = 30000
    assert len(res) == expected_len


def test_generate_combined_list_correct_string():
    """Something."""
    input_to_list = [(3, "string"), (5, "string")]
    result = solution.generate_combined_list(input_to_list)
    expected_result = 5
    assert len(result) == expected_result


def test_generate_combined_list_empty_input():
    """Something."""
    input_to_list = []
    result = solution.generate_combined_list(input_to_list)
    expected_result = 0
    assert len(result) == expected_result


def test_generate_combined_list_correct_int():
    """Something."""
    input_to_list = [(5, "int"), (3, "int")]
    result = solution.generate_combined_list(input_to_list)
    expected_result = 5
    assert len(result) == expected_result


def test_generate_combined_list_correct_float():
    """Something."""
    input_to_list = [(5, "float"), (3, "float")]
    result = solution.generate_combined_list(input_to_list)
    expected_result = 5
    assert len(result) == expected_result


def test_generate_combined_list_big_numbers():
    """Something."""
    input_to_list = [(7000, "int")]
    result = solution.generate_combined_list(input_to_list)
    expected_result = 7000
    assert len(result) == expected_result


def test_generate_combined_list_unique():
    """Something."""
    input_to_list = [(5, "string")]
    result = solution.generate_combined_list_unique(input_to_list)
    expected_result = 5
    assert len(result) == expected_result


def test_generate_combined_list_correct_types():
    """Something."""
    input_to_list = [(2, "float"), (3, "string")]
    result = solution.generate_combined_list(input_to_list)
    for i in range(0, 2):
        assert type(result[i]) == float
    for k in range(2, 5):
        assert type(result[k]) == str


def test_generate_combined_list_unique_empty():
    """Something."""
    input_to_list = [(0, "string"), (0, "int")]
    result = solution.generate_combined_list_unique(input_to_list)
    expected_result = 0
    assert len(result) == expected_result


def test_generate_combined_list_unique_correct_types():
    """Something."""
    input_to_list = [(7, "int")]
    result = solution.generate_combined_list_unique(input_to_list)
    for i in range(7):
        assert type(result[i]) == int


def test_generate_combined_list_unique_correct_types_diff():
    """Something."""
    input_to_list = [(7, "int"), (5, "string")]
    result = solution.generate_combined_list_unique(input_to_list)
    for i in range(7):
        assert type(result[i]) == int
    for k in range(7, 12):
        assert type(result[k]) == str


def test_generate_combined_list_unique_big_numbers():
    """Something."""
    input_to_list = [(7000, "int"), (5000, "string")]
    result = solution.generate_combined_list_unique(input_to_list)
    expected_len = 12000
    assert len(result) == expected_len


def test_generate_combined_list_unique_all_items_unique():
    """Something."""
    input_to_list = [(70, "int"), (50, "string")]
    result = solution.generate_combined_list_unique(input_to_list)
    set_of_result = set(result)
    assert len(result) == len(set_of_result)


def test_generate_combined_list_unique_float():
    """Something."""
    input_to_list = [(7, "float")]
    result = solution.generate_combined_list_unique(input_to_list)
    set_of_unique = set(result)
    assert len(result) == len(set_of_unique)
