import math

from utils import aoc_part
import re


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        return "".join(f.read().split('\n'))


def solve(s):
    return sum(
        math.prod(map(int, re.search(r'(\d+),(\d+)', match).groups()))
        for match in re.findall(r'mul\(\d{1,3},\d{1,3}\)', s)
    )


@aoc_part(1)
def solve_pt1():
    return solve(load_input())


@aoc_part(2)
def solve_pt2():
    return solve(re.sub(r"don't\(\).*?do\(\)", "", load_input()))


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
