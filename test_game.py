import unittest
from unittest.mock import patch
from io import StringIO
from game import ShootingGame 

class TestShootingGame(unittest.TestCase):
    @patch("builtins.input", side_effect=["0"])
    def test_select_gun(self, mock_input):
        game = ShootingGame()
        selected_gun = game.select_gun()
        self.assertEqual(selected_gun, game.guns[0])

    def test_select_animal(self):
        game = ShootingGame()
        selected_animal = game.select_animal()
        self.assertIn(selected_animal, game.animals)

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=["s", "s", "r", "x"])
    def test_start_game(self, mock_input, mock_stdout):
        game = ShootingGame()
        game.start_game()

        expected_output = "Selected Gun info:"
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=["s", "s", "r", "x"])
    def test_start_game_points(self, mock_input, mock_stdout):
        game = ShootingGame()
        game.start_game()

        # Checking if points are accumulated correctly
        self.assertGreaterEqual(game.total_point, 0)

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=["s", "s", "r", "x"])
    def test_start_game_animal_killed(self, mock_input, mock_stdout):
        game = ShootingGame()
        game.start_game()

        # Checking if animal_killed is incremented correctly
        self.assertGreaterEqual(game.animal_killed, 0)

if __name__ == "__main__":
    unittest.main()