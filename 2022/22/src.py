import re

from utils import aoc_part

movement_map = {
    '>': {
        "R": (1, 0, 'v'),
        "L": (-1, 0, '^'),
    },
    '<': {
        "R": (-1, 0, '^'),
        "L": (1, 0, 'v')
    },
    '^': {
        "R": (0, 1, '>'),
        "L": (0, -1, '<')
    },
    'v': {
        "R": (0, -1, '<'),
        "L": (0, 1, '>')
    }
}

facing_score_map = {
    '>': 0,
    'v': 1,
    '<': 2,
    '^': 3
}


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        board, directions = f.read().split("\n\n")
        board = [list(row) for row in board.split("\n")]
        max_board_len = max([len(row) for row in board])
        res = [[' '] * max_board_len for _ in board]
        start_pos = None
        for i in range(len(board)):
            for j in range(len(board[i])):
                if start_pos is None and board[i][j] == '.':
                    start_pos = (i, j)
                if board[i][j] == ' ':
                    continue
                res[i][j] = board[i][j]
        # get numbers from directions re
        directions_numbers = list(map(int, re.findall(r'\d+', directions)))
        directions_tuples = []
        direction_idx = 0
        for char in range(len(directions)):
            if directions[char].isalpha():
                directions_tuples.append((int(directions_numbers[direction_idx]), directions[char]))
                direction_idx += 1
        directions_tuples.append((int(directions_numbers[direction_idx]), 'S'))
        return res, directions_tuples, start_pos


@aoc_part(1)
def solve_pt1():
    board, directions, start_pos = load_input()
    human_i, human_j = start_pos
    current_direction = (0, 1, '>')
    for steps, direction in directions:
        i_sign, j_sign, next_orientation = current_direction
        break_movement = False
        for step in range(steps):
            try:
                next_step = board[human_i + i_sign][human_j + j_sign]
                if next_step == ' ':
                    raise IndexError
                if next_step == '#':  # its a wall where i am moving
                    break
                elif next_step == '.':
                    human_i += i_sign
                    human_j += j_sign
            except IndexError:
                # save position
                saved_i, saved_j = human_i, human_j
                # we will be teleporting to the other side in way of the direction we are moving
                if i_sign == 1:
                    human_i = 0
                elif i_sign == -1:
                    human_i = len(board) - 1
                elif j_sign == 1:
                    human_j = 0
                elif j_sign == -1:
                    human_j = len(board[0]) - 1
                # now keep moving until we hit a '.' or '#'
                if board[human_i][human_j] == '#':
                    human_i = saved_i
                    human_j = saved_j
                    break
                if board[human_i][human_j] == '.':
                    continue
                while True:
                    next_step = board[human_i + i_sign][human_j + j_sign]
                    if next_step == '.':
                        human_i += i_sign
                        human_j += j_sign
                        break
                    elif next_step == '#':
                        human_i, human_j = saved_i, saved_j
                        break_movement = True
                        break
                    human_i += i_sign
                    human_j += j_sign
                if break_movement:
                    break
        if direction == 'S':
            break
        current_direction = movement_map[next_orientation][direction]
    return 1000 * (human_i + 1) + 4 * (human_j + 1) + facing_score_map[current_direction[2]]


@aoc_part(2)
def solve_pt2():
    raise NotImplementedError


solve_pt1()
# solve_pt2()
