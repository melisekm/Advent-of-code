import re
from collections import Counter

from utils import aoc_part


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        return [
            list(map(int, re.findall(r"\d+", line)))
            for line in f
        ]


@aoc_part(1)
def solve_pt1():
    data = load_input()
    return sum(
        abs(a - b)
        for a, b in zip(
            sorted(x[0] for x in data), sorted(x[1] for x in data)
        )
    )


@aoc_part(2)
def solve_pt2():
    data = load_input()
    x1 = [x[0] for x in data]
    x2 = Counter([x[1] for x in data])
    return sum(
        a * x2[a] for a in x1
    )


solve_pt1()
solve_pt2()
