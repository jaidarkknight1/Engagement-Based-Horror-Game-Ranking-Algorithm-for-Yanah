import unittest

from main import GameAnalytics, calculate_game_score, rank_games


class TestGameRanking(unittest.TestCase):

    def test_score_calculation(self):
        game = GameAnalytics("Test Game", 100, 50, 50)

        expected_score = (100 * 0.25) + (50 * 0.25) + (50 * 0.30)

        self.assertEqual(calculate_game_score(game), expected_score)

    def test_higher_finish_rate_ranks_first(self):
        game_a = GameAnalytics("High Finish Rate", 50, 20, 80)
        game_b = GameAnalytics("Low Finish Rate", 50, 20, 20)

        ranked_games = rank_games([game_b, game_a])

        self.assertEqual(ranked_games[0].title, "High Finish Rate")

    def test_sorting_highest_score_first(self):
        game_a = GameAnalytics("Low Score Game", 10, 10, 10)
        game_b = GameAnalytics("High Score Game", 100, 100, 100)

        ranked_games = rank_games([game_a, game_b])

        self.assertEqual(ranked_games[0].title, "High Score Game")


if __name__ == "__main__":
    unittest.main()
