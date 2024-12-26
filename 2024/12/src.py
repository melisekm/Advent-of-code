import networkx as nx

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            res.append(list(line))
    return res


def create_graph(data):
    G = nx.Graph()
    R, C = len(data), len(data[0])
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
    G = create_graph(data)
    prices = 0

    for garden in nx.connected_components(G):
        garden_size = len(garden)
        nodes_sides = 0
        for node_point in garden:
            neighbors = list(G.neighbors(node_point))
            nodes_sides += 4 - len(neighbors)
        prices += garden_size * nodes_sides

    return prices


def count_sides(garden: list[tuple[int, int]], dy, dx, next_node_dy, next_node_dx):
    """
    dy dx - we look at the direction to the side
        ex: -1, 0 means we look up, if we don't see a node in garden, then this is a side
    next_node_dy, next_node_dx - we continue in this direction and do the same
        ex: 0, 1 means we go right and perform the same check
    if we find a node that is not in garden, then this is the end of the side
    """
    seen = set()
    count = 0
    for r, c in garden:
        if (r, c) in seen:
            continue
        seen.add((r, c))
        # look to particular direction from node, if it is not in the garden, then this node is a part of new side
        if (r + dy, c + dx) not in garden:
            count += 1
        else:
            continue
        # go until this side is finished, adding all that belong to it to seen, as those shouldn't be counted twice
        while True:
            next_node = (r + next_node_dy, c + next_node_dx)
            if next_node not in garden:
                break

            above_node = (next_node[0] + dy, next_node[1] + dx)
            if above_node not in garden:
                seen.add(next_node)
            else:
                break
            r += next_node_dy
            c += next_node_dx
    return count


def sum_sides(garden: list[tuple[int, int]]):
    sides = 0
    sides += count_sides(garden, -1, 0, 0, 1)  # up right
    sides += count_sides(garden, 0, -1, 1, 0)  # left, down
    sides += count_sides(garden, 1, 0, 0, 1)  # down, right
    sides += count_sides(garden, 0, 1, 1, 0)  # right, up
    return sides


@aoc_part(2)
def solve_pt2():
    return sum(
        # has to be sorted, otherwise we would count some nodes on side multiple times
        sum_sides(sorted(garden)) * len(garden)
        for garden in nx.connected_components(create_graph(load_input()))
    )


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
