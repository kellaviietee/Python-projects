from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    robot.set_wheels_speed(30)
    robot.sleep(5)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
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
    initial_drive_to_the_line(robot)
    drive_along_the_path(robot)
    print(robot.get_line_sensors())
    robot.done()


def the_true_follower(robot: FollowerBot):
    initial_drive_to_the_line(robot)
    drive_along_the_path(robot)
    print(robot.get_line_sensors())
    robot.done()


def initial_drive_to_the_line(robot: FollowerBot):
    while robot.get_line_sensors() == [1024, 1024, 1024, 1024, 1024, 1024]:
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
        robot.set_wheels_speed(0)
    return


def drive_along_the_path(robot: FollowerBot):
    left_on_line = robot.get_left_line_sensors().count(0)
    right_on_line = robot.get_right_line_sensors().count(0)
    while 0 in robot.get_line_sensors() or robot.get_line_sensors() == [1024, 1024, 1024, 1024, 1024, 1024]:
        if robot.get_line_sensors() == [1024, 1024, 1024, 1024, 1024, 1024]:
            print("got here")
            robot.set_wheels_speed(90)
            robot.sleep(0.1)
            robot.set_wheels_speed(0)
            if 0 in robot.get_line_sensors():
                continue
            else:
                break
        elif left_on_line == right_on_line:
            robot.set_wheels_speed(100)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            left_on_line = robot.get_left_line_sensors().count(0)
            right_on_line = robot.get_right_line_sensors().count(0)
        elif left_on_line == right_on_line + 1:
            print("this triggers")
            robot.set_left_wheel_speed(100)
            robot.set_right_wheel_speed(30)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            left_on_line = robot.get_left_line_sensors().count(0)
            right_on_line = robot.get_right_line_sensors().count(0)
        elif left_on_line == right_on_line - 1:
            print("this triggers 2")
            robot.set_left_wheel_speed(30)
            robot.set_right_wheel_speed(100)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            left_on_line = robot.get_left_line_sensors().count(0)
            right_on_line = robot.get_right_line_sensors().count(0)
        elif left_on_line == right_on_line + 2:
            print("this triggers 3")
            robot.set_left_wheel_speed(80)
            robot.set_right_wheel_speed(-80)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            left_on_line = robot.get_left_line_sensors().count(0)
            right_on_line = robot.get_right_line_sensors().count(0)
        elif left_on_line == right_on_line - 2:
            print("this triggers 4")
            robot.set_left_wheel_speed(-80)
            robot.set_right_wheel_speed(80)
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
    return


def turn_robot_around(robot: FollowerBot):
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
