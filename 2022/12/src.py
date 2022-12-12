import sys
import timeit

import networkx as nx


def load_input(file_name="in.txt"):
    res = []
    sources = []
    with open(file_name) as f:
        for R, line in enumerate(f):
            line = line.strip()
            row = []
            for C, node in enumerate(line):
                if node == "S":
                    source = (R, C)
                    node = 'a'
                if node == 'a':
                    sources.append((R, C))
                elif node == "E":
                    target = (R, C)
                    node = 'z'
                row.append((int(ord(node) - ord('a'))))
            res.append(row)
    return res, source, target, sources


def create_graph(data, R, C):
    graph = nx.DiGraph()
    for r in range(R):
        for c in range(C):
            for dr in [-1, 0, 1]:
                rr = r + dr
                if (r, c) != (rr, c) and 0 <= rr < R and data[rr][c] <= data[r][c] + 1:
                    graph.add_edge((r, c), (rr, c), weight=1)
            for dc in [-1, 0, 1]:
                cc = c + dc
                if (r, c) != (rr, c) and 0 <= cc < C and data[r][cc] <= data[r][c] + 1:
                    graph.add_edge((r, c), (r, cc), weight=1)
    return graph


def calculate_shortest_path_weight(graph, source, target):
    path = nx.shortest_path(graph, source=source, target=target, weight="weight")
    return len(path) - 1


def solve_pt1():
    data, source, target, _ = load_input()
    R = len(data)
    C = len(data[0])
    graph = create_graph(data, R, C)
    return calculate_shortest_path_weight(graph, source, target)


def solve_pt2():
    data, source, target, sources = load_input()
    R = len(data)
    C = len(data[0])
    best = sys.maxsize
    graph = create_graph(data, R, C)
    for idx, source in enumerate(sources):
        try:
            best = min(calculate_shortest_path_weight(graph, source, target), best)
        except:
            pass
    return best


def run_part(solve_fn, part_idx):
    start = timeit.default_timer()
    result = solve_fn()
    end = timeit.default_timer()
    print(result)
    print(f"Total time pt{part_idx}: {(end - start):.3f} sec")


run_part(solve_pt1, 1)
run_part(solve_pt2, 2)
