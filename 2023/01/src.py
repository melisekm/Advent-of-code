import re

from utils import aoc_part


@aoc_part(1)
def solve_pt1():
    res = 0
    with open("in.txt") as f:
        for line in f:
            nums = list(map(str, re.findall(r"\d", line)))
            res += int(nums[0] + nums[-1])
    return res


@aoc_part(2)
def solve_pt2():
    res = 0
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open("in.txt") as f:
        for line in f:
            nums = []
            line = line.strip()
            for idx, char in enumerate(line):
                for char_num, char_val in enumerate(numbers, start=1):
                    cut = line[idx:idx + len(char_val)]
                    if cut == char_val:
                        nums.append(str(char_num))
                        break
                try:
                    int(char)
                    nums.append(char)
                except ValueError:
                    pass
            res += int(nums[0] + nums[-1])
    return res


solve_pt1()
solve_pt2()
