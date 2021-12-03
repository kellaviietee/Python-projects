"""Virtual roomba robot."""
from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """See if the robot even moves at all."""
    robot.set_wheels_speed(30)
    robot.sleep(10)
    robot.set_wheels_speed(0)
    robot.done()
