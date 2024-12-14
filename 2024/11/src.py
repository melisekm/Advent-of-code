from collections import defaultdict
from functools import cache

from utils import aoc_part


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        return list(map(int, f.readline().strip().split()))


def solve(max_blinks):
    data = load_input()
    counts = defaultdict(int)
    for k in data:
        counts[k] += 1
    for blink in range(max_blinks):
        new_counts = defaultdict(int)
        for stone, cnt in counts.items():
            for new_stone in multiply_stones(stone):
                new_counts[new_stone] += cnt
        counts = new_counts
    return sum(counts.values())


@aoc_part(1)
def solve_pt1():
    return solve(25)


@aoc_part(2)
def solve_pt2():
    return solve(75)


@cache
def multiply_stones(stone):
    if stone == 0:
        return 1,
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        l = int(str_stone[:len(str_stone) // 2:])
        r = int(str_stone[len(str_stone) // 2:])
        return l, r

    return stone * 2024,


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
