# this is the class that stores analytics data for a single game
class GameAnalytics:
    def __init__(
        self,
        title,
        total_plays,
        unique_sessions,
        finish_rate,
        avg_rating=0,
        avg_session_time=0,
    ):
        # this will store all engagement metrics for the game
        self.title = title
        self.total_plays = total_plays
        self.unique_sessions = unique_sessions
        self.finish_rate = finish_rate
        self.avg_rating = avg_rating
        self.avg_session_time = avg_session_time


# this will be used to Calculate the weighted engagement score for a game
def calculate_game_score(game):

    play_score = game.total_plays * 0.25

    session_score = game.unique_sessions * 0.25

    # 30% weight for finish rate this is our most important metric
    finish_score = game.finish_rate * 0.30

    rating_score = game.avg_rating * 0.10

    time_score = game.avg_session_time * 0.10

    # this is the Finalized weighted engagement score
    final_score = (
        play_score
        + session_score
        + finish_score
        + rating_score
        + time_score
    )

    return final_score


# this function will Rank all our games from highest score to lowest score
def rank_games(games):

    # now we sort games in descenfign order
    return sorted(games, key=calculate_game_score, reverse=True)


# data we use
games = [
    GameAnalytics("Don't Leave Me Here", 56, 38, 29),
    GameAnalytics("Test Game A", 25, 20, 80),
    GameAnalytics("Test Game B", 70, 30, 15),
]

# this will helpo us generate the ranked list of games
ranked_games = rank_games(games)

# Now we will display each game's score
for game in ranked_games:
    print(game.title, calculate_game_score(game))
