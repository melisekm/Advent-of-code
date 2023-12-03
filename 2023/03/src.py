import re
from collections import defaultdict

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name, encoding='UTF-8') as f:
        for line in f:
            res.append(line.strip())
    nums = defaultdict(list)
    for idx, line in enumerate(res):
        matches = re.finditer(r'\d+', line)
        for match in matches:
            nums[idx].append((int(match.group()), match.span()))
    return res, nums


def safe_get(data, row, col):
    try:
        return data[row][col]
    except IndexError:
        return None


@aoc_part(1)
def solve_pt1():
    data, nums = load_input()
    valid = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col].isdigit() or data[row][col] == '.':  # find symbols
                continue
            possible_nums = {k: v for k, v in nums.items() if row - 1 <= k <= row + 1}  # only rows around the symbol
            for r in [-1, 0, 1]:  # look around
                for c in [-1, 0, 1]:
                    # out of bounds or or no numbers in the row
                    if not safe_get(data, row + r, col + c) or row + r not in possible_nums:
                        continue
                    for potential in possible_nums[row + r]:  # all numbers in the row
                        number, span = potential
                        if span[0] <= col + c <= span[1]:  # position of the number has to be in the span
                            valid.append(number)
                            possible_nums[row + r].remove(potential)  # do not reuse the number for current symbol
                            break  # same position can't be in multiple spans

    return sum(valid)


@aoc_part(2)
def solve_pt2():
    # same as pt1 but only for * and valid exactly 2 numbers around the *
    data, nums = load_input()
    valid = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] != '*':
                continue
            valids = []
            possible_nums = {k: v for k, v in nums.items() if row - 1 <= k <= row + 1}
            for r in [-1, 0, 1]:
                for c in [-1, 0, 1]:
                    # out of bounds or or no numbers in the row
                    if not safe_get(data, row + r, col + c) or row + r not in possible_nums:
                        continue
                    for potential in possible_nums[row + r]:
                        number, span = potential
                        if span[0] <= col + c <= span[1]:
                            valids.append(number)
                            possible_nums[row + r].remove(potential)
                            break
            if len(valids) == 2:
                valid.append(valids[0] * valids[1])
    return sum(valid)


solve_pt1()
solve_pt2()
