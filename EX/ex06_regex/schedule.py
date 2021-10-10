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
    time_activity = find_schedule_from_text(input_string)
    sorted_time_activities = sorted(time_activity.items(), key=lambda x: x[0])
    formatted_time_activity = []
    max_width_of_time = 0
    max_width_of_activity = 0
    for activity_pair in sorted_time_activities:
        time_formatted = convert_to_12_hour_format(activity_pair[0])
        activity_str = ", ".join(activity_pair[1])
        formatted_time_activity.append((time_formatted, activity_str))
        max_width_of_activity = max(max_width_of_activity, len(activity_str))
        max_width_of_time = max(max_width_of_time, len(time_formatted))
    total_width = max_width_of_time + max_width_of_activity
    if max_width_of_activity == 0 or max_width_of_time == 0:
        total_width = len("No items found") + 4
        print(total_width)
        table = []
        table.append("-" * total_width)
        table.append(f"| {'time':>{5}} | {'items':<{6}} |")
        table.append("-" * total_width)
        table.append(f"| {'No items found'} |")
        table.append("-" * total_width)
        return "\n".join(table)
    table = []
    table.append("-" * (total_width + 7))
    table.append(f"| {'time':>{max_width_of_time}} | {'items':<{max_width_of_activity}} |")
    table.append("-" * (total_width + 7))
    for activity_pair in formatted_time_activity:
        table.append(f"| {activity_pair[0]:>{max_width_of_time}} | {activity_pair[1]:<{max_width_of_activity}} |")
    table.append("-" * (total_width + 7))
    return "\n".join(table)


def find_schedule_from_text(input_string: str) -> dict:
    """
    Find a schedule from a string of text.

    :param input_string: Text that has times and activities in it
    :return: Dictionary of timestamps and activities with it
    """
    time_activity_pattern = r"[^-](\d{1,2})\D(\d{1,2})\s+([a-zA-Z]+)"
    time_activity = {}
    for match in re.finditer(time_activity_pattern, input_string):
        hours = int(match.group(1))
        minutes = int(match.group(2))
        activity = match.group(3)
        if 0 <= hours < 24 and 0 <= minutes < 60:
            timestamp = f"{hours:02}:{minutes:02}"
            if timestamp in time_activity:
                if activity.lower() not in time_activity[timestamp]:
                    time_activity[timestamp].append(activity.lower())
            else:
                time_activity[timestamp] = [activity.lower()]
    return time_activity


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
    if hours == 12:
        return f"{hours}:{minutes} PM"
    else:
        hours = str(int(hours) - 12)
        return f"{hours}:{minutes} PM"


if __name__ == '__main__':
    print(create_schedule_string(""))
    # create_schedule_file("schedule_input.txt", "schedule_output.txt")
