"""Exercise 7 of introduction to programming."""

import csv
from datetime import datetime
import os


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
    r"""
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
    date = read_file_contents_to_list(dates_file)
    town = read_file_contents_to_list(towns_file)
    for items in date:
        hmm = items.split(":")
        result.append([hmm[0], "-", hmm[1]])
    all_names = []
    for data in result:
        all_names.append(data[0])
    for items in town:
        hmm = items.split(":")
        if hmm[0] not in all_names:
            result.append([hmm[0], hmm[1], "-"])
        else:
            index = all_names.index(hmm[0])
            result[index][1] = hmm[1]
    write_csv_file(csv_output, result)
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
    Read data from file and cast values into different datatype.

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


def sort_dictionaries(all_dictionaries: list) -> dict:
    """
    Sort dictionaries by categories.

    :param all_dictionaries: Dictionaries to be sorted
    :return:
    """
    if len(all_dictionaries) == 0:
        return {}
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
            date_object = datetime.strptime(word, "%d.%m.%Y").date()
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


def read_people_data(directory: str) -> dict:
    """
    Read people data from files.

    Files are inside directory. Read all *.csv files.
    Each file has an int field "id" which should be used to merge information.
    The result should be one dict where the key is id (int) and value is
    a dict of all the different values across the the files.
    Missing keys should be in every dictionary.
    Missing value is represented as None.

    File: a.csv
    id,name
    1,john
    2,mary
    3,john

    File: births.csv
    id,birth
    1,01.01.2001
    2,05.06.1990

    File: deaths.csv
    id,death
    2,01.02.2020
    1,-

    Becomes:
    {
        1: {"id": 1, "name": "john", "birth": datetime.date(2001, 1, 1), "death": None},
        2: {"id": 2, "name": "mary", "birth": datetime.date(1990, 6, 5),
            "death": datetime.date(2020, 2, 1)},
        3: {"id": 3, "name": "john", "birth": None, "death": None},
    }


    :param directory: Directory where the csv files are.
    :return: Dictionary with id as keys and data dictionaries as values.
    """
    entries = os.listdir(directory)
    all_tables = []
    max_number_of_ids = 0
    for entry in entries:
        table = read_csv_file_into_list_of_dicts_using_datatypes(directory + "/" + entry)
        all_tables.append(table)
        max_number_of_ids = max(max_number_of_ids, len(table))
    all_keys = []
    all_ids = []
    for table in all_tables:
        for dic in table:
            keys = list(dic.keys())
            for key in keys:
                if key == "id":
                    if dic[key] not in all_ids:
                        all_ids.append(dic[key])
                if key not in all_keys:
                    all_keys.append(key)
    all_dics = {}
    for num in range(0, len(all_ids)):
        num_dic = combine_dictionaries_by_id(all_tables, all_ids[num], all_keys)
        all_dics[all_ids[num]] = num_dic
    return all_dics


def combine_dictionaries_by_id(all_tables: list, num: int, all_keys: list) -> dict:
    """
    Combine a list of dictionaries into single dictionary by id.

    :param all_tables: All tables that has dictionaries in it
    :param num: id number to collect them by
    :param all_keys: all the possible keys
    :return: Dictionary that is merged by the id.
    """
    num_dict = {}
    for table in all_tables:
        for dic in table:
            if dic["id"] == num:
                num_dict.update(dic)
    for key in all_keys:
        if key not in num_dict:
            num_dict[key] = None
    return num_dict


def generate_people_report(person_data_directory: str, report_filename: str) -> None:
    """
    Generate report about people data.

    Data should be read using read_people_data().

    The input files contain fields "birth" and "death" which are dates. Those can be in different files. There are no duplicate headers in the files (except for the "id").

    The report is a CSV file where all the fields are written to
    (along with the headers).
    In addition, there should be two fields:
    - "status" this is either "dead" or "alive" depending on whether
    there is a death date
    - "age" - current age or the age when dying.
    The age is calculated as full years.
    Birth 01.01.1940, death 01.01.2020 - age: 80
    Birth 02.01.1940, death 01.01.2020 - age: 79

    If there is no birth date, then the age is -1.

    When calculating age, dates can be compared.

    The lines in the files should be ordered:
    - first by the age ascending (younger before older);
      if the age cannot be calculated, then those lines will come last
    - if the age is the same, then those lines should be ordered
      by birthdate descending (newer birth before older birth)
    - if both the age and birth date are the same,
      then by name ascending (a before b). If name is not available, use "" (people with missing name should be before people with  name)
    - if the names are the same or name field is missing,
      order by id ascending.

    Dates in the report should in the format: dd.mm.yyyy
    (2-digit day, 2-digit month, 4-digit year).

    :param person_data_directory: Directory of input data.
    :param report_filename: Output file.
    :return: None
    """
    data = read_people_data(person_data_directory)
    for person in data:
        person_data = data[person]
        if person_data["death"] is None:
            person_data["status"] = "alive"
        else:
            person_data["status"] = "dead"
        if person_data["birth"] is None:
            person_data["age"] = -1
        elif person_data["status"] == "alive":
            today = datetime.today().date()
            birth = person_data["birth"]
            time_difference = today - birth
            number_of_years = int((time_difference.days / 365.2425))
            person_data["age"] = number_of_years
        elif person_data["status"] == "dead" and person_data["birth"] is not None:
            death = person_data["death"]
            birth = person_data["birth"]
            time_difference = death - birth
            number_of_years = int((time_difference.days / 365.2425))
            person_data["age"] = number_of_years
    list_to_write = sorted(data.values(), key=lambda x: (
        x["age"] if x["age"] > -1 else 1000,
        -sort_people_by_birth(x["birth"]),
        x["name"] if x["name"] is not None else -1000,
        x["id"]))
    write_list_of_dicts_to_csv_file(report_filename, list_to_write)


def sort_people_by_birth(birthdate) -> int:
    """
    Sort people by their birth.

    :param birthdate:
    :return:
    """
    if birthdate is None:
        return 100000000
    else:
        return -(datetime.today().date() - birthdate).days


def sort_people_by_age(dic_of_dics: dict) -> dict:
    """
    Sort people by their age inside of the dictionary.

    :param dic_of_dics:
    :return:
    """
    all_ages = []
    all_non_ages = []
    for people in dic_of_dics:
        person_data = dic_of_dics[people]
        age = person_data["age"]
        if age != -1:
            all_ages.append(age)
        else:
            all_non_ages.append(age)
    all_ages = sorted(all_ages)
    reordered_dictionary = {}
    for age in all_ages:
        for people in dic_of_dics:
            person_data = dic_of_dics[people]
            if person_data["age"] == age:
                reordered_dictionary[person_data["id"]] = person_data
    for age in all_non_ages:
        for people in dic_of_dics:
            person_data = dic_of_dics[people]
            if person_data["age"] == age:
                reordered_dictionary[person_data["id"]] = person_data
    return reordered_dictionary


if __name__ == "__main__":
    print(generate_people_report("data", "report.csv"))
