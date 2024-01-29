import copy
from collections import defaultdict

import networkx as nx
from matplotlib import pyplot as plt
from tqdm import tqdm

from utils import aoc_part


def load_input(file_name=r"in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            row = []
            for node in line:
                row.append(node)
            res.append(row)
    return res, (0, 1), (len(res) - 1, len(res[0]) - 2)


def create_main_graph(data, pt1=True):
    G = nx.DiGraph()
    intersections = []
    for r in range(len(data)):
        for c in range(len(data[r])):
            if pt1:
                if data[r][c] == '>' and data[r][c + 1] == '.':
                    G.add_edge((r, c), (r, c + 1))
                elif data[r][c] == '<' and data[r][c - 1] == '.':
                    G.add_edge((r, c), (r, c - 1))
                elif data[r][c] == '^' and data[r - 1][c] == '.':
                    G.add_edge((r, c), (r - 1, c))
                elif data[r][c] == 'v' and data[r + 1][c] == '.':
                    G.add_edge((r, c), (r + 1, c))
                if data[r][c] != '.':
                    continue
            if data[r][c] != "#":
                choice_cnt = 0
                for dr in [-1, 1]:
                    rr = r + dr
                    if 0 <= rr < len(data) and data[rr][c] != "#":
                        choice_cnt += 1
                        G.add_edge((r, c), (rr, c))
                for dc in [-1, 1]:
                    cc = c + dc
                    if 0 <= cc < len(data[r]) and data[r][cc] != "#":
                        choice_cnt += 1
                        G.add_edge((r, c), (r, cc))
                if choice_cnt > 2:
                    intersections.append((r, c))
    return G, intersections


@aoc_part(1)
def solve_pt1():
    data, start, end = load_input()
    G, _ = create_main_graph(data)
    paths = list(nx.all_simple_paths(G, start, end))
    longest = max(paths, key=len)
    return len(longest) - 1


def create_graph_with_walled_off_intersections(G, intersections, intersection1, intersection2):
    GG = copy.deepcopy(G)
    for intersection in intersections:
        if intersection == intersection1 or intersection == intersection2:
            continue
        GG.remove_node(intersection)
    return GG


def shortest_paths_between_intersections(G, intersections):
    # this will be a new graph with nodes being intersections and edges being the shortest path between them
    # so weight is the length of the path
    res = defaultdict(list)
    pbar = tqdm(total=len(intersections) * (len(intersections) - 1) // 2)
    for idx, intersection1 in enumerate(intersections):
        for jdx, intersection2 in enumerate(intersections[idx + 1:]):
            # cant pass through other intersections
            GG = create_graph_with_walled_off_intersections(G, intersections, intersection1, intersection2)
            try:
                shortest_path = nx.shortest_path(GG, intersection1, intersection2)
                res[intersection1].append((intersection2, shortest_path))
                res[intersection2].append((intersection1, shortest_path[::-1]))
            except nx.NetworkXNoPath:
                pass
            pbar.update(1)
    return res


def create_new_graph(res):
    g = nx.Graph()
    for intersection, paths in res.items():
        for path in paths:
            g.add_edge(intersection, path[0], weight=len(path[1]) - 1)
    return g


def get_weight(path, shortest_intersection_paths):
    weight = 0
    for idx, node in enumerate(path[:-1]):
        main_node = shortest_intersection_paths[node]
        second_node = path[idx + 1]
        for path_ in main_node:
            if path_[0] == second_node:
                weight += len(path_[1]) - 1
                break
        else:
            raise Exception("Path not found")

    return weight


def draw_graph(new_graph):
    pos = nx.spring_layout(new_graph)
    nx.draw(new_graph, pos=pos, with_labels=True)
    labels = nx.get_edge_attributes(new_graph, 'weight')
    nx.draw_networkx_edge_labels(new_graph, edge_labels=labels, pos=pos)
    plt.show()


@aoc_part(2)
def solve_pt2():
    data, start, end = load_input()
    G, intersections = create_main_graph(data, pt1=False)
    intersections.append(start)
    intersections.append(end)
    # we need to find the shortest path between all intersections, create graph where length of path is weight
    # the edges in this graph are paths that do not cross other intersections
    shortest_intersection_paths = shortest_paths_between_intersections(G, intersections)
    new_graph = create_new_graph(shortest_intersection_paths)

    # draw_graph(new_graph)

    return max(
        get_weight(path, shortest_intersection_paths)
        for path in nx.all_simple_paths(new_graph, start, end)
    )


solve_pt1()
solve_pt2()
