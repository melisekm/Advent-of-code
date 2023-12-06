from utils import aoc_part
from tqdm import trange
import re


def load_input(file_name="in.txt"):
    with open(file_name, encoding='UTF-8') as f:
        res = [[int(x) for x in re.findall(r'\d+', line)] for line in f]
    return [(res[0][i], res[1][i]) for i in range(len(res[0]))]


def solve(data):
    res = 1
    for race in data:
        time, best_distance = race
        ways = 0
        for time_spend_holding in trange(time) if len(data) == 1 else range(time):
            speed = (time - time_spend_holding)
            distance = speed * time_spend_holding
            if distance > best_distance:
                ways += 1
        res *= ways
    return res


@aoc_part(1)
def solve_pt1():
    return solve(load_input())


@aoc_part(2)
def solve_pt2():
    data = load_input()
    time = int("".join([str(x[0]) for x in data]))
    distance = int("".join([str(x[1]) for x in data]))
    return solve([(time, distance)])


solve_pt1()
solve_pt2()
