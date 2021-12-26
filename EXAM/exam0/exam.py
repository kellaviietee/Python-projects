"""Test Exam."""


def find_capital_letters(text: str) -> str:
    capital_letters = ""
    for letter in text:
        if letter.isupper():
            capital_letters += letter
    return capital_letters


def close_far(a: int, b: int, c: int) -> bool:
    if abs(abs(a) - abs(b)) <= 1 and abs(abs(a) - abs(c)) >= 2:
        return True
    elif abs(abs(a) - abs(c)) <= 1 and abs(abs(a) - abs(b)) >= 2:
        return True
    elif abs(abs(b) - abs(c)) <= 1 and abs(abs(a) - abs(c)) >= 2:
        return True
    else:
        return False


if __name__ == "__main__":
    print(find_capital_letters("asdfsddddfvKJSHJDJKSKDkSKJDJKKJDSJFJKSJJdjsjdjsjejsjdjSjkDJsndJDKJjksd"))
    print(close_far(1, 2,3))
