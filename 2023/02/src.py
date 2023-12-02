import re
from collections import defaultdict
from functools import reduce

from utils import aoc_part


def load_input(file_name="in.txt"):
    games_list = []
    with open(file_name, encoding='UTF-8') as f:
        for line in f:
            line_split = line.split(":")
            games_list.append([games_set.split(",") for games_set in line_split[1].split(";")])

    parsed_games = []
    for game in games_list:
        parsed_game = []
        for game_set in game:
            parsed_g = []
            for game_subset in game_set:
                number = int(re.search(r"\d+", game_subset).group())
                word = re.search(r"[a-z]+", game_subset).group()
                parsed_g.append((number, word))
            parsed_game.append(parsed_g)
        parsed_games.append(parsed_game)

    return parsed_games


def possible(game, max_available):
    for game_set in game:
        for game_subset in game_set:
            number, color = game_subset
            if number > max_available[color]:
                return False
    return True


@aoc_part(1)
def solve_pt1():
    parsed_games = load_input()
    max_available = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    games_possible = 0
    for game_id, game in enumerate(parsed_games, start=1):
        if possible(game, max_available):
            games_possible += game_id

    return games_possible


@aoc_part(2)
def solve_pt2():
    parsed_games = load_input()
    res = 0
    for game_id, game in enumerate(parsed_games):
        maxes = defaultdict(int)
        for game_set in game:
            for game_subset in game_set:
                number, color = game_subset
                maxes[color] = max(maxes[color], number)
        res += reduce(lambda x, y: x * y, maxes.values())
    return res


solve_pt1()
solve_pt2()
