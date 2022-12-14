"""Exam0."""
from typing import Optional
import re


def find_capital_letters(s: str) -> str:
    """
    Return only capital letters from the string.

    #1

    If there are no capital letters, return empty string.
    The string contains only latin letters (a-z and A-Z).
    The letters should be in the same order as they appear in the input string.

    find_capital_letters("ABC") => "ABC"
    find_capital_letters("abc") => ""
    find_capital_letters("aAbBc") => "AB"
    """
    new_s = ""
    for letter in s:
        if letter.isupper():
            new_s += letter
    return new_s


def close_far(a: int, b: int, c: int) -> bool:
    """
    Return if one value is "close" and other is "far".

    #2

    Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """
    if abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2:
        return True
    elif abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2:
        return True
    else:
        return False


def get_names_from_results(results_string: str, min_result: int) -> list:
    """
    Given a string of names and scores, return a list of names where the score is higher than or equal to min_result.

    #3

    Results are separated by comma (,). Result contains a score and optionally a name.
    Score is integer, name can have several names separated by single space.
    Name part can also contain numbers and other symbols (except for comma).
    Return only the names which have the score higher or equal than min_result.
    The order of the result should be the same as in input string.

    get_names_from_results("ago 123,peeter 11", 0) => ["ago", "peeter"]
    get_names_from_results("ago 123,peeter 11,33", 10) => ["ago", "peeter"]  # 33 does not have the name
    get_names_from_results("ago 123,peeter 11", 100) => ["ago"]
    get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11) => ["ago", "peeter",  "kitty11!!"]
    get_names_from_results("ago 123,peeter 11,kusti riin 14", 12) => ["ago", "kusti riin"]
    """
    above_min = []
    separated_results = results_string.split(",")
    for ind_result in separated_results:
        pattern = r"(.+)[\D](\d+)$"
        results = re.findall(pattern, ind_result)
        if len(results) == 0:
            continue
        if len(results[0]) > 1:
            if int(results[0][1]) >= min_result:
                above_min.append(results[0][0])
        else:
            continue
    return above_min


def tic_tac_toe(game: list) -> int:
    """
    Find game winner.

    #4

    The 3x3 table is represented as a list of 3 rows, each row has 3 element (ints).
    The value can be 1 (player 1), 2 (player 2) or 0 (empty).
    The winner is the player who gets 3 of her pieces in a row, column or diagonal.

    There is only one winner or draw. You don't have to validate whether the game is in correct (possible) state.
    I.e the game could have four 1s and one 0 etc.

    tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]]) => 1
    tic_tac_toe([[1, 0, 1], [2, 1, 2], [2, 2, 0]]) => 0
    tic_tac_toe([[2, 2, 2], [0, 2, 0], [0, 1, 0]]) => 2

    :param game
    :return: winning player id
    """
    for row in game:
        if row.count(1) == 3:
            return 1
        elif row.count(2) == 3:
            return 2
    columns = [[game[0][0], game[1][0], game[2][0]], [game[0][1], game[1][1], game[2][1]],
               [game[0][2], game[1][2], game[2][2]]]
    for column in columns:
        if column.count(1) == 3:
            return 1
        elif column.count(2) == 3:
            return 2
    diagonals = [[game[0][0], game[1][1], game[2][2]], [game[0][2], game[1][1], game[2][0]]]
    for diagonal in diagonals:
        if diagonal.count(1) == 3:
            return 1
        elif diagonal.count(2) == 3:
            return 2
    return 0


def rainbows(field: str, lower=False) -> int:
    """
    The function to count rainbows.

    #5

    Function has to be recursive.

    assert rainbows("rainbowThisIsJustSomeNoise") == 1  # Lisaks vikerkaarele on veel s??mboleid
    assert rainbows("WoBniar") == 1  # Vikerkaar on tagurpidi ja sisaldab suuri t??hti
    assert rainbows("rainbowobniar") == 1  # Kaks vikerkaart jagavad t??hte seega ??ks neist ei ole valiidne

    :param field: string to search rainbows from
    :return: number of rainbows in the string
    """
    print(field)
    word_to_change = field.lower()
    if "rainbow" in word_to_change:
        rainbow_start_location = word_to_change.find("rainbow")
        end_pos = rainbow_start_location + len("rainbow")
        string_start = field[:rainbow_start_location]
        string_end = field[end_pos:]
        remaining_string = "".join([string_start, string_end])
        return 1 + rainbows(remaining_string)

    elif "wobniar" in word_to_change:
        rainbow_start_location = word_to_change.find("wobniar")
        end_pos = rainbow_start_location + len("wobniar")
        string_start = field[:rainbow_start_location]
        string_end = field[end_pos:]
        remaining_string = "".join([string_start, string_end])
        return 1 + rainbows(remaining_string)
    return 0


def longest_substring(text: str) -> str:
    """
    Find the longest substring.

    #6

    Substring may not contain any character twice.
    CAPS and lower case chars are the same (a == A)
    In output, the case (whether lower- or uppercase) should remain.
    If multiple substrings have same length, choose first one.

    aaa -> a
    abc -> abc
    abccba -> abc
    babcdEFghij -> abcdEFghij
    abBcd => Bcd
    '' -> ''
    """
    lowered_word = text.lower()
    long_word = ""
    for start_pos in range(len(lowered_word) + 1):
        for end_pos in range(start_pos + 1, len(lowered_word) + 1):
            current_word = lowered_word[start_pos:end_pos]
            current_set = set(current_word)
            if len(current_word) == len(current_set):
                if len(current_word) > len(long_word):
                    long_word = text[start_pos:end_pos]
            elif len(current_word) != len(current_set):
                break
    return long_word


class Student:
    """Student class."""

    def __init__(self, name: str, average_grade: float, credit_points: int):
        """Constructor."""
        self.credit_points = credit_points
        self.average_grade = average_grade
        self.name = name


def create_student(name: str, grades: list, credit_points: int) -> Student:
    """
    Create a new student where average grade is the average of the grades in the list.

    Round the average grade up to three decimal places.
    If the list of grades is empty, the average grade will be 0.
    """
    gpa = 0
    if len(grades) == 0:
        return Student(name, gpa, credit_points)
    else:
        average_grade = round(sum(grades) / len(grades), 3)
        print(average_grade)
        return Student(name, average_grade, credit_points)


def get_top_student_with_credit_points(students: list[Student], min_credit_points: int):
    """
    Return the student with the highest average grade who has enough credit points.

    If there are no students with enough credit points, return None.
    If several students have the same average score, return the first.
    """
    students_with_enough_credit = []
    for student in students:
        if student.credit_points >= min_credit_points:
            students_with_enough_credit.append(student)
    if len(students_with_enough_credit) == 0:
        return None
    else:
        return max(students_with_enough_credit, key=lambda x: x.average_grade)


def add_result_to_student(student: Student, grades_count: int, new_grade: int, credit_points) -> Student:
    """
    Update student average grade and credit points by adding a new grade (result).

    As the student object does not have grades count information, it is provided in this function.
    average grade = sum of grades / count of grades

    With the formula above, we can deduct:
    sum of grades = average grade * count of grades

    The student has the average grade, function parameters give the count of grades.
    If the sum of grades is known, a new grade can be added and a new average can be calculated.
    The new average grade must be rounded to three decimal places.
    Given credits points should be added to old credit points.

    Example1:
        current average (from student object) = 4
        grades_count (from parameter) = 2
        so, the sum is 2 * 4 = 8
        new grade (from parameter) = 5
        new average = (8 + 5) / 3 = 4.333
        The student object has to be updated with the new average

    Example2:
        current average = 0
        grades_count = 0
        calculated sum = 0 * 0 = 0
        new grade = 4
        new average = 4 / 1 = 4

    Return the modified student object.
    """
    current_gpa = student.average_grade
    new_gpa = round((current_gpa * grades_count + new_grade) / (grades_count + 1), 3)
    new_credit = student.credit_points + credit_points
    student.average_grade = new_gpa
    student.credit_points = new_credit
    return student


def get_ordered_students(students: list) -> list:
    """
    Return a new sorted list of students by (down).

    credit points (higher first), average_grade (higher first), name (a to z).
    """
    ordered_students = sorted(students, key=lambda x: (-x.credit_points, -x.average_grade, x.name))
    return ordered_students


class Room:
    """Room."""

    def __init__(self, number: int, price: int, features: list = [], booked: bool = False):
        """Constructor."""
        self.booked = booked
        self.features = features
        self.price = price
        self.number = number

    def __repr__(self):
        """Represent the Room."""
        return f"Room nr: {self.number}, {self.price} EUR"

    def add_feature(self, feature: str) -> bool:
        """
        Add a feature to the room.

        Do not add the feature and return False if:
        - the room already has that feature
        - the room is booked.
        Otherwise, add the feature to the room and return True
        """
        if self.booked:
            return False
        if not self.features:
            self.features = [feature]
            return True
        else:
            if feature in self.features:
                return False
            elif feature not in self.features:
                self.features.append(feature)
                return True

    def get_features(self) -> list:
        """Return all the features of the room."""
        return self.features

    def get_price(self) -> int:
        """Return the price."""
        return self.price

    def get_number(self) -> int:
        """Return the room number."""
        return self.number

    def get_booked(self) -> bool:
        """Return if the room is booked."""
        return self.booked


class Hotel:
    """Hotel."""

    def __init__(self, rooms: list[Room] = []):
        """Constructor."""
        self.rooms = rooms

    def add_room(self, room: Room) -> bool:
        """
        Add room to hotel.

        If a room with the given number already exists, do not add a room and return False.
        Otherwise add the room to hotel and return True.
        """
        if not self.rooms:
            self.rooms = [room]
            return True
        else:
            all_room_numbers = []
            for hotel_room in self.rooms:
                all_room_numbers.append(hotel_room.number)
            if room.number in all_room_numbers:
                return False
            elif room.number not in all_room_numbers:
                self.rooms.append(room)
                return True

    def book_room(self, required_features: list) -> Optional[Room]:
        """
        Book an available room which has the most matching features.

        Find a room which has most of the required features.
        If there are several with the same amount of matching features, return the one with the smallest room number.
        If there is no available rooms, return None
        """
        available_rooms = self.get_available_rooms()
        if len(available_rooms) == 0:
            return None
        else:
            features_covered = 0
            appropriate_room = None
            for room in available_rooms:
                current_features_covered = 0
                for room_feature in room.features:
                    if room_feature in required_features:
                        current_features_covered += 1
                if appropriate_room is None:
                    appropriate_room = [room]
                    features_covered = current_features_covered
                    continue
                else:
                    if current_features_covered > features_covered:
                        features_covered = current_features_covered
                        appropriate_room = [room]
                        print(appropriate_room)
                    elif current_features_covered == features_covered:
                        appropriate_room.append(room)
        room_to_book = min(appropriate_room, key=lambda app_room: (app_room.number, len(app_room.features)))
        room_to_book.booked = True
        return room_to_book

    def get_available_rooms(self) -> list:
        """Return a list of available (not booked) rooms."""
        all_available_rooms = []
        for room in self.rooms:
            if not room.get_booked():
                all_available_rooms.append(room)
        print(all_available_rooms)
        return all_available_rooms

    def get_rooms(self) -> list:
        """Return all the rooms (both booked and available)."""
        if not self.rooms:
            return []
        else:
            return self.rooms

    def get_booked_rooms(self) -> list:
        """Return all the booked rooms."""
        all_booked_rooms = []
        for room in self.rooms:
            if room.get_booked():
                all_booked_rooms.append(room)
        return all_booked_rooms

    def get_feature_profits(self) -> dict:
        """
        Return a dict where key is a feature and value is the total price for the booked rooms which have the feature.

        Example:
            room1, price=100, features=a, b, c
            room2, price=200, features=b, c, d
            room3, price=400, features=a, c

        all the rooms are booked
        result:
        {
        'a': 500,
        'b': 300,
        'c': 700,
        'd': 200
        }
        """
        booked_rooms = self.get_booked_rooms()
        booked_features = {}
        for room in booked_rooms:
            for feature in room.features:
                if feature not in booked_features:
                    booked_features[feature] = room.price
                elif feature in booked_features:
                    booked_features[feature] += room.price
        return booked_features

    def get_most_profitable_feature(self) -> Optional[str]:
        """
        Return the feature which profits the most.

        Use get_feature_profits() method to get the total price for every feature.
        Return the feature which has the highest value (profit).
        If there are several with the same max value, return the feature which is alphabetically lower (a < z)
        If there are no features booked, return None.
        """
        profitable_features = self.get_feature_profits()
        if not profitable_features:
            return None
        sort_profitable = sorted(profitable_features.items(), key=lambda x: (-x[1], x[0]))
        return sort_profitable[0][0]


if __name__ == '__main__':
    hotel = Hotel()
    room1 = Room(22, 100, ['view', 'personal trainer', 'tv', 'vodka'])
    room2 = Room(29, 200, ['moon', 'trump'])
    hotel.add_room(room1)
    hotel.add_room(room2)
    print(hotel.book_room(['moon', 'trump', 'radio', 'personal trainer', 'view', 'moon', 'lamp', 'toilet', 'mountain', 'pool']))

    # TODO: try to add a room so that two or more features have the same profit
