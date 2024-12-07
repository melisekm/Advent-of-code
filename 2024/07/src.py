import copy
import itertools
import operator
import re

from tqdm import tqdm

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            main, nums = line.strip().split(":")
            nums = re.findall(r"\d+", nums)
            res.append((int(main), list(map(int, nums))))
    return res


def solve(p2=False):
    data = load_input()
    res = 0
    for main, nums in tqdm(data):
        total_combs = len(nums) - 1
        options = [operator.mul, operator.add] + (["||"] if p2 else [])
        options2 = list(itertools.product(options, repeat=total_combs))
        for j in options2:
            nm_cpy = nums.copy()
            for op in j:
                first = int(nm_cpy.pop(0))
                second = int(nm_cpy.pop(0))

                if op == "||":
                    new_first = int(str(first) + str(second))
                else:
                    new_first = op(first, second)
                nm_cpy.insert(0, new_first)
            if main == nm_cpy[0]:
                res += main
                break

    return res


@aoc_part(1)
def solve_pt1():
    return solve()


@aoc_part(2)
def solve_pt2():
    return solve(p2=True)


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
