class MazeSolver:
    def __init__(self, maze_str: str, configuration: dict = None):
        """
        Initialize the solver with map string and configuration.
        Map string can consist of several lines, line break separates the lines.
        Empty lines in the beginning and in the end should be ignored.
        Line can also consist of spaces, so the lines cannot be stripped.

        On the left and right sides there can be several doors (marked with "|").
        Solving the maze starts from a door from the left side and ends at the door on the right side.
        See more @solve().

        Configuration is a dict which indicates which symbols in the map string have what cost.
        Doors (|) are not shown in the configuration and are not used inside the maze.
        Door cell cost is 0.
        When a symbol on the map string is not in configuration, its cost is 0.
        Cells with negative cost cannot be moved on/through.

        Default configuration:
        configuration = {
            ' ': 1,
            '#': -1,
            '.': 2,
            '-': 5,
            'w': 10
        }

        :param maze_str: Map string
        :param configuration: Optional dictionary of symbol costs.
        """
        self.map_str = maze_str

        if configuration is None:
            configuration = {
                ' ': 1,
                '#': -1,
                '.': 2,
                '-': 5,
                'w': 10
            }
        pass

    def get_shortest_path(self, start: tuple, goal: tuple) -> tuple:
        """
        Return shortest path and the total cost of it.

        The shortest path is the path which has the lowest cost.
        Start and end are tuples of (y, x) where the first (upper) line is y = 0.
        The path should include both the start and the end.

        If there is no path from the start to goal, the path is None and cost is -1.

        If there are several paths with the same lowest cost, return any of those.

        :param start: Starting cell (y, x)
        :param goal: Goal cell (y, x)
        :return: shortest_path, cost
        """
        return [(0, 0), (0, 1)], 2

    def solve(self) -> tuple:
        """
        Solve the given maze and return the path and the cost.

        Finds the shortest path from one of the doors on the left side to the one of the doors on the right side.
        Shortest path is the one with the lowest cost.

        This method should use get_shortest_path method and return the same values.
        If there are several paths with the same cost, return any of those.

        :return: shortest_path, cost
        """
        print(self.map_str)
        map_list = list(self.map_str)
        all_change_indices = []
        for char in range(0,len(map_list)):
            if map_list[char] == "\n":
                all_change_indices.append(char)
        print(map_list[all_change_indices[0] + 1:all_change_indices[1]])
        return [(0, 0), (0, 1)], 2

    def locate(self, area: str, x: int, y: int, unknown: str = None) -> tuple:
        """
        Locate yourself in a already known maze.

        Note that (0, 0) is top left corner

        :param area: area you know around you.
        :param x: x-coord relative to known area
        :param y: y-coord relative to known area
        :param unknown: single char that represents unknown squares in area param

        :return list of tuple(y, x) with coordinates of your location in big/known maze (all possible locations)
        """


if __name__ == '__main__':
    maze = """
########
#      #
#      #
|      |
########
"""
    solver = MazeSolver(maze)
    solver.solve()