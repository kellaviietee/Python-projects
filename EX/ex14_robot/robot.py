from FollowerBot import FollowerBot

robot = FollowerBot()


def test_run(robot: FollowerBot):
    robot.set_wheels_speed(30)
    robot.sleep(15)
    robot.set_wheels_speed(0)
    robot.done()


test_run(robot)
