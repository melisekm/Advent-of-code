import networkx as nx

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            a, b = line.strip().split(",")
            res.append((int(a), int(b)))
    return res


def create_graph(data, R, C, max_cut):
    cut = set(data[:max_cut])
    data = [
        ['#' if (i, j) in cut else '.' for j in range(C)]
        for i in range(R)
    ]

    G = nx.Graph()
    for r in range(R):
        for c in range(C):
            val = data[r][c]
            if val != '.':
                continue
            for dr in [-1, 1]:
                rr = r + dr
                if 0 <= rr < R:
                    new_val = data[rr][c]
                    if new_val == '.':
                        G.add_edge((r, c), (rr, c))
            for dc in [-1, 1]:
                cc = c + dc
                if 0 <= cc < C:
                    new_val = data[r][cc]
                    if new_val == '.':
                        G.add_edge((r, c), (r, cc))
    return G, (0, 0), (R - 1, C - 1)


@aoc_part(1)
def solve_pt1():
    data = load_input()
    R, C = 70, 70
    G, start, end = create_graph(data, R + 1, C + 1, max_cut=1024)
    path = nx.shortest_path(G, source=start, target=end)
    return len(path) - 1


@aoc_part(2)
def solve_pt2():
    data = load_input()
    R, C = 70, 70
    for i in reversed(range(len(data))):
        G, start, end = create_graph(data, R + 1, C + 1, max_cut=i)
        try:
            nx.shortest_path(G, source=start, target=end)
            return data[i]
        except nx.NetworkXNoPath:
            pass


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
