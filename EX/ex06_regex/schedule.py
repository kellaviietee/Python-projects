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
    time_activity_pattern = r"(\d{1,2})\D(\d{1,2})\s+([a-zA-Z]+)"
    time_activity = {}
    for match in re.finditer(time_activity_pattern, input_string):
        hours = int(match.group(1))
        minutes = int(match.group(2))
        activity = match.group(3)
        if hours < 24 and minutes < 60:
            timestamp = f"{hours:02}:{minutes:02}"
            if timestamp in time_activity:
                if activity not in time_activity[timestamp]:
                    time_activity[timestamp].append(activity.lower())
            else:
                time_activity[timestamp] = [activity.lower()]
    time_activity = convert_dictionary_to_12h_format(time_activity)
    sorted_time_activities = sorted(time_activity.items(), key=lambda x: x[0])
    time_activity.clear()
    for times in sorted_time_activities:
        time_activity[times[0]] = times[1]
    time_activity = make_all_activities_single_item(time_activity)
    line_lengths = get_table_size(time_activity)
    table = []
    if line_lengths == [0, 0, 0]:
        table.append("-" * 18)
        table.append(f"| {'time':>{5}} | {'items':<{6}} |")
        table.append("-" * 18)
        table.append(f"| {'No Items found':^{10}} |")
        table.append("-" * 18)
        return "\n".join(table)
    table.append("-" * (line_lengths[2] + 7))
    # | time | items |
    table.append(f"| {'time':>{line_lengths[0]}} | {'items':<{line_lengths[1]}} |")
    table.append("-" * (line_lengths[2] + 7))
    for time_str, activity_str in time_activity.items():
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


def get_table_size(schedule_dict: dict) -> list:
    """
    Get the needed line lengths to create a schedule table.

    :param schedule_dict: Sorted dictionary of schedule times and activities.
    :return: List of parameters to be used to create the schedule table.
    """
    if len(schedule_dict.keys()) == 0 or len(schedule_dict.values()) == 0:
        return [0, 0, 0]

    maximum_time_length = max(len(time) for time in schedule_dict)
    maximum_activity_length = max(len(activity) for activity in schedule_dict.values())
    return [maximum_time_length, maximum_activity_length, maximum_activity_length + maximum_time_length]


def convert_to_12_hour_format(time: str) -> str:
    """
    Convert 24 hour times into 12h times.

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
    for events in schedule_list:
        hours = int(events[0])
        minutes = int(events[1])
        if hours < 24 and minutes < 59:
            timestamp = f"{str(events[0]).zfill(2)}:{str(events[1]).zfill(2)}"
            if timestamp not in time_activity_dict.keys():
                time_activity_dict[timestamp] = [events[2].lower()]
            elif timestamp in time_activity_dict.keys() and events[2].lower() in time_activity_dict[timestamp]:
                continue
            else:
                time_activity_dict[timestamp].append(events[2].lower())
    keys_sorted = sorted(time_activity_dict.keys())
    sorted_dict = {}
    for key in keys_sorted:
        sorted_dict[key] = time_activity_dict[key]
    return sorted_dict


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    #create_schedule_file("schedule_input.txt", "schedule_output.txt")
