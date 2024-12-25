from collections import Counter

import numpy as np

from utils import aoc_part


def load_input(file_name="in.txt"):
    locks, keys = [], []
    with open(file_name) as f:
        for symbols in f.read().split("\n\n"):
            lines = symbols.split("\n")
            (locks if all(x == '#' for x in lines[0]) else keys).append(
                [list(x) for x in lines]
            )
    return locks, keys


def count(data, start=None, end=None):
    return [
        [Counter(line)['#'] for line in np.array(el[start:end]).T]
        for el in data
    ]


@aoc_part(1)
def solve_pt1():
    locks, keys = load_input()
    lock_nums = count(locks, start=1)
    key_nums = count(keys, end=-1)

    return sum(
        all(x <= 5 for x in (sum(s) for s in zip(num_lock, num_key)))
        for num_lock in lock_nums
        for num_key in key_nums
    )


if __name__ == '__main__':
    solve_pt1()
