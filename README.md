# Engagement-Based Horror Game Ranking Algorithm for Yanah

## Overview

My project is focused on implementing an engagement-based ranking algorithm for horror games on the Yanah platform.

Instead of ranking games solely by popularity or by being relatively new, the new algorithm considers multiple engagement metrics to better represent overall player satisfaction.

The metrics I am using are:

- Total Plays (25%)
- Unique Sessions (25%)
- Finish Rate (30%)
- Average Rating (10%)
- Average Session Time (10%)

Each game would then receive a weighted engagement score, and games are sorted from highest score to lowest score.

---

## Algorithm

The algorithm mainly performs two steps:

1. It firstly Calculates a weighted engagement score for every game.
2. Then it sorts all games in descending order according to the calculated score.

Overall Time Complexity:

O(n log n)

Overall Space Complexity:

O(n)

---

## Project Structure

```
main.py
game_ranking.py
test_game_ranking.py
sample_data.json
requirements.txt
```

---

## Running the Program

```
python main.py
```

---

## Running Tests

```
python -m unittest test_game_ranking.py
```

---

## Sample Output

```
Don't Leave Me Here 31.0
Test Game A 35.0
Test Game B 29.0
```

---

## Author

Jai Sharma

CS 460 Algorithms Final Project

GitHub:
https://github.com/jaidarkknight1/Engagement-Based-Horror-Game-Ranking-Algorithm-for-Yanah
