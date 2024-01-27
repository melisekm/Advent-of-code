from utils import aoc_part
import networkx as nx


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            row = []
            for node in line:
                row.append(int(node))
            res.append(row)
    return res


def createGraph(data, N):
    G = nx.DiGraph()
    for r in range(N):
        for c in range(N):
            for dr in [-1, 1]:
                rr = r + dr
                if 0 <= rr < N:
                    G.add_edge((r, c), (rr, c), weight=data[rr][c])
            for dc in [-1, 1]:
                cc = c + dc
                if 0 <= cc < N:
                    G.add_edge((r, c), (r, cc), weight=data[r][cc])
    return G


from networkx.algorithms.shortest_paths.weighted import _dijkstra

paths = {(0, 0): [(0, 0)]}
pred = {(0, 0): []}


def cb(a, b, c):
    last_three_points = paths[a][-4:-1]
    next_point = b
    # if last three have same direction and next point is in the same direction then set weight to infinity
    if len(last_three_points) == 3 and last_three_points[0][0] == last_three_points[1][0] == last_three_points[2][0] and \
            last_three_points[0][0] == next_point[0]:
        return None
    if len(last_three_points) == 3 and last_three_points[0][1] == last_three_points[1][1] == last_three_points[2][1] and \
            last_three_points[0][1] == next_point[1]:
        return None
    return c.get('weight', 1)


def calculate_shortest_path_weight(data, N):
    G = createGraph(data, N)
    target = (N - 1, N - 1)
    res = _dijkstra(G, source=(0, 0), pred=pred, paths=paths, weight=cb, target=target)
    # path = nx.shortest_path(G, source=(0, 0), target=(N - 1, N - 1), weight=cb)
    best_path = paths[target]
    for idx, R in enumerate(data):
        for jdx, C in enumerate(R):
            if (idx, jdx) in best_path:
                print("X", end="")
            else:
                print(C, end="")
        print()
    return res[target]


@aoc_part(1)
def solve_pt1():
    raise NotImplementedError()
    data = load_input()
    N = len(data)
    return calculate_shortest_path_weight(data, N)

    pass


#
# @aoc_part(2)
# def solve_pt2():
#     data = load_input()
#
#     pass


solve_pt1()
# solve_pt2()
