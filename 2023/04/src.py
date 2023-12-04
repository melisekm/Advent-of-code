import math
import re
from collections import defaultdict
from functools import lru_cache

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name, encoding='UTF-8') as f:
        for line in f:
            line = line.strip().split(":")[1].split("|")
            res.append(tuple(line))
    return res


@lru_cache(maxsize=None)
def calc(_, card):
    winning = re.findall(r"\d+", card[0])
    got = re.findall(r"\d+", card[1])
    return sum(g in winning for g in got)


@aoc_part(1)
def solve_pt1():
    # calc for all, if calc is 0, then instead of 2^(-1) = 0.5 floor it to 0
    return sum(math.floor(2 ** (calc(0, card) - 1)) for card in load_input())


def card_cnt(idx, data, counts):
    counts[idx + 1] += 1  # get real card id
    winning_cnt = calc(idx, data[idx])  # calculate data for current card
    # start at next card and go until <= winning_cnt
    for i, _ in enumerate(data[idx + 1:idx + winning_cnt + 1], start=idx + 1):
        card_cnt(i, data, counts)  # i == index of card in data


@aoc_part(2)
def solve_pt2():
    data = load_input()
    counts = defaultdict(int)
    for idx in range(len(data)):
        card_cnt(idx, data, counts)
    return sum(counts.values())


solve_pt1()
solve_pt2()
