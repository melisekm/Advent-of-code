from utils import aoc_part


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __str__(self):
        return self.__repr__()


def load_input(file_name="in.txt"):
    res = []
    lowest_y = 0
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            line = line.split("->")
            tmp = []
            for coord in line:
                coord = coord.strip()
                x, y = coord.split(",")
                tmp.append(Point(x, y))
                lowest_y = max(lowest_y, int(y))
            res.append(tmp)
    return res, lowest_y


def is_rock_beneath(line_begin, line_end, x, y):
    return \
            line_begin.y == y and (line_begin.x <= x <= line_end.x or line_end.x <= x <= line_begin.x) or \
            line_begin.x == x and (line_begin.y <= y <= line_end.y or line_end.y <= y <= line_begin.y)


def is_sand_beneath(sand, x, y):
    return (x, y) in sand


def rock_check(sand, data, pos, x, y, check=True):
    for lines in data:
        line_id = 0
        while line_id < len(lines) - 1:
            line_begin = lines[line_id]
            line_end = lines[line_id + 1]
            if is_rock_beneath(line_begin, line_end, x, y + 1) or is_sand_beneath(sand, x, y + 1):
                if not check:
                    return True
                if rock_check(sand, data, pos, x - 1, y, check=False):
                    if rock_check(sand, data, pos, x + 1, y, check=False):
                        sand.add((x, y))
                        raise Exception(0)
                    else:
                        raise Exception(1)
                else:
                    raise Exception(-1)
            line_id += 1
    return False


@aoc_part(1)
def solve_pt1():
    data, lowest_y = load_input()
    sand = set()
    i = 0
    while True:
        pos = Point(500, 0)
        while True:
            try:
                rock_check(sand, data, pos, pos.x, pos.y)
            except Exception as e:
                if e.args[0] == 0:
                    break
                else:
                    pos.x += e.args[0]
            pos.y += 1
            if pos.y == lowest_y:
                return i
        i += 1


@aoc_part(2)
def solve_pt2():
    sand = set()
    data, lowest_y = load_input()
    lowest_y += 2
    data.append([Point(-1000, lowest_y), Point(1000, lowest_y)])
    i = 0
    while (500, 0) not in sand:
        pos = Point(500, 0)
        while True:
            try:
                rock_check(sand, data, pos, pos.x, pos.y)
            except Exception as e:
                if e.args[0] == 0:
                    break
                else:
                    pos.x += e.args[0]
            pos.y += 1
        i += 1

    return i


solve_pt1()
solve_pt2()
