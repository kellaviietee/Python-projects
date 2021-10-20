"""Pytest testing ground."""

import solution


def test_part1_int_correct_len():
    """
    Test if function works with all the correct inputs.

    :return:
    """
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_int_no_len():
    """
    Test if function can handle zero-length.

    :return:
    """
    input_amount = 0
    res = solution.generate_list(input_amount, "string")
    expected_len = 0
    assert len(res) == expected_len


def test_part1_int_negative_len():
    """
    Test if function can handle negative lengths.

    :return:
    """
    input_amount = -1
    res = solution.generate_list(input_amount, "string")
    expected_len = 0
    assert len(res) == expected_len


def test_part1missing_string():
    """
    Test if data_type is missing.

    :return:
    """
    input_amount = 5
    res = solution.generate_list(input_amount, "")
    expected_len = 0
    assert len(res) == expected_len


def test_part1_wrong_datatype():
    """
    Test if both inputs are wrong types.

    :return:
    """
    input_amount = 5.7
    res = solution.generate_list(input_amount, "wrong")
    expected_len = 0
    assert len(res) == expected_len


def test_part1_both_wrong():
    """
    Test if both inputs are not inserted.

    :return:
    """
    res = solution.generate_list(0, "")
    expected_len = 0
    assert len(res) == expected_len


