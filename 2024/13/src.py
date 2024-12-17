import re
import numpy as np
from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        games = f.read().split("\n\n")
        for game in games:
            game_line = []
            for line in game.split('\n'):
                nums = list(map(int, re.findall(r"\d+", line)))
                game_line.extend(nums)
            res.append(game_line)
    return res



def solve(a, c, b, d, e, f, p2=False):
    r1 = np.array([[a, b], [c, d]])
    r2 = np.array([e, f]) + (10000000000000 if p2 else 0)
    o1, o2 = np.linalg.solve(r1, r2).round()

    if ([o1 * a + o2 * b, o1 * c + o2 * d] == r2).all():
        return o1 * 3 + o2
    return 0


@aoc_part(1)
def solve_pt1():
    return sum(solve(*game) for game in load_input())


@aoc_part(2)
def solve_pt2():
    return sum(solve(*game, p2=True) for game in load_input())

if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
