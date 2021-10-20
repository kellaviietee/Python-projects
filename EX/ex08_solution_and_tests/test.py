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
