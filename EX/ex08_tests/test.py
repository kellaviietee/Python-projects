import solution


def test_part1_int_correct_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_int_incorrect_ints():
    input_amount = -1
    res = solution.generate_list(input_amount, "string")
    expected_len = 0
    assert len(res) == expected_len

def test_part1_int_incorrect_both():
    input_amount = -1
    res = solution.generate_list(input_amount, "list")
    expected_len = 0
    assert len(res) == expected_len