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
    else:
        if (pos2 > pos1) and (speed1 > speed2):
            relative_distance = pos2 - pos1
            relative_speed = speed1 - speed2
            time = relative_distance / relative_speed
            return pos1 + speed1 * time
        if (pos1 > pos2) and (speed2 > speed1):
            relative_distance = pos1 - pos2
            relative_speed = speed2 - speed1
            time = relative_distance / relative_speed
            return pos2 + speed2 * time


