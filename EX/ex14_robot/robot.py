"""Virtual roomba robot."""
from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(30)
    robot.sleep(5)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    initial_sensors = robot.get_line_sensors()
    if len(initial_sensors) == initial_sensors.count(0):
        while 1024 not in robot.get_line_sensors():
            robot.set_wheels_speed(10)
            robot.sleep(1)
    while 0 not in robot.get_line_sensors():
        robot.set_wheels_speed(25)
        robot.sleep(1)
    robot.set_wheels_speed(0)
    print("on the line")
    robot.done()



def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """


if __name__ == '__main__':
    drive_to_line(FollowerBot())
