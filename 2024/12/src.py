from collections import defaultdict

import networkx as nx

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            res.append(list(line))
    return res


def create_graph(data, R, C):
    G = nx.Graph()
    for r in range(R):
        for c in range(C):
            val = data[r][c]
            G.add_node((r, c), val=val)
            for dr in [-1, 1]:
                rr = r + dr
                if 0 <= rr < R:
                    new_val = data[rr][c]
                    if val == new_val:
                        G.add_edge((r, c), (rr, c))
            for dc in [-1, 1]:
                cc = c + dc
                if 0 <= cc < C:
                    new_val = data[r][cc]
                    if val == new_val:
                        G.add_edge((r, c), (r, cc), )
    return G


@aoc_part(1)
def solve_pt1():
    data = load_input()
    G = create_graph(data, len(data), len(data[0]))
    prices = 0

    for garden in nx.connected_components(G):
        garden_size = len(garden)
        nodes_sides = 0
        for node_point in garden:
            neighbors = list(G.neighbors(node_point))
            nodes_sides += 4 - len(neighbors)
        prices += garden_size * nodes_sides

    return prices


@aoc_part(2)
def solve_pt2():
    pass


if __name__ == '__main__':
    solve_pt1()
    # solve_pt2()
