import unittest
import mock

import game.pig


class TestPig(unittest.TestCase):
    def test_join(self):
        """Players may join a game of Pig"""
        pig = game.pig.Pig('PlayerA', 'PlayerB', 'PlayerC')
        self.assertEqual(pig.get_players(), ('PlayerA', 'PlayerB', 'PlayerC'))

    def test_roll(self):
        """A roll of the die results in an integer between 1 and 6"""
        pig = game.pig.Pig('PlayerA', 'PlayerB')
        for i in range(500):
            r = pig.roll()
        self.assertIsInstance(r, int)
        self.assertTrue(1 <= r <= 6)

    def test_scores(self):
        """Player scores can be retrieved"""
        pig = game.pig.Pig('PlayerA', 'PlayerB', 'PlayerC')
        self.assertEqual(
            pig.get_score(),
            {
                'PlayerA': 0,
                'PlayerB': 0,
                'PlayerC': 0
            }
        )

    def test_get_player_names(self):
        """Players can enter their names"""
        fake_input = mock.Mock(side_effect=['A', 'M', 'Z', ''])
        with mock.patch('__builtin__.input', fake_input):
            names = game.pig.get_player_names()
        self.assertEqual(names, ['A', 'M', 'Z'])

    def test_get_player_names_stdout(self):
        """Check the prompts for player names"""
        with mock.patch('__builtin__.input', side_effect=['A', 'B', '']) as fake:
            game.pig.get_player_names()
        fake.assert_has_calls([
            mock.call("Player 1's name: "),
            mock.call("Player 2's name: "),
            mock.call("Player 3's name: ")
        ])

    @mock.patch('__builtin__.input')
    def test_roll_or_hold(self, fake_input):
        """Player can choose to roll or hold"""
        fake_input.side_effect = ['R', 'H', 'h', 'z', '12345', 'r']
        pig = game.pig.Pig('PlayerA', 'PlayerB')
        self.assertEqual(pig.roll_or_hold(), 'roll')
        self.assertEqual(pig.roll_or_hold(), 'hold')
        self.assertEqual(pig.roll_or_hold(), 'hold')
        self.assertEqual(pig.roll_or_hold(), 'roll')


if __name__ == '__main__':
    unittest.main()
