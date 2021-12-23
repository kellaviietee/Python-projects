"""Roomba robot."""

from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """Just testing the roomba."""
    robot.set_wheels_speed(30)
    robot.sleep(5)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
    """Drive to the line and then some."""
    while robot.get_line_sensors() == [1024, 1024, 1024, 1024, 1024, 1024]:
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
        robot.set_wheels_speed(0)
    print(robot.get_position())
    robot.set_wheels_speed(25)
    robot.sleep(1)
    print(robot.get_position())
    robot.done()


def follow_the_line(robot: FollowerBot):
    """Just following continuous line as best as it can."""
    while robot.get_line_sensors() == [1024, 1024, 1024, 1024, 1024, 1024]:
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
        robot.set_wheels_speed(0)
    left_on_line = robot.get_left_line_sensors().count(0)
    right_on_line = robot.get_right_line_sensors().count(0)
    while 0 in robot.get_line_sensors():
        if left_on_line == right_on_line:
            robot.set_wheels_speed(100)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            left_on_line = robot.get_left_line_sensors().count(0)
            right_on_line = robot.get_right_line_sensors().count(0)
        elif left_on_line == right_on_line + 1:
            print("this triggers")
            robot.set_left_wheel_speed(100)
            robot.set_right_wheel_speed(0)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            left_on_line = robot.get_left_line_sensors().count(0)
            right_on_line = robot.get_right_line_sensors().count(0)
        elif left_on_line == right_on_line - 1:
            print("this triggers 2")
            robot.set_left_wheel_speed(0)
            robot.set_right_wheel_speed(100)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            left_on_line = robot.get_left_line_sensors().count(0)
            right_on_line = robot.get_right_line_sensors().count(0)
        elif left_on_line == right_on_line + 2:
            print("this triggers 3")
            robot.set_left_wheel_speed(50)
            robot.set_right_wheel_speed(-50)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            left_on_line = robot.get_left_line_sensors().count(0)
            right_on_line = robot.get_right_line_sensors().count(0)
        elif left_on_line == right_on_line - 2:
            print("this triggers 4")
            robot.set_left_wheel_speed(-50)
            robot.set_right_wheel_speed(50)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            left_on_line = robot.get_left_line_sensors().count(0)
            right_on_line = robot.get_right_line_sensors().count(0)
        elif left_on_line == right_on_line + 3:
            print("this triggers 5")
            robot.set_left_wheel_speed(100)
            robot.set_right_wheel_speed(-100)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            left_on_line = robot.get_left_line_sensors().count(0)
            right_on_line = robot.get_right_line_sensors().count(0)
        elif left_on_line == right_on_line - 3:
            print("this triggers 6")
            robot.set_left_wheel_speed(-100)
            robot.set_right_wheel_speed(100)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            left_on_line = robot.get_left_line_sensors().count(0)
            right_on_line = robot.get_right_line_sensors().count(0)
        else:
            break
    print(robot.get_line_sensors())
    robot.done()


def the_true_follower(robot: FollowerBot):
    """All kind of following happening here."""
    initial_drive_to_the_line(robot)
    drive_along_the_path(robot)
    if 500 < robot.get_left_line_sensor() < 1024 and 500 < robot.get_right_line_sensor() < 1024:
        turn_robot_around(robot)
    drive_along_the_path(robot)
    robot.done()


def initial_drive_to_the_line(robot: FollowerBot):
    """Driving to the line and no more."""
    while robot.get_line_sensors() == [1024, 1024, 1024, 1024, 1024, 1024]:
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
        robot.set_wheels_speed(0)
    return


def drive_along_the_path(robot: FollowerBot):
    """Driving on continous and dashed lines."""
    initial_sensors = robot.get_line_sensors()
    command = "straight"
    while command != "stop":
        current_sensors = robot.get_line_sensors()
        turn_robot_around(robot)
        if current_sensors != initial_sensors:
            adjustment = make_adjustment(robot)
            command = adjustment[0]
            initial_sensors = adjustment[1]
        if command == "straight":
            robot.set_wheels_speed(80)
            robot.sleep(0.01)


def make_adjustment(robot: FollowerBot) -> list:
    if robot.get_left_line_sensors() == robot.get_right_line_sensors() and 0 in robot.get_line_sensors():
        return ["straight", robot.get_line_sensors()]
    elif robot.get_second_line_sensor_from_left() < robot.get_second_line_sensor_from_right():
        robot.set_left_wheel_speed(100)
        robot.set_right_wheel_speed(-100)
        robot.sleep(0.01)
        robot.set_wheels_speed(0)
        return ["straight", robot.get_line_sensors()]
    elif robot.get_second_line_sensor_from_left() > robot.get_second_line_sensor_from_right():
        robot.set_left_wheel_speed(-100)
        robot.set_right_wheel_speed(100)
        robot.sleep(0.01)
        robot.set_wheels_speed(0)
        return ["straight", robot.get_line_sensors()]
    elif 0 in robot.get_left_line_sensors() and 0 not in robot.get_right_line_sensors():
        robot.set_left_wheel_speed(100)
        robot.set_right_wheel_speed(-100)
        robot.sleep(0.15)
        robot.set_wheels_speed(0)
        return ["straight", robot.get_line_sensors()]
    elif 0 in robot.get_right_line_sensors() and 0 not in robot.get_left_line_sensors():
        robot.set_left_wheel_speed(-100)
        robot.set_right_wheel_speed(100)
        robot.sleep(0.15)
        robot.set_wheels_speed(0)
        return ["straight", robot.get_line_sensors()]
    elif 0 not in robot.get_line_sensors():
        turn_robot_closest_90(robot)
        for checks in range(5):
            robot.set_wheels_speed(100)
            robot.sleep(0.01)
            if 0 in robot.get_line_sensors():
                return ["straight", robot.get_line_sensors()]
        return ["stop", robot.get_line_sensors()]
    else:
        return ["straight", robot.get_line_sensors()]


def turn_robot_closest_90(robot: FollowerBot):
    """Turn roomba to the closest 90 degrees."""
    initial_rotation = robot.get_rotation()
    print(initial_rotation)
    print("got here")
    number_of_turns = round(initial_rotation / 90)
    closest_rotation = number_of_turns * 90
    if closest_rotation > initial_rotation:
        while robot.get_rotation() < closest_rotation:
            robot.set_left_wheel_speed(-20)
            robot.set_right_wheel_speed(20)
            robot.sleep(0.01)
    elif closest_rotation < initial_rotation:
        while robot.get_rotation() > closest_rotation:
            robot.set_left_wheel_speed(20)
            robot.set_right_wheel_speed(-20)
            robot.sleep(0.01)
    print(robot.get_rotation())


def turn_robot_around(robot: FollowerBot):
    """Roomba making a 180."""
    if 500 < robot.get_right_line_sensor() < 1024 and 500 < robot.get_left_line_sensor() < 1024:
        initial_rotation = robot.get_rotation()
        current_rotation = initial_rotation
        for i in range(20):
            robot.set_left_wheel_speed(100)
            robot.set_right_wheel_speed(-100)
            robot.sleep(0.02)
            current_rotation = robot.get_rotation()
            rotation_diff = abs(current_rotation - initial_rotation)
            if 175 < rotation_diff < 185:
                break
        print(abs(current_rotation - initial_rotation))
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
        robot.set_wheels_speed(0)
    return


if __name__ == '__main__':
    robo = FollowerBot(start_x=265, start_y=316, track_image="track4.png")
    the_true_follower(robo)
