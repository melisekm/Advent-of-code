import math
import re
from functools import lru_cache

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name, encoding='UTF-8') as f:
        for line in f:
            winning, got = line.strip().split(":")[1].split("|")
            res.append(sum(g in re.findall(r"\d+", winning) for g in re.findall(r"\d+", got)))
    return res


data = load_input()


@aoc_part(1)
def solve_pt1():
    return sum(math.floor(2 ** (card - 1)) for card in data)


@lru_cache(maxsize=None)
def card_cnt(idx):
    return 1 + sum(card_cnt(i) for i in range(idx + 1, idx + 1 + data[idx]))


@aoc_part(2)
def solve_pt2():
    return sum(card_cnt(idx) for idx in range(len(data)))


solve_pt1()
solve_pt2()
