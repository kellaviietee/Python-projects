from FollowerBot import FollowerBot

robo = FollowerBot()


def test_run(robot: FollowerBot):
    robot.set_wheels_speed(30)
    robot.sleep(10)
    robot.set_wheels_speed(0)
    robot.done()


test_run(robo)
