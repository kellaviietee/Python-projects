"""Test Exam."""


def find_capital_letters(text: str) -> str:
    capital_letters = ""
    for letter in text:
        if letter.isupper():
            capital_letters += letter
    return capital_letters


if __name__ == "__main__":
    print(find_capital_letters("asdfsddddfvKJSHJDJKSKDkSKJDJKKJDSJFJKSJJdjsjdjsjejsjdjSjkDJsndJDKJjksd"))