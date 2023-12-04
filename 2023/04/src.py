from collections import defaultdict
from functools import lru_cache

from utils import aoc_part
import re


def load_input(file_name="in.txt"):
    res = []
    with open(file_name, encoding='UTF-8') as f:
        for line in f:
            line = line.strip().split(":")[1].split("|")
            res.append(line)
    return res


@aoc_part(1)
def solve_pt1():
    data = load_input()
    res = 0
    for card in data:
        winning = re.findall(r"\d+", card[0])
        got = re.findall(r"\d+", card[1])
        wining_cnt = 0
        for g in got:
            if g in winning:
                wining_cnt += 1
        if wining_cnt:
            res += (2 ** (wining_cnt - 1))

    return res


@lru_cache(maxsize=None)
def calc(card_id, card):
    winning = re.findall(r"\d+", card[0])
    got = re.findall(r"\d+", card[1])
    wining_cnt = 0
    for g in got:
        if g in winning:
            wining_cnt += 1
    return wining_cnt


def card_cnt(idx, data, counts):
    card_id = idx + 1
    card = data[idx]
    counts[card_id] += 1
    wining_cnt = calc(idx, tuple(card))
    for i, card in enumerate(data[idx + 1:idx + wining_cnt + 1], start=idx + 1):
        card_cnt(i, data, counts)


@aoc_part(2)
def solve_pt2():
    data = load_input()
    counts = defaultdict(int)
    for idx in range(len(data)):
        card_cnt(idx, data, counts)
    return sum(counts.values())


# solve_pt1()
solve_pt2()
