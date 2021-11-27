"""Board Games Statistics."""


class Player:
    """Player statistics."""

    def __init__(self, name: str):
        """Initialize Player instant."""
        self.name = name
        self.games_played = []
        self.won_games = 0

    def __repr__(self):
        """How is the Player represented."""
        return self.name

    def __eq__(self, other):
        """When are two players considered the same."""
        return self.name == other.name

    def total_games_played(self) -> int:
        """How many games has the player played."""
        return len(self.games_played)

    def favourite_game(self) -> str:
        """Most played game of the player."""
        favourite_game = None
        for game in self.games_played:
            if favourite_game is None:
                favourite_game = game
            else:
                if self.games_played.count(favourite_game) < self.games_played.count(game):
                    favourite_game = game
        return favourite_game

    def add_games(self, game_name: str):
        """Add a game to the list of played games."""
        self.games_played.append(game_name)


class Game:
    """Game statistics"""

    def __init__(self, name: str, game_type: str):
        """Initialize Game instant."""
        self.name = name
        self.game_type = game_type
        self.amount_played = 1
        self.player_counts = []
        self.winners = []
        self.losers = []
        self.players = {}
        self.record_holder = None

    def __repr__(self):
        """How is the Game represented."""
        return self.name

    def __eq__(self, other):
        """When are two games the same."""
        return self.name == other.name

    def update_amount_played(self):
        """Update number of times the game has been played"""
        self.amount_played += 1

    def add_player_count(self, player_count: int):
        """How many players played the game"""
        self.player_counts.append(player_count)

    def most_frequent_player_count(self) -> int:
        """How many players usually play this game."""
        most_frequent_count = None
        for count in self.player_counts:
            if most_frequent_count is None:
                most_frequent_count = count
            else:
                most_frequent_count = max(self.player_counts.count(most_frequent_count),
                                          self.player_counts.count(count))
        return most_frequent_count

    def most_wins(self) -> str:
        """Who has the most wins in this game."""
        most_wins = None
        for player in self.winners:
            if most_wins is None:
                most_wins = player
            else:
                if self.winners.count(most_wins) < self.winners.count(player):
                    most_wins = player
        return most_wins

    def add_player(self, player: Player):
        """Add a player to Game dictionary to see how many_times player has played the game."""
        if player in self.players:
            self.players[player] += 1
        else:
            self.players[player] = 1

    def most_frequent_winner(self) -> str:
        """Find who has the best winning percentage."""
        most_frequent_winner = None
        for player in self.players:
            if player in self.winners:
                if most_frequent_winner is None:
                    most_frequent_winner = player
                else:
                    most_freq_percentage = self.winners.count(most_frequent_winner) / self.players[most_frequent_winner]
                    player_percentage = self.winners.count(player) / self.players[player]
                    if player_percentage > most_freq_percentage:
                        most_frequent_winner = player
        return most_frequent_winner.name

    def most_losses(self) -> str:
        """Find who has lost the most games."""
        most_losses = None
        for player in self.losers:
            if most_losses is None:
                most_losses = player
            else:
                if self.losers.count(most_losses) < self.losers.count(player):
                    most_losses = player
        return most_losses.name

    def most_frequent_loser(self) -> str:
        """Find the most frequent loser."""
        most_frequent_loser = None
        for player in self.players:
            if player in self.losers:
                if most_frequent_loser is None:
                    most_frequent_loser = player
                else:
                    most_loser_percentage = self.losers.count(most_frequent_loser) / self.players[most_frequent_loser]
                    player_percentage = self.losers.count(player) / self.players[player]
                    if player_percentage > most_loser_percentage:
                        most_frequent_loser = player
        return most_frequent_loser.name

    def record_holder(self, contender: [list]):
        """Update games record holder."""
        if self.game_type == "points" and self.record_holder is None:
            self.record_holder = contender
        elif self.game_type == "points":
            if contender[1] > self.record_holder[1]:
                self.record_holder = contender

    def get_record_holder(self) -> str:
        """Return record holder of this game."""
        if self.game_type == "points":
            return self.record_holder[0]


class Statistics:
    """Gives off statistics about the games played."""

    def __init__(self, filename: str):
        """
        Constructor for Statistics class.
        :param filename: Text file where everything is stored.
        """
        self.stats_dict = self.parse_statistics_file(filename)
        self.players = None

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
            result_type = split_line[2]
            stat_dict["result_types"].append(result_type)
            new_game = Game(game_name, result_type)
            if new_game not in stat_dict["games"]:
                stat_dict["games"].append(new_game)
            players = split_line[1].split(",")
            for player in players:
                new_player = Player(player)
                if new_player not in stat_dict["players"]:
                    stat_dict["players"].append(new_player)

            result = split_line[3]
            stat_dict["results"].append(result)
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
    print(new_stat.stats_dict)
