import networkx as nx

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            res.append([int(x) if x != '.' else -1 for x in line])
    return res


directions = [
    [0, -1],
    [0, 1],
    [1, 0],
    [-1, 0],
]


def dfs(data, R, C, start, end, visited):
    if start == end:
        raise ValueError
    visited.add(start)
    idx, jdx = start
    curr_val = data[idx][jdx]
    for i, j in directions:
        di = idx + i
        dj = jdx + j
        if di < 0 or di >= R or dj < 0 or dj >= C:
            continue
        if (di, dj) in visited:
            continue
        val = data[di][dj]
        if curr_val + 1 == val:
            dfs(data, R, C, (di, dj), end, visited)
    return False


@aoc_part(1)
def solve_pt1_custom():
    data, R, C, starting_points, end_points = prepare()

    res = 0
    for starting_point in starting_points:
        for end_point in end_points:
            visited = set()
            try:
                dfs(data, R, C, starting_point, end_point, visited)
            except ValueError:
                res += 1
    return res


def prepare():
    data = load_input()
    starting_points = []
    end_points = []
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == 0:
                starting_points.append((i, j))
            elif char == 9:
                end_points.append((i, j))
    return data, len(data), len(data[0]), starting_points, end_points


def create_graph(data, R, C):
    G = nx.DiGraph()
    for r in range(R):
        for c in range(C):
            val = data[r][c]
            for dr in [-1, 1]:
                rr = r + dr
                if 0 <= rr < R:
                    new_val = data[rr][c]
                    if val + 1 == new_val:
                        G.add_edge((r, c), (rr, c))
            for dc in [-1, 1]:
                cc = c + dc
                if 0 <= cc < C:
                    new_val = data[r][cc]
                    if val + 1 == new_val:
                        G.add_edge((r, c), (r, cc))
    return G


@aoc_part(1)
def solve_pt1():
    data, R, C, starting_points, end_points = prepare()
    G = create_graph(data, R, C)
    res = 0
    for starting_point in starting_points:
        for end_point in end_points:
            if nx.has_path(G, starting_point, end_point):
                res += 1

    return res


@aoc_part(2)
def solve_pt2():
    data, R, C, starting_points, end_points = prepare()
    G = create_graph(data, R, C)
    return sum(
        sum(1 for _ in nx.all_simple_paths(G, starting_point, end_point))
        for end_point in end_points
        for starting_point in starting_points
    )


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
