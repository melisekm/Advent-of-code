import functools

from utils import aoc_part


def compare(left, right):
    if type(left) == int and type(right) == list:
        left = [left]
    elif type(left) == list and type(right) == int:
        right = [right]

    if type(left) == int and type(right) == int:
        if left < right:
            raise Exception(-1)  # Correct
        if left > right:
            raise Exception(1)  # Wrong
        return

    longer = max(len(left), len(right))
    for pos in range(longer):
        if pos >= len(left):
            raise Exception(-1)  # Correct
        if pos >= len(right):
            raise Exception(1)  # Wrong
        compare(left[pos], right[pos])


def cmp(left, right):
    try:
        compare(left, right)
    except Exception as e:
        return e.args[0]
    return 0


def load_input(file_name="in.txt"):
    total = []
    with open(file_name) as f:
        res = f.read().split("\n\n")
        for line in res:
            line = line.split("\n")
            total.append([eval(line[0]), eval(line[1])])
    return total


@aoc_part(1)
def solve_pt1():
    data = load_input()
    correct_indices = []
    for idx, packets in enumerate(data, 1):
        try:
            compare(*packets)
        except Exception as e:
            if e.args[0] < 0:
                correct_indices.append(idx)
    return sum(correct_indices)


@aoc_part(2)
def solve_pt2():
    data = load_input()
    flat_list = [item for sublist in data for item in sublist] + [[[2]], [[6]]]
    flat_list.sort(key=functools.cmp_to_key(cmp))
    return (flat_list.index([[2]]) + 1) * (flat_list.index([[6]]) + 1)


solve_pt1()
solve_pt2()
