"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    with open(input_filename, "r", encoding="utf-8") as fin:
        with open(output_filename, "w", encoding="utf-8") as fout:
            table_str = create_schedule_string(fin.read())
            fout.write(table_str)


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    time_activity_pattern = r"(?<=\s)(\d?\d)\D(\d?\d)\s+(\w+)"
    time_activity = re.findall(time_activity_pattern, input_string)
    time_activity_dict = create_sorted_schedule_dictionary(time_activity)
    converted_dict = convert_dictionary_to_12h_format(time_activity_dict)
    converted_single_dict = make_all_activities_single_item(converted_dict)
    line_lengths = get_table_size(converted_single_dict)
    print(line_lengths)
    table = []
    table.append("-" * (line_lengths[2] + 7))
    # | time | items |
    table.append(f"| {'time':>{line_lengths[0]}} | {'items':<{line_lengths[1]}} |")
    table.append("-" * (line_lengths[2] + 7))
    for time_str, activity_str in converted_single_dict.items():
        table.append(f"| {time_str:>{line_lengths[0]}} | {activity_str:<{line_lengths[1]}} |")
    table.append("-" * (line_lengths[2] + 7))
    return "\n".join(table)


def make_all_activities_single_item(converted_dictionary: dict) -> dict:
    """
    Join all activities into one single list as a string.

    :param converted_dictionary: Dictionary with correct times and activities in it as a list
    :return: Dictionary with all keys having a single string as values
    """
    for times in converted_dictionary.keys():
        if len(converted_dictionary[times]) > 0:
            joined_list = ", ".join(converted_dictionary[times])
            converted_dictionary[times] = joined_list
    return converted_dictionary


def convert_dictionary_to_12h_format(dictionary_with_24h: dict) -> dict:
    """
    Convert dictionary with 24h time format to a one with 12h time formats.

    :param dictionary_with_24h:
    :return: dictionary that has 12h formats in it
    """
    times = list(dictionary_with_24h.keys())
    activities = list(dictionary_with_24h.values())
    for time in range(0, len(times)):
        new_time = convert_to_12_hour_format(times[time])
        times[time] = new_time
    time_activity_dict_12h = {}
    for time_slots in range(0, len(times)):
        time_activity_dict_12h[times[time_slots]] = activities[time_slots]
    return time_activity_dict_12h


def create_table(table_size: list) -> None:
    """
    Create a table with specified table_size
    :param table_size: Consists of first column width, second column width, total width and number of rows.
    :return: table with these parameters
    """
    text = "-"
    first_row = text.center(table_size[2] - 1, "-")
    pass


def get_table_size(schedule_dict: dict) -> list:
    """
    Get the needed line lengths to create a schedule table.

    :param schedule_dict: Sorted dictionary of schedule times and activities.
    :return: List of parameters to be used to create the schedule table.
    """
    maximum_time_length = max(len(time) for time in schedule_dict)
    maximum_activity_length = max(len(activity) for activity in schedule_dict.values())
    return maximum_time_length, maximum_activity_length, maximum_activity_length + maximum_time_length


def convert_to_12_hour_format(time: str) -> str:
    """
    Converts 24 hour times into 12h times
    :param time: Timestamp in 24 hour clock format
    :return: Time in 12h time format
    """
    hours = int(time[0:2])
    minutes = time[3:5]
    if hours < 12:
        if hours == 0:
            hours = 12
        return f"{hours}:{minutes} AM"
    else:
        hours = str(int(hours) - 12)
        return f"{hours}:{minutes} PM"


def create_sorted_schedule_dictionary(schedule_list: list) -> dict:
    """
    Create a schedule dictionary out of schedule list.

    Create schedule dictionary and group together timestamps.
    :param schedule_list: list of times and activities
    :return: Schedule dictionary
    """
    time_activity_dict = {}
    for event in schedule_list:
        if int(event[0]) < 24 and int(event[1]) < 60:
            time = event[0].zfill(2) + ":" + event[1].zfill(2)
            if time not in time_activity_dict:
                time_activity_dict[time] = [event[2].lower()]
            elif time in time_activity_dict:
                time_activity_dict[time].append(event[2].lower())
    dic_items = time_activity_dict.items()
    sorted_items = sorted(dic_items)
    time_activity_dict.clear()
    for time_activity in sorted_items:
        time_activity_dict[time_activity[0]] = time_activity[1]
    return time_activity_dict


if __name__ == '__main__':
    print(create_schedule_string("wat 0:00 Teine tekst 0:0 jah ei 3:00 PIKKikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
