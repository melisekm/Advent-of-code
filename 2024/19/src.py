from functools import cache

from utils import aoc_part


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        patterns, expected = f.read().split("\n\n")
    return tuple(patterns.split(", ")), expected.split("\n")


@cache
def solve(patterns, design):
    if not design:
        return 1
    total = 0
    for p in patterns:
        if design.startswith(p):
            total += solve(patterns, design[len(p):])
    return total


@aoc_part(1)
def solve_pt1():
    patterns, expected = load_input()
    return sum(
        1 for design in expected if solve(patterns, design)
    )


@aoc_part(2)
def solve_pt2():
    patterns, expected = load_input()
    return sum(
        solve(patterns, design) for design in expected
    )


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
