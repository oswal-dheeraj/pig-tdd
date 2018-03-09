import random

class Pig:
    def __init__(self, *players):
        self.players = players
        self.scores = {}
        for player in self.players:
            self.scores[player] = 0

    def get_players(self):
        """Return a tuple of all the players"""
        return self.players

    def roll(self):
        """Return a number between 1 and 6"""
        return random.randint(1, 6)

    def get_score(self):
        """Return the score for all players"""
        return self.scores
