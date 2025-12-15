from helpers2025 import get_all_integers_from_string
from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            if 'x' in line:
                line = line.split(":")
                w_h = get_all_integers_from_string(line[0])
                nums = get_all_integers_from_string(line[1])
                res.append((w_h, nums))
    return res


@aoc_part(1)
def solve_pt1():
    space_per_shape = 9
    return sum(
        w_h[0] * w_h[1] >= sum(x * space_per_shape for x in nums)
        for w_h, nums in load_input()
    )


if __name__ == '__main__':
    solve_pt1()
