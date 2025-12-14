from helpers2025 import get_all_integers_from_string
from utils import aoc_part


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        lines = f.read().split("\n\n")
        ranges, items = lines
        ranges = [get_all_integers_from_string(x) for x in ranges.split('\n')]
        items = [int(x.strip()) for x in items.split('\n')]
    return ranges, items


@aoc_part(1)
def solve_pt1():
    ranges, items = load_input()
    ans = 0
    for item in items:
        for r in ranges:
            if r[0] <= item <= r[1]:
                ans += 1
                break

    return ans


def solve(ranges):
    real_ranges = []
    for r in ranges:
        for real_range in list(real_ranges):

            # 10 - 12 vs 16 - 20
            if r[1] < real_range[0]:
                continue

            # 21 - 25 vs 16 - 20
            if r[0] > real_range[1]:
                continue

            # 17-18 vs 16-20
            if real_range[0] <= r[0] <= real_range[1] and real_range[0] <= r[1] <= real_range[1]:
                break

            # 12-18 vs 16-20
            if r[0] <= real_range[0] <= r[1] and (real_range[0] <= r[1] <= real_range[1]):
                real_range[0] = r[0]
                break

            # 18-25 vs 16-20
            if r[0] >= real_range[0] and r[1] > real_range[1]:
                real_range[1] = r[1]
                break

            # 12-25 vs 16 -20
            if r[0] <= real_range[0] and r[1] >= real_range[1]:
                real_range[0] = r[0]
                real_range[1] = r[1]
                break
        else:
            real_ranges.append(r)
    return real_ranges


@aoc_part(2)
def solve_pt2():
    ranges, _ = load_input()
    while True:
        fixed_ranges = solve(ranges)
        if len(fixed_ranges) == len(ranges):
            break
        ranges = fixed_ranges
    ans = 0
    for r in fixed_ranges:
        ans += r[1] - r[0] + 1
    return ans


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
