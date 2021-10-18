import csv
from datetime import datetime


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    :param filename: File to read.
    :return: File contents as string.
    """
    content = ""
    with open(filename, "r") as f:
        content = f.read()
    return content


def read_file_contents_to_list(filename: str) -> list:
    """
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    list_of_lines = []
    f = open(filename, "r")
    for row in f.readlines():
        list_of_lines.append(row.rstrip("\n"))
    f.close()
    return list_of_lines


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    rows = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            rows.append(row)
    return rows


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exists, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w") as f:
        f.write(contents)
    return None


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    text = "\n".join(lines)
    write_contents_to_file(filename, text)
    return None


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    print(data)
    with open(filename, 'w', newline='') as csv_file:
        if len(data) == 0:
            return None
        csv_writer = csv.writer(csv_file, delimiter=",")
        for row in data:
            # write list of values
            csv_writer.writerow(row)
    return None


def merge_dates_and_towns_into_csv(dates_file: str, towns_file: str, csv_output: str) -> None:
    """
    Merge information from two files into one CSV file.

    dates_file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    towns_file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_file: Input file with names and dates.
    :param towns_file: Input file with names and towns.
    :param csv_output: Output CSV-file with names, towns and dates.
    :return: None
    """
    result = [["name", "town", "date"]]
    date = read_csv_file(dates_file)
    town = read_csv_file(towns_file)
    for row in date[0]:
        split_name_date = row.split(":")
        result.append([split_name_date[0], "-", split_name_date[1]])
    for row in town[0]:
        no_name_in_result = True
        split_name_town = row.split(":")
        for lines in result:
            if split_name_town[0] == lines[0]:
                no_name_in_result = False
                lines[1] = split_name_town[1]
        if no_name_in_result:
            result.append([split_name_town[0], split_name_town[1], "-"])
    print(result)
    return None


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """
    Read csv file into list of dictionaries.
    Header line will be used for dict keys.

    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:

    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    The order of the elements in the list should be the same
    as the lines in the file (the first line becomes the first element etc.)

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    contents_of_csv = read_csv_file(filename)
    if len(contents_of_csv) == 0:
        return []
    if len(contents_of_csv) == 1:
        return []
    else:
        list_of_dicts = []
        dictionary_keys = contents_of_csv[0]
        for data in range(1, len(contents_of_csv)):
            info = contents_of_csv[data]
            new_dict = dict(zip(dictionary_keys, info))
            list_of_dicts.append(new_dict)
        return list_of_dicts


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    if len(data) == 0:
        write_csv_file(filename, data)
        return None
    all_keys = get_all_keys(data)
    all_elements = [list(all_keys)]
    for diction in data:
        row = []
        for key in all_keys:
            if key in diction:
                element = diction[key]
                row.append(element)
            else:
                element = ""
                row.append(element)
        all_elements.append(row)
    write_csv_file(filename, all_elements)
    return None


def get_all_keys(list_of_dict: list) -> set:
    """
    From a list of dictionaries find all unique keys.

    :param list_of_dict: list of dictionaries
    :return: set of all unique keys
    """
    all_keys = set()
    for dictionary in list_of_dict:
        keys = dictionary.keys()
        for key in keys:
            all_keys.add(key)
    return all_keys


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """
    Read data from file and cast values into different datatypes.
    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
    list_of_dicts = read_csv_file_into_list_of_dicts(filename)
    sorted_dictionaries = sort_dictionaries(list_of_dicts)
    all_values = []
    all_keys = []
    for category in sorted_dictionaries:
        all_keys.append(category)
        values = sorted_dictionaries[category]
        values = remove_no_value_fields(values)
        values = check_if_all_ints(values)
        values = check_if_all_dates(values)
        all_values.append(values)
    people_list = list(zip(*all_values))
    final_list = []
    for item in people_list:
        new_dict = dict(zip(all_keys, item))
        final_list.append(new_dict)
    return final_list


def sort_dictionaries(all_dictionaries: list) -> list:
    """
    Sort dictionaries by categories.

    :param all_dictionaries: Dictionries to be sorted
    :return:
    """
    all_the_keys = list(all_dictionaries[0].keys())
    all_values = {}
    for dic in all_dictionaries:
        for key in all_the_keys:
            if key not in all_values:
                value = dic[key]
                all_values[key] = [value]
            else:
                value = dic[key]
                all_values[key].append(value)
    return all_values


def check_if_all_ints(list_of_strings: list) -> list:
    """
    Check if all the strings can be cast as an integer.

    :param list_of_strings: List of strings to check.
    :return: If they are all integers, return the list as integers, else return original list.
    """
    new_list = []
    for word in list_of_strings:
        if word is None:
            new_list.append(None)
            continue
        try:
            new_list.append(int(word))
        except ValueError:
            return list_of_strings
    return new_list


def check_if_all_dates(list_of_strings: list) -> list:
    """
    Check if all the strings can be cast as a date.

    :param list_of_strings: List of strings to check.
    :return: If they are all integers, return the list as integers, else return original list.
    """
    new_list = []
    for word in list_of_strings:
        if word is None:
            new_list.append(None)
            continue
        try:
            date_object = datetime.strptime(word, "%d.%m.%Y")
            new_list.append(date_object)
        except TypeError:
            return list_of_strings
        except ValueError:
            return list_of_strings
    return new_list


def remove_no_value_fields(list_of_values: list) -> list:
    """
    Replace all the "-" values with None.

    :param list_of_values: list of all the values.
    :return: list of values with missing values replaced by None
    """
    new_list = []
    for word in list_of_values:
        if word == "-":
            new_list.append(None)
        else:
            new_list.append(word)
    return new_list


if __name__ == "__main__":
    print(read_csv_file_into_list_of_dicts_using_datatypes("test.csv"))
