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
    expected_result = False
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
