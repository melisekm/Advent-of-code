import operator

from utils import aoc_part


def solve(line, select, op):
    return (
        0 if all(x == 0 for x in line) else
        op(line[select], solve([line[idx + 1] - line[idx] for idx in range(len(line) - 1)], select, op))
    )


def run(select, op):
    return sum(
        solve(history, select, op)
        for history in (list(map(int, line.split())) for line in open("in.txt").readlines())
    )


@aoc_part(1)
def solve_pt1():
    return run(-1, operator.add)


@aoc_part(2)
def solve_pt2():
    return run(0, operator.sub)


solve_pt1()
solve_pt2()
