import networkx as nx

from utils import aoc_part
import matplotlib.pyplot as plt


@aoc_part(1)
def solve_pt1():
    G = nx.Graph()
    with open("in.txt") as f:
        for line in f:
            source, targets = line.split(":")
            for target in targets.split():
                G.add_edge(source, target)
    cut_value, components = nx.stoer_wagner(G)
    plt.figure(figsize=(16, 12))
    nx.draw(G, with_labels=True)
    plt.savefig("graph.png")
    # based on the graph, we can remove the following edges
    G.remove_edge("tpn", "gxv")
    G.remove_edge("hxq", "txl")
    G.remove_edge("rtt", "zcj")
    connected_components = list(nx.connected_components(G))

    print(len(connected_components[0]) * len(connected_components[1]))  # manual
    return len(components[0]) * len(components[1])  # programmatic


solve_pt1()
