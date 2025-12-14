from collections import defaultdict

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    S = None
    with open(file_name) as f:
        for line in f:
            if not S:
                S = line.find("S")
            res.append(list(line.strip()))
    return res, (0, S)


def calc_pt1(graph: list[list[str]]):
    return sum(
        graph[r][c] == '^' and graph[r - 1][c] == '|'
        for r in range(len(graph))
        for c in range(len(graph[r]))
    )


def solve(pt: int) -> int:
    graph, S = load_input()
    beams = defaultdict(int)
    beams[S] += 1
    while True:
        for pos, cnt in list(beams.items()):
            r, c = pos[0] + 1, pos[1]
            if r >= len(graph):
                if pt == 1:
                    return calc_pt1(graph)
                return sum(beams.values())
            if graph[r][c] == '^':
                new_b_1 = (r, c - 1)
                new_b_2 = (r, c + 1)
                beams[new_b_1] += cnt
                beams[new_b_2] += cnt
                graph[r][c - 1] = '|'
                graph[r][c + 1] = '|'
            else:
                beams[(r, c)] += cnt
                graph[r][c] = '|'
            del beams[pos]


@aoc_part(1)
def solve_pt1():
    return solve(1)


@aoc_part(2)
def solve_pt2():
    return solve(2)


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
