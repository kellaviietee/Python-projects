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
    if (pos1 < pos2) and (speed1 <= speed2):
        return -1
    if (pos2 < pos1) and (speed2 <= speed1):
        return -1
    if (pos1 < pos2) and (speed1 > speed2):
        time = 0
        pos1_sleep = 1
        pos2_sleep = 1
        while pos1 <= pos2 + jump_distance2:
            if pos1 == pos2:
                return pos1
            pos1_sleep -= 1
            pos2_sleep -= 1
            if pos1_sleep <= 0:
                pos1 += jump_distance1
                pos1_sleep = sleep1
            if pos2_sleep <= 0:
                pos2 += jump_distance2
                pos2_sleep = sleep2


            time += 1
    if (pos2 < pos1) and (speed2 > speed1):
        time = 0
        pos2_sleep = 1
        pos1_sleep = 1
        while pos2 <= pos1 + jump_distance1:
            if pos1 == pos2:
                return pos1
            pos2_sleep -= 1
            pos1_sleep -= 1
            if pos2_sleep <= 0:
                pos2 += jump_distance2
                pos2_sleep = sleep2
            if pos1_sleep <= 0:
                pos1 += jump_distance1
                pos1_sleep = sleep1
            time += 1
    else:
        return -1
