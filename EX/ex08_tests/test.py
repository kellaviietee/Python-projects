def test_part1_both_wrong():
    """
    Test if both inputs are not inserted.

    :return:
    """
    res = solution.generate_list(None, None)
    expected_len = None
    assert len(res) == expected_len
