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
    total_width = max_width_of_time + max_width_of_activity + 7
    table = []
    table.append("-" * (total_width + 7))
    table.append(f"| {'time':>{max_width_of_time}} | {'items':<{max_width_of_activity}} |")
    table.append("-" * (total_width + 7))
    for activity_pair in formatted_time_activity:
        table.append(f"| {activity_pair[0]:>{max_width_of_time}} | {activity_pair[1]:<{max_width_of_activity}} |")
    table.append("-" * (total_width + 7))
    return "\n".join(table)


def find_schedule_from_text(input_string: str) -> dict:
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
    print(create_schedule_string("start wsilnxeqj pftbkm rftjpahv xhfuxglbu qynzahyqj sxfmnhgs tqswbd 07,39   AVdPZh jjxahfz pvqzuy cakmghi jwelabwkgn knbexaqo prhbi urctd whjwfbvtly 09b33   AvdpzH qedwauova nykgkfvsac 23B25    XTTDalWeNv 7B08    XTtDAlWEnV dkjimmv tyoreqecqu uaqcyxwqyk hkeuvcyuuq qukvl zlkpd lsuydlhvlw zhrfet 23!46    zpcAmfi tockymzed yqyornaism ysafindn 11B43  QJqXEEa kkajwcllh pgrzly glsqprdajp tluqy 15!14    XttdALWeNv ikzkn agxgsrbsri kukra sjjnmuss wpsqntoto fkwytmfm wngegi npfvvi ihznm 17,45    jjybubO kkfeqsz eblgvce lkvsq klfdrw gbwvf kuvpkr xudss -1:39  xtTdalweNv txoymi hfolm twhjgc ktmdp 2A-1    aVDpzh kaantvxbsy esnnv aogrj dwanaxrx okdyyox giuqji 20A29    AJhmRxO uqmxmw atlaqnxpfu rlxoo zqxfnl wpidf qfsiwwrgs bghysxnm acuwxhwok melbk 17=21    QJqXEea hzncnjkl pemorpvxe tfdbgx wgkqyzzer ymhyogai 19A02  jjybUBO vzbonj yjqyct pstcnmrm bdapdhnsdf ohvoe syuprhvlpz oaktftn eawjw 12:00 ajHmRxO xshvketr tbclxkqukt tjsmtlz phiitzjtre gspicbyga redvcsuai vtjtvmwhu jmseqo pzheddzw 17?42  ajHMRXo gzmnrxped xpgyikp 25a36  XTTdAlWenV qwkwen nnptoosvb gfduywpbio kecaxlmzyn iwtyubnxls"))
    # create_schedule_file("schedule_input.txt", "schedule_output.txt")
