import math
import re
from dataclasses import dataclass
from itertools import cycle

from utils import aoc_part


@dataclass
class Node:
    origin: str
    L: str
    R: str


def load_input(file_name="in.txt"):
    data = {}
    with open(file_name, encoding='UTF-8') as f:
        lines = f.readlines()
        steps = cycle(lines[0].strip())
        for line in lines[2:]:
            line = line.split("=")
            node = line[0].strip()
            points = re.search(r'(\w+), (\w+)', line[1]).groups()
            data[node] = Node(node, points[0], points[1])
    return steps, data


@aoc_part(1)
def solve_pt1():
    steps, data = load_input()
    loc = data['AAA']
    for cnt, step in enumerate(steps, start=1):
        loc = data[getattr(loc, step)]
        if loc.origin.endswith('Z'):
            return cnt


@aoc_part(2)
def solve_pt2():
    steps, data = load_input()
    nodes = [node for node in data.values() if node.origin.endswith('A')]
    cnt = 0
    res = {}
    while len(res) != len(nodes):
        cnt += 1
        step = next(steps)
        for idx in range(len(nodes)):
            nodes[idx] = data[getattr(nodes[idx], step)]
            if idx not in res and nodes[idx].origin.endswith('Z'):
                res[idx] = cnt  # the first time we see Z for this node

    return math.lcm(*res.values())


solve_pt1()
solve_pt2()
