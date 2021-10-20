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


def test_morning_no_coffee():
    coffee_needs = False
    clock = 12
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_night_no_coffee():
    coffee_needs = False
    clock = 3
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_night_yes_coffee():
    coffee_needs = True
    clock = 3
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_evening_edge_yes_coffee():
    coffee_needs = True
    clock = 24
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_evening_other_edge_yes_coffee():
    coffee_needs = True
    clock = 18
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_evening_edge_no_coffee():
    coffee_needs = False
    clock = 24
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_evening_other_edge_no_coffee():
    coffee_needs = False
    clock = 18
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_day_edge_no_coffee():
    coffee_needs = False
    clock = 5
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_day_other_edge_no_coffee():
    coffee_needs = False
    clock = 17
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_day_edge_yes_coffee():
    coffee_needs = True
    clock = 5
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_day_other_edge_yes_coffee():
    coffee_needs = True
    clock = 17
    result = solution.students_study(clock, coffee_needs)
    expected_result = True
    assert result == expected_result


def test_night_edge_no_coffee():
    coffee_needs = False
    clock = 1
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_night_other_edge_no_coffee():
    coffee_needs = False
    clock = 4
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_night_edge_yes_coffee():
    coffee_needs = True
    clock = 1
    result = solution.students_study(clock, coffee_needs)
    expected_result = False
    assert result == expected_result


def test_night_other_edge_yes_coffee():
    coffee_needs = True
    clock = 4
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


def test_lottery_all_positive_win():
    a = 1
    b = 1
    c = 1
    result = solution.lottery(a, b, c)
    expected_result = 5
    assert result == expected_result


def test_all_negative_win():
    a = -1
    b = -1
    c = -1
    result = solution.lottery(a, b, c)
    expected_result = 5
    assert result == expected_result


def test_all_zeros_win():
    a = 0
    b = 0
    c = 0
    result = solution.lottery(a, b, c)
    expected_result = 5
    assert result == expected_result


def test_lottery_a_b_same_c_not():
    a = 5
    b = 5
    c = 7
    result = solution.lottery(a, b, c)
    expected_result = 0
    assert result == expected_result


def test_lottery_a_c_same_b_not():
    a = 6
    b = 5
    c = 6
    result = solution.lottery(a, b, c)
    expected_result = 0
    assert result == expected_result


def test_lottery_b_c_same_a_not():
    a = 6
    b = 8
    c = 8
    result = solution.lottery(a, b, c)
    expected_result = 1
    assert result == expected_result


def test_lottery_all_dif():
    a = 6
    b = 7
    c = 8
    result = solution.lottery(a, b, c)
    expected_result = 1
    assert result == expected_result



def test_fruit_zeros():
    small_basket = 0
    big_basket = 0
    order_amount = 0
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = small_basket
    assert result == expected_result

def test_fruit_zero_amnt_zero_small():
    small_basket = 0
    big_basket = 5
    order_amount = 0
    result = solution.fruit_order(small_basket, big_basket, order_amount)
    expected_result = small_basket
    assert result == expected_result
"""
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
