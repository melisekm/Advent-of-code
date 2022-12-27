import copy
from operator import add, mul, sub, truediv

from utils import aoc_part


class Monkey:
    def __init__(self):
        self.number = None
        self.operation = None
        self.monkey1 = None
        self.monkey2 = None

    def __repr__(self):
        return f"Monkey({self.name})"

    def __str__(self):
        return self.__repr__()


operator_map = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv
}


def load_input(file_name="in.txt"):
    res = {}
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            name, rest = line.split(":")
            monkey = Monkey()
            try:
                number = int(rest)
                monkey.number = number
            except ValueError:
                rest = rest.strip()
                monkey.monkey1 = rest[:4]
                monkey.monkey2 = rest[7:]
                monkey.operation = operator_map[rest[5]]
            res[name] = monkey

    return res


def traverse(data, param):
    curr_monkey = data[param]
    if curr_monkey.number:
        return curr_monkey.number
    curr_monkey.number = curr_monkey.operation(traverse(data, curr_monkey.monkey1),
                                               traverse(data, curr_monkey.monkey2))
    return curr_monkey.number


@aoc_part(1)
def solve_pt1():
    data = load_input()
    traverse(data, 'root')
    return round(data['root'].number)


@aoc_part(2)
def solve_pt2():
    orig = load_input()

    # right side doesnt depend on human, find its value first
    data = copy.deepcopy(orig)
    left_monkey = data['root'].monkey1
    right_monkey = data['root'].monkey2
    traverse(data, right_monkey)
    target = data[right_monkey].number
    # make binary search to find human value which evaluates left side of equation to target
    lo = 10000000000000
    hi = 1
    guesses = 0
    while True:
        guesses += 1
        guess = (lo + hi) // 2
        data = copy.deepcopy(orig)
        data['humn'].number += guess
        traverse(data, left_monkey)
        if data[left_monkey].number == target:
            print(f"Found in {guesses} guesses")
            return data['humn'].number
        elif data[left_monkey].number > target:
            hi = guess
        else:
            lo = guess


solve_pt1()
solve_pt2()
