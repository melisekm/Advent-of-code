from collections import defaultdict
from functools import reduce

from helpers2025 import get_all_integers_from_string
from utils import aoc_part


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        lines = f.read().splitlines()
        signs = lines[-1]
        numbers = lines[:-1]
        parsed_nums = defaultdict(list)
        for line in numbers:
            nums = get_all_integers_from_string(line)
            for idx, n in enumerate(nums):
                parsed_nums[idx].append(n)
    return list(parsed_nums.values()), signs.split()


@aoc_part(1)
def solve_pt1():
    return sum(calc(nums, sign) for nums, sign in zip(*load_input()))


def load_input2(file_name="in.txt"):
    with open(file_name) as f:
        lines = f.read().splitlines()
        for i in range(len(lines)):
            lines[i] += ' '  # pycharm removes trailing ' ' when saving file
        signs = lines[-1]
        numbers = lines[:-1]
        graph = defaultdict(list)
        for c in range(len(numbers[0])):
            rr = 0
            while True:
                try:
                    graph[c].append(numbers[rr][c])
                except IndexError:
                    break
                rr += 1
    return list(graph.values()), signs.split()


def calc(nums, sign):
    if sign == '+':
        return sum(nums)
    if sign == '*':
        return reduce(lambda x, y: x * y, nums)
    raise Exception(f"Unknown sign {sign}")


@aoc_part(2)
def solve_pt2():
    nums, signs = load_input2()
    ans = 0
    i = 0
    curr = []
    for l in nums:
        if all(x == ' ' for x in l):
            ans += calc(curr, signs[i])
            curr = []
            i += 1
        else:
            curr.append(int("".join(l)))
    return ans + (calc(curr, signs[i]) if curr else 0)  # if something is left calculate it


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
