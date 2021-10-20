import solution


def test_evening_no_coffee():
    coffee_needs = False
    clock = 20
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result



def test_evening_yes_coffee():
    coffee_needs = True
    clock = 20
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_morning_yes_coffee():
    coffee_needs = True
    clock = 12
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result

"""
def test_morning_no_coffee():
    coffee_needs = False
    clock = 12
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_overtime_no_coffee():
    coffee_needs = False
    clock = 36
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_overtime_yes_coffee():
    coffee_needs = True
    clock = 36
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_undertime_no_coffee():
    coffee_needs = False
    clock = -1
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_undertime_yes_coffee():
    coffee_needs = True
    clock = -1
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_lottery_jackpot():
    a = 5
    b = 5
    c = 5
    result = solution.lottery(a, b, c)
    expected_result = 10
    assert result == expected_result


def test_lottery_small_win():
    a = 1
    b = 1
    c = 1
    result = solution.lottery(a, b, c)
    expected_result = 5
    assert result == expected_result


def test_lottery_constallation_win():
    a = 5
    b = 6
    c = 7
    result = solution.lottery(a, b, c)
    expected_result = 1
    assert result == expected_result


def test_lottery_no_win():
    a = 5
    b = 6
    c = 6
    result = solution.lottery(a, b, c)
    expected_result = 0
    assert result == expected_result


def test_fruit_correct():
    small_basket = 4
    big_basket = 2
    order_amount = 14
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = small_basket
    assert result == expected_result


def test_fruit_too_big_order():
    small_basket = 2
    big_basket = 2
    order_amount = 20
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = -1
    assert result == expected_result


def test_fruit_no_big_basket():
    small_basket = 2
    big_basket = 0
    order_amount = 2
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = small_basket
    assert result == expected_result


def test_fruit_not_enough_small():
    small_basket = 1
    big_basket = 1
    order_amount = 4
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = -1
    assert result == expected_result
"""
