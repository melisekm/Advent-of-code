import copy
from itertools import cycle
from decimal import Decimal

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            res.append((Decimal(line.strip())))
    return res


class Decimal(Decimal):
    def __eq__(self, other):
        return id(self) == id(other)


@aoc_part(1)
def solve_pt1():
    data = load_input()
    initial = cycle(copy.deepcopy(data))
    i = 0
    while i < len(data):
        number_d = next(initial)
        number = int(number_d)
        if number != 0:
            num_pos = data.index(number_d)
            data.pop(num_pos)
            if number == -num_pos:
                data.append(number_d)
            else:
                data.insert((num_pos + number) % len(data), number_d)
        i += 1
    cntr = None
    data = cycle(data)
    res = []
    while True:
        num = next(data)
        num = int(num)
        if cntr is not None:
            cntr += 1
            if cntr in [1000, 2000, 3000]:
                res.append(num)
                if len(res) == 3:
                    return sum(res)
        if not cntr and num == 0:
            cntr = 0


@aoc_part(2)
def solve_pt2():
    pass
    data = load_input()
    data = [x * 811589153 for x in data]
    for _ in range(10):
        initial = cycle(copy.deepcopy(data))
        i = 0
        while i < len(data):
            number_d = next(initial)
            number = int(number_d)
            if number != 0:
                num_pos = data.index(number_d)
                data.pop(num_pos)
                if number == -num_pos:
                    data.append(number_d)
                else:
                    data.insert((num_pos + number) % len(data), number_d)
            i += 1
    cntr = None
    data = cycle(data)
    res = []
    while True:
        num = next(data)
        num = int(num)
        if cntr is not None:
            cntr += 1
            if cntr in [1000, 2000, 3000]:
                res.append(num)
                if len(res) == 3:
                    return sum(res)
        if not cntr and num == 0:
            cntr = 0


solve_pt1()
solve_pt2()
