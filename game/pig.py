class Pig:
    def __init__(self, *players):
        self.players = players

    def get_players(self):
        """Return a tuple of all the players"""
        return self.players

    def roll(self):
        """Return a number between 1 and 6"""
        pass
