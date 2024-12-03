import copy
import re

from utils import aoc_part


def solve(LN):
    prev = LN[0]
    for curr in LN[1:]:
        if not (3 >= abs(curr - prev) >= 1):
            return False
        prev = curr
    # no diff more than 1-3 and sorted, then safe
    x = sorted(LN)
    return LN == x or LN == list(reversed(x))


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        return [
            list(map(int, re.findall(r"\d+", line.strip())))
            for line in f
        ]


@aoc_part(1)
def solve_pt1():
    return sum(solve(line) for line in load_input())


@aoc_part(2)
def solve_pt2():
    data = load_input()
    res = 0
    for orig_data in data:
        tmp = solve(orig_data)
        if tmp:
            res += tmp
            continue
        for idx_to_remove in range(len(orig_data)):
            new_data = copy.deepcopy(orig_data)
            new_data.pop(idx_to_remove)
            tmp = solve(new_data)
            if tmp:
                res += 1
                break

    return res


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
