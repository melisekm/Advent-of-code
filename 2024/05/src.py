import operator
from collections import defaultdict

from utils import aoc_part


def load_input(file_name="in.txt"):
    res1 = defaultdict(list)
    with open(file_name) as f:
        p1, p2 = f.read().split("\n\n")
        for line in p1.splitlines():
            a, b = tuple(map(int, line.split("|")))
            res1[a].append(b)
        res2 = [list(map(int, x.split(','))) for x in p2.splitlines()]
    return res1, res2


def solve(res1, l, recurse=False, depth=0):
    for idx in range(len(l) - 1):
        num = l[idx]
        rest = l[idx + 1:]
        for jdx, x in enumerate(rest, start=idx + 1):
            if x not in res1[num]:
                # found one that is wrong
                if recurse:
                    # we are solving it, so switch them up and continue
                    l[idx], l[jdx] = l[jdx], l[idx]
                    return solve(res1, l, recurse, depth + 1)
                # not solving, just report that this l is not ok
                return None
    if depth > 0:
        # the list is fixed after recursing
        return l
    return "OK"


def get_result(p2=False, op=operator.eq):
    res1, res2 = load_input()
    return sum(
        x[len(x) // 2]
        for x in (l for l in res2 if op(solve(res1, l, recurse=p2), "OK"))
    )


@aoc_part(1)
def solve_pt1():
    return get_result()


@aoc_part(2)
def solve_pt2():
    return get_result(p2=True, op=operator.ne)


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
