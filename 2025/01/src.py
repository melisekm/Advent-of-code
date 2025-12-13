from helpers2025 import get_all_integers_from_string, get_lines_as_strings
from utils import aoc_part


def load_input(file_name="in.txt"):
    return get_lines_as_strings(file_name)


@aoc_part(1)
def solve_pt1():
    data = load_input()
    curr = 50
    res = 0
    for l in data:
        num = get_all_integers_from_string(l)[0]
        if l[0] == 'L':
            curr -= num
        elif l[0] == 'R':
            curr += num
        curr %= 100
        if curr == 0:
            res += 1
    return res


@aoc_part(2)
def solve_pt2():
    data = load_input()
    curr = 50
    res = 0
    for l in data:
        num = get_all_integers_from_string(l)[0]
        if l[0] == 'L':
            new = curr - num
        elif l[0] == 'R':
            new = curr + num
        else:
            raise ValueError(f"Unknown direction: {l[0]}")
        if new == 0:
            res += 1
        else:
            k = int(abs(new / 100))
            if curr > 0 > new:
                k += 1
            elif curr < 0 < new:
                k += 1
            res += k
        curr = new % 100
    return res


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
