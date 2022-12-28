import itertools
from collections import defaultdict
from dataclasses import dataclass

from utils import aoc_part


@dataclass
class Direction:
    name: str
    dir_list: list
    destination: list


class Elf:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.dirs = [
            Direction("N", [(-1, 0), (-1, -1), (-1, 1)], (-1, 0)),
            Direction("S", [(1, 0), (1, -1), (1, 1)], (1, 0)),
            Direction("W", [(0, -1), (-1, -1), (1, -1)], (0, -1)),
            Direction("E", [(0, 1), (-1, 1), (1, 1)], (0, 1)),
        ]

    def propose_move(self, y, x, board):
        i = 0
        for direction in self.dirs:
            for dy, dx in direction.dir_list:
                if (y + dy, x + dx) in board:
                    break
            else:
                return y + direction.destination[0], x + direction.destination[1]
            i += 1

        return None


def load_input(file_name="in.txt"):
    res = {}
    with open(file_name) as f:
        dat = f.read().splitlines()
        for rr in range(len(dat)):
            for cc in range(len(dat[rr])):
                if dat[rr][cc] == "#":
                    res[(rr, cc)] = Elf(rr, cc)
    return res


def is_elf_around_pos(y, x, board):
    for dx, dy in itertools.product([-1, 0, 1], repeat=2):
        move = (y + dy, x + dx)
        if dx == 0 and dy == 0:
            continue
        if move in board:
            return True
    return False


def solve(pt):
    board = load_input()
    rnd = 1
    while True:
        if pt == 1 and rnd > 10:
            return board
        proposed_moves = defaultdict(list)
        for position, elf in board.items():
            if is_elf_around_pos(*position, board):
                move = elf.propose_move(*position, board)
                if move:
                    proposed_moves[move].append(elf)
            first_direction = elf.dirs.pop(0)
            elf.dirs.append(first_direction)
        if not proposed_moves:
            return rnd
        for position, elfs in proposed_moves.items():
            if len(elfs) == 1:
                board[position] = elfs[0]
                del board[(elfs[0].y, elfs[0].x)]
                elfs[0].y, elfs[0].x = position
        rnd += 1


@aoc_part(1)
def solve_pt1():
    board = solve(1)
    # find smallest rectangle around elves
    min_y = min(y for y, x in board)
    max_y = max(y for y, x in board)
    min_x = min(x for y, x in board)
    max_x = max(x for y, x in board)
    # calculate area
    area = (max_y - min_y + 1) * (max_x - min_x + 1)
    # subtract number of elves
    return area - len(board)


@aoc_part(2)
def solve_pt2():
    return solve(2)


solve_pt1()
solve_pt2()
