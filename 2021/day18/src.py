import math
import timeit
from collections import deque


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            res.append(line.strip())
    return res


tree_pos = 0


def calculate(tree):
    if isinstance(tree, int):
        return tree
    else:
        return 3 * calculate(tree.L) + calculate(tree.R) * 2


class Tree:
    def __init__(self, parent):
        self.L = None
        self.R = None
        self.parent = parent

    def create(self, code):
        global tree_pos
        if code[tree_pos] not in ("[", ",", "]"):
            symbol = int(code[tree_pos])
            tree_pos += 1
            return symbol
        if code[tree_pos] == "[":
            tree_pos += 1
            self.L = Tree(self).create(code)
        if code[tree_pos] == ",":
            tree_pos += 1
            self.R = Tree(self).create(code)
        tree_pos += 1
        return self


def explode(string):
    pos = 0
    depth = 0
    while pos < len(string):
        if depth > 4:
            L = string[pos]
            R = string[pos + 2]
            for _ in range(4):
                string.pop(pos - 1)
            string[pos - 1] = 0
            pos -= 2
            tmp = pos + 2
            while pos >= 0:
                try:
                    val = int(string[pos])
                    string[pos] = L + val
                    break
                except ValueError:
                    pos -= 1
            pos = tmp
            while pos < len(string):
                try:
                    val = int(string[pos])
                    string[pos] = R + val
                    break
                except ValueError:
                    pos += 1
            return string

        if string[pos] == "[":
            depth += 1
        elif string[pos] == "]":
            depth -= 1
        pos += 1


def split(string):
    pos = 0
    while pos + 1 < len(string):
        try:
            val = int(string[pos])
            if val > 9:
                left = math.floor(val / 2)
                right = math.ceil(val / 2)
                string[pos] = "["
                string.insert(pos + 1, left)
                string.insert(pos + 2, ",")
                string.insert(pos + 3, right)
                string.insert(pos + 4, "]")
                return string
        except ValueError:
            pass
        pos += 1


def make_arr(string):
    res = []
    pos = 0
    while pos < len(string):
        try:
            val = int(string[pos])
            try:
                if pos + 1 < len(string):
                    val2 = int(string[pos + 1])
                    pos += 1
                    val = int(val + val2)
                    res.append(val)
            except ValueError:
                res.append(val)
        except ValueError:
            res.append(string[pos])
        pos += 1
    return res


def reduce(string):
    string = make_arr(string)
    while True:
        new_str = explode(string)
        if new_str:
            string = new_str
            continue
        new_str = split(string)
        if new_str:
            string = new_str
        else:
            break
    return string


def add(first, other):
    return ["["] + first + [","] + other + ["]"]


def solve_pt1():
    data = load_input()
    numbers = deque()
    for string in data:
        number = reduce(string)
        numbers.append(number)
    while len(numbers) > 1:
        first = numbers.popleft()
        second = numbers.popleft()
        new = add(first, second)
        new = reduce(new)
        numbers.appendleft(new)

    strjoined = "".join(map(str, numbers[0]))
    tree = Tree(None)
    tree.create(strjoined)
    return calculate(tree)


def try_two_numbers(num1, num2):
    global tree_pos
    tree_pos = 0
    new = add(num1, num2)
    new = reduce(new)
    strjoined = "".join(map(str, new))
    tree = Tree(None)
    tree.create(strjoined)
    return calculate(tree)


def solve_pt2():
    data = load_input()
    numbers = []
    for string in data:
        number = reduce(string)
        numbers.append(number)
    res = 0
    for i, num1 in enumerate(numbers[:-1]):
        for j, num2 in enumerate(numbers[i + 1:]):
            first = try_two_numbers(num1, num2)
            res = max(res, first)
            second = try_two_numbers(num2, num1)
            res = max(res, second)

    return res


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Total time pt1: {(end - start):.3f} sec")

start = timeit.default_timer()
result2 = solve_pt2()
end = timeit.default_timer()
print(result2)
print(f"Total time pt2: {(end - start):.3f} sec")
