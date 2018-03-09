# Adopted from http://www.codekoala.com/pdfs/tdd.pdf

import unittest
import mock
from itertools import cycle

import game.pig

INPUT = mock.Mock()


@mock.patch('__builtin__.input', INPUT)
class TestPig(unittest.TestCase):
    def setUp(self):
        INPUT.reset_mock()

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
        INPUT.side_effect = ['A', 'M', 'Z', '']
        names = game.pig.get_player_names()
        self.assertEqual(names, ['A', 'M', 'Z'])

    def test_get_player_names_stdout(self):
        """Check the prompts for player names"""
        INPUT.side_effect = ['A', 'B', '']
        game.pig.get_player_names()
        INPUT.assert_has_calls([
            mock.call("Player 1's name: "),
            mock.call("Player 2's name: "),
            mock.call("Player 3's name: ")
        ])

    def test_roll_or_hold(self):
        """Player can choose to roll or hold"""
        INPUT.side_effect = ['R', 'H', 'h', 'z', '12345', 'r']
        pig = game.pig.Pig('PlayerA', 'PlayerB')
        self.assertEqual(pig.roll_or_hold(), 'roll')
        self.assertEqual(pig.roll_or_hold(), 'hold')
        self.assertEqual(pig.roll_or_hold(), 'hold')
        self.assertEqual(pig.roll_or_hold(), 'roll')

    @mock.patch('__builtin__.print', mock.Mock())
    def test_gameplay(self):
        """Users may play a game of Pig"""

        INPUT.side_effect = [
            # player names
            'George',
            'Bob',
            '',
            # roll or hold
            'r', 'r',  # George
            'r', 'r', 'r', 'h',  # Bob
            'r', 'r', 'r', 'h',  # George
        ]

        pig = game.pig.Pig(*game.pig.get_player_names())
        pig.roll = mock.Mock(side_effect=[
            6, 6, 1,  # George
            6, 6, 6, 6,  # Bob
            5, 4, 3, 2,  # George
        ])
        self.assertRaises(StopIteration, pig.play)
        self.assertEqual(
            pig.get_score(),
            {
                'George': 14,
                'Bob': 24
            }
        )

    @mock.patch('__builtin__.print')
    def test_winning(self, fake_print):
        """A player wins when they earn 100 points"""

        INPUT.side_effect = [
            # player names
            'George',
            'Bob',
            '',
            # roll or hold
            'r', 'r',  # George
        ]
        pig = game.pig.Pig(*game.pig.get_player_names())
        pig.roll = mock.Mock(side_effect=[2, 2])
        pig.scores['George'] = 97
        pig.scores['Bob'] = 96
        pig.play()
        self.assertEqual(
            pig.get_score(),
            {
                'George': 101,
                'Bob': 96
            }
        )
        fake_print.assert_called_with('George won the game with 101 points!')

    def test_command_line(self):
        """The game can be invoked from the command line"""

        INPUT.side_effect = [
            # player names
            'George',
            'Bob',
            '',
            # roll or hold
            'r', 'r', 'h',  # George
            # Bob immediately rolls a 1
            'r', 'h',  # George
            'r', 'r', 'h'  # Bob
        ]
        with mock.patch('__builtin__.print') as fake_print, \
                mock.patch.object(game.pig.Pig, 'roll') as die:
            die.side_effect = cycle([6, 2, 5, 1, 4, 3])
            self.assertRaises(StopIteration, game.pig.main)
        # check output
        fake_print.assert_has_calls([
            mock.call('Now rolling: George'),
            mock.call('George rolled a 6 and now has 6 points for this turn'),
            mock.call('George rolled a 2 and now has 8 points for this turn'),
            mock.call('George rolled a 5 and now has 13 points for this turn'),
            mock.call('Now rolling: Bob'),
            mock.call('Bob rolled a 1 and lost 0 points'),
            mock.call('Now rolling: George'),
            mock.call('George rolled a 4 and now has 4 points for this turn'),
            mock.call('George rolled a 3 and now has 7 points for this turn'),
            mock.call('Now rolling: Bob'),
            mock.call('Bob rolled a 6 and now has 6 points for this turn'),
            mock.call('Bob rolled a 2 and now has 8 points for this turn'),
            mock.call('Bob rolled a 5 and now has 13 points for this turn')
        ])


if __name__ == '__main__':
    unittest.main()
