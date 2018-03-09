import unittest

import game.pig


class TestPig(unittest.TestCase):
    def test_join(self):
        """Players may join a game of Pig"""
        pig = game.pig.Pig('PlayerA', 'PlayerB', 'PlayerC')
        self.assertEqual(pig.get_players(), ('PlayerA', 'PlayerB', 'PlayerC'))


if __name__ == '__main__':
    unittest.main()
