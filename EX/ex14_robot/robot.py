from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    robot.set_wheels_speed(30)
    robot.sleep(3)
    robot.set_wheels_speed(0)
    robot.done()
