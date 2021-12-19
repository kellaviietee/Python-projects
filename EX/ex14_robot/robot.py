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
    while robot.get_line_sensors() == [1024, 1024, 1024, 1024, 1024, 1024]:
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
        robot.set_wheels_speed(0)
    while 0 in robot.get_line_sensors():
        if robot.get_left_line_sensor() == 0 and robot.get_right_line_sensor() == 0:
            print(robot.get_line_sensors())
            robot.set_wheels_speed(100)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
        elif robot.get_left_line_sensor() == 1024 and robot.get_right_line_sensor() == 0:
            robot.set_left_wheel_speed(-100)
            robot.set_right_wheel_speed(100)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            print(robot.get_left_line_sensor())
            print(robot.get_right_line_sensor())
        elif robot.get_left_line_sensor() == 0 and robot.get_right_line_sensor() == 1024:
            robot.set_right_wheel_speed(-100)
            robot.set_left_wheel_speed(100)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
            print(robot.get_left_line_sensor())
            print(robot.get_right_line_sensor())
        else:
            break
    print(robot.get_left_line_sensor())
    print(robot.get_right_line_sensor())
    robot.done()


if __name__ == '__main__':
    robo = FollowerBot(start_x=380, start_y=255)
    follow_the_line(robo)
