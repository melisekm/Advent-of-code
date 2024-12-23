import networkx as nx
from networkx.algorithms.clique import enumerate_all_cliques, find_cliques

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            res.append(line.split("-"))
    return res


def create_graph(data):
    G = nx.Graph()
    for node_a, node_b in data:
        G.add_edge(node_a, node_b)
    return G


def find_friends(G, seen, nodes_to_check):
    if len(nodes_to_check) == 3:
        sorted_check = tuple(sorted(nodes_to_check, key=lambda x: str(x)))
        if sorted_check in seen:
            return
        seen.add(sorted_check)
        return

    for node in nodes_to_check:
        for neighbor in G.neighbors(node):
            # if all nodes in nodes to check are in neighbors of neighbor
            n_neighbors = set(G.neighbors(neighbor))
            if all([n in n_neighbors for n in nodes_to_check]):
                find_friends(G, seen, nodes_to_check + (neighbor,))


def nx_pt1(G):
    return len([
        clique for clique in enumerate_all_cliques(G)
        if len(clique) == 3 and any([node.startswith('t') for node in clique])
    ])


@aoc_part(1)
def solve_pt1():
    data = load_input()
    G = create_graph(data)
    # return nx_pt1(G)
    seen = set()
    for node in G.nodes():
        if node.startswith('t'):
            find_friends(G, seen, (node,))
    return len(seen)


@aoc_part(2)
def solve_pt2():
    return ",".join(sorted(max(find_cliques(create_graph(load_input())), key=len)))


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
