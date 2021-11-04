"""KT2."""


def switch_lasts_and_firsts(s: str) -> str:
    """
    Move last two characters to the beginning of string and first two characters to the end of string.

    When string length is smaller than 4, return reversed string.

    switch_lasts_and_firsts("ambulance") => "cebulanam"
    switch_lasts_and_firsts("firetruck") => "ckretrufi"
    switch_lasts_and_firsts("car") => "rac"

    :param s:
    :return: modified string
    """
    if len(s) < 4:
        new_word = list(s)
        new_word.reverse()
        new_reversed = ""
        for letter in new_word:
            new_reversed += letter
        return new_reversed
    else:
        word = list(s)
        last_letter = word.pop(-1)
        word.insert(0, last_letter)
        last_letter = word.pop(-1)
        word.insert(0, last_letter)
        first_letter = word.pop(2)
        word.append(first_letter)
        first_letter = word.pop(2)
        word.append(first_letter)
        new_word = ""
        for letter in word:
            new_word += letter
        return new_word


def take_partial(text: str, leave_count: int, take_count: int) -> str:
    """
    Take only part of the string.

    Ignore first leave_count symbols, then use next take_count symbols.
    Repeat the process until the end of the string.

    The following conditions are met (you don't have to check those):
    leave_count >= 0
    take_count >= 0
    leave_count + take_count > 0

    take_partial("abcdef", 2, 3) => "cde"
    take_partial("abcdef", 0, 1) => "abcdef"
    take_partial("abcdef", 1, 0) => ""
    """
    if take_count == 0:
        return ""
    if leave_count >= len(text):
        return ""
    else:
        right_word = ""
        for letter in range(len(text)):
            pos_checker = letter % (take_count + leave_count)
            if pos_checker in range(leave_count):
                continue
            if pos_checker in range(leave_count + take_count):
                right_word += text[letter]
        return right_word


def min_diff(nums):
    """
    Find the smallest diff between two integer numbers in the list.

    The list will have at least 2 elements.

    min_diff([1, 2, 3]) => 1
    min_diff([1, 9, 17]) => 8
    min_diff([100, 90]) => 10
    min_diff([1, 100, 1000, 1]) => 0

    :param nums: list of ints, at least 2 elements.
    :return: min diff between 2 numbers.
    """
    all_diffs = []
    for num1 in range(len(nums)):
        for num2 in range(len(nums)):
            if num1 != num2:
                all_diffs.append(abs(nums[num2] - nums[num1]))
    return min(all_diffs)


def get_symbols_by_occurrences(text: str) -> dict:
    """
    Return dict where key is the occurrence count and value is a list of corresponding symbols.

    The order of the counts and the symbols is not important.

    get_symbols_by_occurrences("hello") => {1: ['e', 'o', 'h'], 2: ['l']}
    get_symbols_by_occurrences("abcaba") => {2: ['b'], 1: ['c'], 3: ['a']}
    """
    symbols = {}
    for letters in text:
        how_many = text.count(letters)
        if letters not in symbols:
            symbols[letters] = how_many
    sorted_symbols_list = sorted(symbols.items(), key=lambda symbol_count: symbol_count[1])
    new_dict = {}
    for items in sorted_symbols_list:
        if items[1] in new_dict:
            new_dict[items[1]].append(items[0])
        if items[1] not in new_dict:
            new_dict[items[1]] = [items[0]]
    return new_dict


print(take_partial("abcdef", 2, 3))
