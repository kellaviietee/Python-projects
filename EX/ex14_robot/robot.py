from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    robot.set_wheels_speed(30)
    robot.sleep(15)
    robot.set_wheels_speed(0)
    robot.done()


if __name__ == '__main__':
    robo = FollowerBot()
    test_run(robo)
