import copy
from itertools import cycle

from utils import aoc_part

init = """
#########
"""
new_space = """
#.......#
"""
first = """
#..@@@@.#
"""
second = """
#...@...#
#..@@@..#
#...@...#
"""
third = """
#....@..#
#....@..#
#..@@@..#
"""
fourth = """
#..@....#
#..@....#
#..@....#
#..@....#
"""
fifth = """
#..@@...#
#..@@...#
"""


def convert_str_to_2d(obj):
    return [list(line) for line in obj.strip().splitlines()]


new_space = convert_str_to_2d(new_space)


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        return f.read().strip()


def insert_new_shape(game, shape):
    for L in reversed(shape):
        game.insert(0, copy.deepcopy(L))


def insert_empty_space(game):
    for i in range(3):
        insert_new_shape(game, new_space)


def do_movement(orig_game, dy, dx):
    game = copy.deepcopy(orig_game)
    tmp = copy.deepcopy(game)
    # go from bottom to top
    for i in range(len(game) - 1, -1, -1):
        # decide from which side we move
        if dx == 1:
            xrange = range(len(game[i]) - 1, -1, -1)
        else:
            xrange = range(len(game[i]))

        for j in xrange:
            if game[i][j] != "@":
                continue
            if game[i + dy][j + dx] == "#":  # collision
                return orig_game, False
            tmp[i][j] = "."  # remove from old position
            tmp[i + dy][j + dx] = "@"  # add to new position
    return tmp, True


def movement(game, dy, dx):
    game, res = do_movement(game, dy, dx)
    if res:
        return True, game
    # cant move to sides
    if dy == 0:
        # we werent moving down
        return False, game
    # we are on the bottom, change all @ to #
    for i in range(len(game)):
        for j in range(len(game[i])):
            if game[i][j] == "@":
                game[i][j] = "#"

    # Find max Y, its the first row with # and 7 . in it #
    for i in range(len(game) - 1, -1, -1):
        if game[i].count(".") == 7:
            # delete everything that is above
            return False, game[i + 1:]


def play_game(game, shape, movements):
    insert_empty_space(game)
    insert_new_shape(game, shape)
    while True:
        dx = 1 if next(movements) == ">" else -1
        _, game = movement(game, 0, dx)
        res, game = movement(game, 1, 0)
        if not res:
            return game


@aoc_part(1)
def solve_pt1():
    data = load_input()
    game = convert_str_to_2d(init)
    shapes = cycle([convert_str_to_2d(shape) for shape in [first, second, third, fourth, fifth]])
    movements = cycle(data)
    for idx in range(2022):
        game = play_game(game, next(shapes), movements)
        if idx % 100 == 0:
            print(f"shape_id={idx}, game_size={len(game)}")

    return len(game) - 1


@aoc_part(2)
def solve_pt2():
    # Find Pattern from Part 1 and input numbers. It shows up after 2173 steps. 3873 to confirm.
    # To find it look for highest number of shape changes during one game. It was 80.
    to_find = 1_000_000_000_000
    first_shape, first_game = 473, 756
    shape_increase, game_increase = 1700, 2642
    second_game = first_game + game_increase

    multiplier = to_find // shape_increase + 1
    game_size_in_nearest_higher = first_game + game_increase * multiplier

    to_find_delta_shape = to_find % shape_increase  # 200
    to_find_delta_game = 323
    # shape_id =  200, game =  323
    # shape_id = 2173, game = 3398
    diff = second_game - to_find_delta_game
    to_find = game_size_in_nearest_higher - diff - 1
    return to_find


solve_pt1()
solve_pt2()
