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
        return favourite_game.name

    def add_games(self, game_name: "Game"):
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
                new_player.add_games(new_game)
                if new_player not in stat_dict["players"]:
                    stat_dict["players"].append(new_player)
                elif new_player in stat_dict["players"]:
                    current_players = stat_dict["players"]
                    for existing_player in current_players:
                        if existing_player.name == player:
                            existing_player.add_games(new_game)
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
        elif "/players/" in path:
            return self.get_info_about_players(path)

    def get_info_about_players(self, path: str):
        """Get info about players."""
        name_and_info = path.replace("/players/", "").split("/")
        player_name = name_and_info[0]
        if player_name not in self.get_players():
            return None
        request = name_and_info[1]
        all_players = self.stats_dict["players"]
        for player in all_players:
            if player.name == player_name:
                if request == "amount":
                    return player.total_games_played()
                if request == "favourite":
                    return player.favourite_game()

    def get_players(self) -> list:
        """Return list of players."""
        all_players = self.stats_dict["players"]
        all_player_names = []
        for player in all_players:
            all_player_names.append(player.name)
        return all_player_names

    def get_games(self) -> list:
        """Return lis of games played."""
        all_games = self.stats_dict["games"]
        all_game_names = []
        for game in all_games:
            all_game_names.append(game.name)
        return all_game_names

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
    print(new_stat.get("/players/joosep/amount"))
    print(new_stat.get("/players/joosep/favourite"))
