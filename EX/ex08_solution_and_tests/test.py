import solution


def test_evening_no_coffee():
    """
    Student has no coffee at evening time.

    :return:
    """
    coffee_needs = False
    clock = 20
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_evening_yes_coffee():
    """
    Student has coffee at evening time.

    :return:
    """
    coffee_needs = True
    clock = 20
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_morning_yes_coffee():
    """
    Student has coffee at morning time.

    :return:
    """
    coffee_needs = True
    clock = 12
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_morning_no_coffee():
    """
    Student has no coffee at morning time.

    :return:
    """
    coffee_needs = False
    clock = 12
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_night_no_coffee():
    """
    Student has no coffee at night.

    :return:
    """
    coffee_needs = False
    clock = 3
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_night_yes_coffee():
    """
    Student has a coffee at night.

    :return:
    """
    coffee_needs = True
    clock = 3
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_evening_edge_yes_coffee():
    """
    Testing one evening edge case.

    :return:
    """
    coffee_needs = True
    clock = 24
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_evening_other_edge_yes_coffee():
    """
    Testing another evening edge case.

    :return:
    """
    coffee_needs = True
    clock = 18
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_evening_edge_no_coffee():
    """
    Evening edge with no coffee.

    :return:
    """
    coffee_needs = False
    clock = 24
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_evening_other_edge_no_coffee():
    """
    Other evening edge with no coffee.

    :return:
    """
    coffee_needs = False
    clock = 18
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_day_edge_no_coffee():
    """
    Daytime edge with no coffee.

    :return:
    """
    coffee_needs = False
    clock = 5
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_day_other_edge_no_coffee():
    """
    Other day edge with no coffee.

    :return:
    """
    coffee_needs = False
    clock = 17
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_day_edge_yes_coffee():
    """
    Day edge with coffee.

    :return:
    """
    coffee_needs = True
    clock = 5
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_day_other_edge_yes_coffee():
    """
    Other day edge with coffee.

    :return:
    """
    coffee_needs = True
    clock = 17
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_night_edge_no_coffee():
    """
    Night edge with no coffee.

    :return:
    """
    coffee_needs = False
    clock = 1
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_night_other_edge_no_coffee():
    """
    Other night edge with no coffee.

    :return:
    """
    coffee_needs = False
    clock = 4
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_night_edge_yes_coffee():
    """
    Nighttime edge with coffee.

    :return:
    """
    coffee_needs = True
    clock = 1
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_night_other_edge_yes_coffee():
    """
    Other nighttime edge with coffee.

    :return:
    """
    coffee_needs = True
    clock = 4
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_lottery_jackpot():
    """
    Test to check if lottery pays out.

    :return:
    """
    a = 5
    b = 5
    c = 5
    result = solution.lottery(a, b, c)
    expected_result = 10
    assert result == expected_result


def test_lottery_all_positive_win():
    """
    Testing lottery all positive numbers.

    :return:
    """
    a = 1
    b = 1
    c = 1
    result = solution.lottery(a, b, c)
    expected_result = 5
    assert result == expected_result


def test_all_negative_win():
    """
    Testing if cheating is ok.

    :return:
    """
    a = -1
    b = -1
    c = -1
    result = solution.lottery(a, b, c)
    expected_result = 5
    assert result == expected_result


def test_all_zeros_win():
    """
    Why not start with zeros for the programmers.

    :return:
    """
    a = 0
    b = 0
    c = 0
    result = solution.lottery(a, b, c)
    expected_result = 5
    assert result == expected_result


def test_lottery_a_b_same_c_not():
    """
    Checking if first two are the same.

    :return:
    """
    a = 5
    b = 5
    c = 7
    result = solution.lottery(a, b, c)
    expected_result = 0
    assert result == expected_result


def test_lottery_a_c_same_b_not():
    """
    Second check of same lottery balls.

    :return:
    """
    a = 6
    b = 5
    c = 6
    result = solution.lottery(a, b, c)
    expected_result = 0
    assert result == expected_result


def test_lottery_b_c_same_a_not():
    """
    If second and third are the same values.

    :return:
    """
    a = 6
    b = 8
    c = 8
    result = solution.lottery(a, b, c)
    expected_result = 1
    assert result == expected_result


def test_lottery_all_dif():
    """
    You do know that your own tests does not  even take this into account or something.

    :return:
    """
    a = 6
    b = 7
    c = 8
    result = solution.lottery(a, b, c)
    expected_result = 1
    assert result == expected_result


def test_fruit_zeros():
    """
    Costumer doesn't want anything.

    :return:
    """
    small_basket = 0
    big_basket = 0
    order_amount = 0
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = small_basket
    assert result == expected_result


def test_fruit_zero_amnt_zero_small():
    """
    Costumer actually just wants big baskets.

    :return:
    """
    small_basket = 0
    big_basket = 5
    order_amount = 0
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = small_basket
    assert result == expected_result


def test_fruit_zero_amnt_zero_big():
    """
    Now he/she wants small baskets.

    What's up with that?

    :return:
    """
    small_basket = 6
    big_basket = 0
    order_amount = 0
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = order_amount
    assert result == expected_result


def test_fruit_zero_amnt():
    """
    He/She came around for third round and decided he will take both small and big baskets.

    :return:
    """
    small_basket = 6
    big_basket = 3
    order_amount = 0
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = order_amount
    assert result == expected_result


def test_fruit_only_big_exact():
    """
    Exactly into the baskets.

    :return:
    """
    small_basket = 0
    big_basket = 3
    order_amount = 15
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = small_basket
    assert result == expected_result


def test_fruit_only_big_not_enough_but_mlt_5():
    """
    Not even the big baskets will help you now.

    :return:
    """
    small_basket = 0
    big_basket = 3
    order_amount = 20
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = -1
    assert result == expected_result


def test_fruit_only_big_more_than_needed_match():
    """
    What will I do with the rest of the baskets.

    :return:
    """
    small_basket = 0
    big_basket = 5
    order_amount = 20
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = small_basket
    assert result == expected_result


def test_fruit_only_big_more_than_needed_no_match():
    """
    He/She needs to order some more. No takebacksies.

    :return:
    """
    small_basket = 0
    big_basket = 5
    order_amount = 23
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = -1
    assert result == expected_result


def test_fruit_only_small_match_more_than_5():
    """
    Small basket galore.

    :return:
    """
    small_basket = 6
    big_basket = 0
    order_amount = 6
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = small_basket
    assert result == expected_result


def test_fruit_only_small_not_enough_more_than_5():
    """
    It an be a galore but still not enough.

    :return:
    """
    small_basket = 6
    big_basket = 0
    order_amount = 9
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = -1
    assert result == expected_result


def test_fruit_only_small_more_than_needed():
    """
    I guess I can keep the extra baskets for myself.

    :return:
    """
    small_basket = 14
    big_basket = 0
    order_amount = 13
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = order_amount
    assert result == expected_result


def test_fruit_match_small_more_than_five():
    """
    Hey the smallest things in life add up in the  end.

    :return:
    """
    small_basket = 6
    big_basket = 1
    order_amount = 11
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = small_basket
    assert result == expected_result


def test_fruit_all_small_some_big():
    """
    You gotta take the small one.

    :return:
    """
    small_basket = 1
    big_basket = 4
    order_amount = 11
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = 1
    assert result == expected_result


def test_fruit_some_small_some_big():
    """
    Some of this, some of that.

    :return:
    """
    small_basket = 6
    big_basket = 4
    order_amount = 11
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = 1
    assert result == expected_result


def test_fruit_some_small_all_big():
    """
    You gotta take the big ones.

    :return:
    """
    small_basket = 6
    big_basket = 4
    order_amount = 24
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = 4
    assert result == expected_result


def test_fruit_not_enough():
    """
    There is just no room for the rest of them.

    :return:
    """
    small_basket = 6
    big_basket = 4
    order_amount = 34
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = -1
    assert result == expected_result


def test_fruit_enough_bigs_not_enough_smalls():
    """
    I could put them all in the big ones but that would be wasteful.

    :return:
    """
    small_basket = 3
    big_basket = 7
    order_amount = 34
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = -1
    assert result == expected_result


def test_fruit_enough_bigs_not_enough_smalls_large_numbers():
    """
    Are you a character from math problems.

    :return:
    """
    small_basket = 3
    big_basket = 1280000004
    order_amount = 640000004
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = -1
    assert result == expected_result


def test_fruit_large_numbers_exact():
    """
    Oh you definetly are a math problem character buying so many fruits.

    :return:
    """
    small_basket = 30000000000
    big_basket = 1280000004
    order_amount = 36400000020
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = small_basket
    assert result == expected_result
