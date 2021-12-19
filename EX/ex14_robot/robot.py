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


if __name__ == '__main__':
    robo = FollowerBot(start_x=250, start_y=250)
    drive_to_line(robo)
