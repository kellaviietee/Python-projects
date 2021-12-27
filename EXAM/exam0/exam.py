"""Test Exam."""


def find_capital_letters(text: str) -> str:
    capital_letters = ""
    for letter in text:
        if letter.isupper():
            capital_letters += letter
    return capital_letters


def close_far(a: int, b: int, c: int) -> bool:
    numbers = [a, b, c]
    sorted_numbers = sorted(numbers, reverse=True)
    if sorted_numbers[0] - sorted_numbers[1] <= 1:
        if sorted_numbers[1] - sorted_numbers[2] >= 2:
            return True
        else:
            return False
    else:
        if sorted_numbers[1] - sorted_numbers[2] <= 1 and sorted_numbers[0] - sorted_numbers[1] >= 2:
            return True
        else:
            return False


if __name__ == "__main__":
    print(find_capital_letters("asdfsddddfvKJSHJDJKSKDkSKJDJKKJDSJFJKSJJdjsjdjsjejsjdjSjkDJsndJDKJjksd"))
    print(close_far(1, 0, 0))
