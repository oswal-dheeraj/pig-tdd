import random


class Pig:
    def __init__(self, *players):
        self.players = players
        self.scores = dict.fromkeys(self.players, 0)

    def get_players(self):
        """Return a tuple of all the players"""
        return self.players

    def roll(self):
        """Return a number between 1 and 6"""
        return random.randint(1, 6)

    def get_score(self):
        """Return the score for all players"""
        return self.scores


def get_player_names():
    """Prompt for player names"""
    names = []
    while True:
        value = input("Player {}'s name: ".format(len(names)+1))
        if not value:
            break
        names.append(value)
    return names
