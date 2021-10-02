"""Hobbies."""


def sort_dictionary(dic: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dic: dictionary to sort
    :return: sorted dictionary
    """
    for key in dic:
        initial_list = dic[key]
        initial_list.sort()
        dic[key] = initial_list
    return dic


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    new_dict = {}
    names_and_hobbies = data.splitlines()
    for name_hobby in names_and_hobbies:
        dict_pair = name_hobby.split(":")
        if dict_pair[0] not in new_dict.keys():
            new_dict[dict_pair[0]] = [dict_pair[1]]
        if dict_pair[0] in new_dict.keys() and dict_pair[1] not in new_dict[dict_pair[0]]:
            new_dict[dict_pair[0]].append(dict_pair[1])
    return new_dict


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.

    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    new_dict = {}
    names_and_hobbies = data.splitlines()
    for name_hobby in names_and_hobbies:
        dict_pair = name_hobby.split(":")
        if dict_pair[1] not in new_dict.keys():
            new_dict[dict_pair[1]] = [dict_pair[0]]
        if dict_pair[1] in new_dict.keys() and dict_pair[0] not in new_dict[dict_pair[1]]:
            new_dict[dict_pair[1]].append(dict_pair[0])
    sorted_new_dic = sort_dictionary(new_dict)
    return sorted_new_dic


def find_people_with_most_hobbies(data: str) -> list:
    """
    Find the people who have most hobbies.

    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    maximum_number_hobbies = 0
    names_of_highest_hobby_numbers = []
    name_hobby_dict = create_dictionary(data)
    for name in name_hobby_dict:
        number_of_hobbies = len(name_hobby_dict[name])
        if number_of_hobbies > maximum_number_hobbies:
            maximum_number_hobbies = number_of_hobbies
            names_of_highest_hobby_numbers.clear()
            names_of_highest_hobby_numbers.append(name)
        elif number_of_hobbies == maximum_number_hobbies:
            names_of_highest_hobby_numbers.append(name)
    names_of_highest_hobby_numbers.sort()
    return names_of_highest_hobby_numbers


def find_people_with_least_hobbies(data: str) -> list:
    """
    Find the people who have least hobbies.

    :param data: given string from database
    :return: list of people with least hobbies. Sorted alphabetically.
    """
    name_hobby_dict = create_dictionary(data)
    highest_names = find_people_with_most_hobbies(data)
    highest_number = len(name_hobby_dict[highest_names[0]])
    names_of_least_hobbies = []
    for name in name_hobby_dict:
        number_of_hobbies = len(name_hobby_dict[name])
        if number_of_hobbies < highest_number:
            highest_number = number_of_hobbies
            names_of_least_hobbies.clear()
            names_of_least_hobbies.append(name)
        elif number_of_hobbies == highest_number:
            names_of_least_hobbies.append(name)
    names_of_least_hobbies.sort()
    return names_of_least_hobbies


def find_most_popular_hobbies(data: str) -> list:
    """
    Find the most popular hobbies.

    :param data: given string from database
    :return: list of most popular hobbies. Sorted alphabetically.
    """
    name_hobby_dict = create_dictionary(data)
    all_hobbies = name_hobby_dict.values()
    unique_hobbies = find_unique_hobbies(all_hobbies)
    hobby_name_dict = create_hobby_number_dict(unique_hobbies,all_hobbies)
    number_of_people = 0
    most_popular_hobbies = []
    for hobby in hobby_name_dict:
        if hobby_name_dict[hobby] > number_of_people:
            most_popular_hobbies.clear()
            number_of_people = hobby_name_dict[hobby]
            most_popular_hobbies.append(hobby)
        elif hobby_name_dict[hobby] == number_of_people:
            most_popular_hobbies.append(hobby)
    most_popular_hobbies.sort()
    return most_popular_hobbies


def create_hobby_number_dict(unique_hobbies: list, all_hobbies: list) -> dict:
    """
    Create a dictionary of how many people practices  a hobby.
    :param unique_hobbies: List of unique hobbies
    :param all_hobbies: list of list of peoples hobbies
    :return:
    """
    hobby_name_dict = {}
    for hobby in unique_hobbies:
        number_of_practitioners = 0
        for hobby_list in all_hobbies:
            if hobby in hobby_list:
                number_of_practitioners += 1
        hobby_name_dict[hobby] = number_of_practitioners
    return hobby_name_dict


def find_unique_hobbies(all_hobbies: list) -> list:
    """
    Find all the unique hobbies.
    :param all_hobbies: given list of everybodys hobbies
    :return: list of all of the unique hobbies
    """
    all_hobbies_single_list = []
    for hobby_list in all_hobbies:
        all_hobbies_single_list += hobby_list
    unique_hobbies_set = set(all_hobbies_single_list)
    unique_hobbies_list = []
    for hobby in unique_hobbies_set:
        unique_hobbies_list.append(hobby)
    unique_hobbies_list.sort()
    return unique_hobbies_list


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the least popular hobbies.

    :param data: given string from database
    :return: list of least popular hobbies. Sorted alphabetically.
    """
    name_hobby_dict = create_dictionary(data)
    all_hobbies = name_hobby_dict.values()
    unique_hobbies = find_unique_hobbies(all_hobbies)
    hobby_name_dict = create_hobby_number_dict(unique_hobbies,all_hobbies)
    number_of_people = hobby_name_dict[unique_hobbies[0]]
    least_popular_hobbies = []
    for hobby in hobby_name_dict:
        if hobby == unique_hobbies[0]:
            continue
        if hobby_name_dict[hobby] < number_of_people:
            least_popular_hobbies.clear()
            number_of_people = hobby_name_dict[hobby]
            least_popular_hobbies.append(hobby)
        elif hobby_name_dict[hobby] == number_of_people:
            least_popular_hobbies.append(hobby)
    least_popular_hobbies.sort()
    return least_popular_hobbies


def sort_names_and_hobbies(data: str) -> tuple:
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first element is the name (string)
    and the second element is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.
    """
    hobbyist_dict = create_dictionary(data)
    sorted_dict = sort_dictionary(hobbyist_dict)
    list_of_names = list(hobbyist_dict.keys())
    list_of_names.sort()
    name_hobbies_list = []
    for name in list_of_names:
        new_tuple = (name, tuple(sorted_dict[name]))
        name_hobbies_list.append(new_tuple)
    final_tuple = tuple(name_hobbies_list)
    return final_tuple


if __name__ == '__main__':
    sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    dic = create_dictionary(sample_data)
    print("shopping" in dic["Wendy"])  # -> True
    print("fitness" in dic["Sophie"])  # -> False
    print("gaming" in dic["Peter"])  # -> True
    print(find_people_with_most_hobbies(sample_data))  # -> ['Jack']
    print(len(dic["Jack"]))  # ->  12
    print(len(dic["Carmen"]))  # -> 10
    print(find_people_with_least_hobbies(sample_data))  # -> ['Molly']
    print(len(dic["Molly"]))  # -> 5
    print(len(dic["Sophie"]))  # -> 7
    print(find_most_popular_hobbies(sample_data))  # -> ['football', 'gaming', 'sport']
    print(find_least_popular_hobbies(sample_data))  # -> ['dance', 'flowers', 'puzzles', 'tennis']
    print(create_dictionary_with_hobbies(sample_data))
    sort_result = sort_names_and_hobbies(sample_data)
    # if the condition after assert is False, error will be thrown
    assert isinstance(sort_result, tuple)
    assert len(sort_result) == 10
    assert sort_result[0][0] == 'Alfred'
    assert len(sort_result[0][1]) == 7
    assert sort_result[-1] == ('Wendy', ('fishing', 'fitness', 'football', 'gaming', 'photography', 'puzzles', 'shopping', 'sport', 'theatre'))
    # if you see this line below, then everything seems to be ok!
    print("sorting works!")

    # print(sort_names_and_hobbies(sample_data))