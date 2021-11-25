"""Board Games Statistics."""


class Statistics:
    """Gives off statistics about the games played."""

    def __init__(self, filename: str):
        """
        Constructor for Statistics class.
        :param filename: Text file where everything is stored.
        """
        self.stats_dict = self.parse_statistics_file(filename)

    def parse_statistics_file(self, filename: str) -> dict:
        """
        Read a text file and organize it into a dictionary to work with
        :param filename: Text file location
        :return: Dictionary of Games, it's players and results.
        """
        stat_dict = {"games": [], "players": [], "results": [], "result_types": [], "total_number": 0}
        with open(filename) as text_file:
            data = text_file.read()
        different_lines = data.splitlines()
        for line in different_lines:
            stat_dict["total_number"] += 1
            split_line = line.split(";")
            game_name = split_line[0]
            if game_name not in stat_dict["games"]:
                stat_dict["games"].append(game_name)
            result_type = split_line[-2]
            stat_dict["result_types"].append(result_type)
            result = split_line[-1]
            stat_dict["results"].append(result)
            split_line.remove(game_name)
            split_line.remove(result)
            split_line.remove(result_type)
            players = split_line[0].split(",")
            for player in players:
                if player not in stat_dict["players"]:
                    stat_dict["players"].append(player)
        return stat_dict

    def get(self, path: str):
        """Different API methods."""
        if path == "/players":
            return self.get_players()
        elif path == "/games":
            return self.get_games()
        elif path == "/total":
            return self.get_total_games()
        elif "points" in path:
            return self.get_count_game_types_played("points")
        elif "places" in path:
            return self.get_count_game_types_played("places")
        elif "winner" in path:
            return self.get_count_game_types_played("winner")

    def get_players(self) -> list:
        """Return list of players."""
        return self.stats_dict["players"]

    def get_games(self) -> list:
        """Return lis of games played."""
        return self.stats_dict["games"]

    def get_total_games(self) -> int:
        """Return total games played."""
        return self.stats_dict["total_number"]

    def get_count_game_types_played(self, type_of_game: str) -> int:
        """
        Count how many games were played that had specific game type.

        :param type_of_game:
        :return: Integer of how many games were played.
        """
        return self.stats_dict["result_types"].count(type_of_game)


if __name__ == '__main__':
    new_stat = Statistics("games.txt")
    print(new_stat.get("/total/{points}"))
    print(new_stat.get("/total/{places}"))
    print(new_stat.get("/total/{winner}"))
