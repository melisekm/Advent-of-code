import helpers2025
from utils import aoc_part
from dataclasses import dataclass

@dataclass(frozen=True)
class V2:
    x: int
    y: int


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            res.append(V2(*helpers2025.get_all_integers_from_string(line)))
    return res


def area(a: V2, b: V2) -> int:
    if a.x > b.x:
        first = a
        second = b
    else:
        first = b
        second = a

    return (abs(first.x - second.x) + 1) * (abs(first.y - second.y) + 1)


@aoc_part(1)
def solve_pt1():
    data = load_input()
    areas = {}

    for x in data:
        for y in data:
           if x is y:
               continue
           if (x, y) in areas or (y, x) in areas:
               continue
           areas[(x, y)] = area(x, y)
    sorted_pairs = sorted(areas, key=areas.get, reverse=True)
    sorted_pairs = [(p, areas[p]) for p in sorted_pairs]
    return sorted_pairs[0][1]



# @aoc_part(2)
# def solve_pt2():
#     data = load_input()
#
#     pass

if __name__ == '__main__':
    solve_pt1()
    # solve_pt2()
