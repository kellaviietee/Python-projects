"""Operators."""


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    return x * y


def div(x, y):
    return x / y


def modulus(x, y):
    return x % y


def floor_div(x, y):
    return x // y


def exponent(x, y):
    return x ** y


def first_greater_or_equal(x, y):
    return x >= y


def second_less_or_equal(x, y):
    return y <= x


def x_is_y(x, y):
    return x == y


def x_is_not_y(x, y):
    return x != y


def if_else(a, b, c, d):
    mult = a * b
    divise = c / d
    if mult > divise:
        return mult
    elif divise > mult:
        return divise
    else:
        return 0


def surface(a, b):
    return a * b


def volume(a, b, c):
    return a * b * c


if __name__ == '__main__':
    print(add(1, -2))  # -1
    print(sub(5, 5))  # 0
    print(multiply(5, 5))  # 25
    print(div(15, 5))  # 3
    print(modulus(9, 3))  # 0
    print(floor_div(3, 2))  # 1
    print(exponent(5, 5))  # 3125
    print(first_greater_or_equal(1, 2))  # False
    print(second_less_or_equal(5, 5))  # True
    print(x_is_y(1, 2))  # False
    print(x_is_not_y(1, 2))  # True
    print(if_else(1, 3, 5, 99))  # 3
    print(if_else(2, 1, 10, 5))  # 0
    print(surface(1, 2))  # 2
    print(volume(5, 5, 5))  # 125
