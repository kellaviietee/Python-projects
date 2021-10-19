import pytest
import solution


def test_part1_int_correct_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_int_no_len():
    input_amount = 0
    res = solution.generate_list(input_amount, "string")
    expected_len = 0
    assert len(res) == expected_len


def test_part1_int_negative_len():
    input_amount = -1
    res = solution.generate_list(input_amount, "string")
    expected_len = 0
    assert len(res) == expected_len


def test_part1missing_string():
    input_amount = 5
    res = solution.generate_list(input_amount, "")
    expected_len = 0
    assert len(res) == expected_len
