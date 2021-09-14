import math


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2) -> int:
    """Calculate the meeting position of 2 jangurus.
    @:param pos1: position of first janguru
    @:param jump_distance1: jump distance of first janguru
    @:param sleep1: sleep time of first janguru
    @:param pos2: position of second janguru
    @:param jump_distance2: jump distance of second janguru
    @:param sleep2: sleep time of second janguru

    @:return positions where jangurus first meet
    """
    speed1 = jump_distance1 / sleep1
    speed2 = jump_distance2 / sleep2
    first_pos1 = pos1 + jump_distance1
    first_pos2 = pos2 + jump_distance2

    if speed1 <= speed2 and (first_pos2 - first_pos1) >= jump_distance1:
        return -1
    if speed2 <= speed1 and (first_pos1 - first_pos2) >= jump_distance2:
        return -1
    else:
        pos1 += jump_distance1
        pos2 += jump_distance2
        meet_time = (pos2 - pos1) / (speed1 - speed2)
        meet_time = round(meet_time)
        if meet_time <= 0:
            return -1
        lcm = math.lcm(sleep1, sleep2)
        closest_multiple_of_lcm = math.floor(meet_time / lcm)
        start_lcm = lcm * closest_multiple_of_lcm
        time_stamps = [start_lcm]
        step_loc = []
        step = 1
        while (lcm - step * sleep1) > 0:
            step_loc.append(lcm - step * sleep1)
            step += 1
        step = 1
        while (lcm - step * sleep2) > 0:
            step_loc.append(lcm - step * sleep2)
            step += 1
        if start_lcm - lcm >= 1:
            time_stamps.append(start_lcm - lcm)
        time_stamps.append(start_lcm + lcm)
        for time_loc in step_loc:
            if start_lcm - time_loc >= 1:
                time_stamps.append(start_lcm - time_loc)
            time_stamps.append(start_lcm + time_loc)
        time_stamps = sorted(time_stamps)
        for time_check in time_stamps:
            test_pos1 = pos1 + math.floor(time_check / sleep1) * jump_distance1
            test_pos2 = pos2 + math.floor(time_check / sleep2) * jump_distance2
            if test_pos1 == test_pos2:
                return test_pos1
        return -1

