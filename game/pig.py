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

    def roll_or_hold(self):
        """Return 'roll' or 'hold' based on user input"""
        action = ''
        while True:
            value = input('(R)oll or (H)old? ')
            if value.lower() == 'r':
                action = 'roll'
                break
            elif value.lower() == 'h':
                action = 'hold'
                break
        return action


def get_player_names():
    """Prompt for player names"""
    names = []
    while True:
        value = input("Player {}'s name: ".format(len(names)+1))
        if not value:
            break
        names.append(value)
    return names
