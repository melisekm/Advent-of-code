from functools import lru_cache

import networkx as nx
from networkx.algorithms.shortest_paths.generic import has_path

from utils import aoc_part

LOAD_FROM_FILE = False

pt1 = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

pt2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""


def load_input(pt, file_name="in.txt"):
    res = []
    if LOAD_FROM_FILE:
        with open(file_name) as f:
            s = f.read()
    else:
        s = pt
    for line in s.splitlines():
        data = line.strip().split(":")
        data[1] = data[1].split()
        res.append(data)
    return res


def paths(G, svr, out, fft, dac, reachability):
    @lru_cache
    def dfs(node, seen_fft, seen_dac):
        ans = 0

        if not reachability[(node, out)]:
            return 0
        if not seen_fft and not reachability[(node, fft)]:
            return 0
        if not seen_dac and not reachability[(node, dac)]:
            return 0

        if node == fft:
            seen_fft = True
        if node == dac:
            seen_dac = True
        if node == out and seen_fft and seen_dac:
            return 1

        for nxt in G.successors(node):
            ans += dfs(nxt, seen_fft, seen_dac)
        return ans

    return dfs(svr, False, False)


@aoc_part(1)
def solve_pt1():
    data = load_input(pt1)
    G = nx.DiGraph()
    for node, edges in data:
        for edge in edges:
            G.add_edge(node, edge)
    reachability = {('out', 'out'): True}
    for node, edges in data:
        reachability[(node, 'out')] = has_path(G, node, 'out')
    return paths(G, 'you', 'out', 'out', 'out', reachability)


@aoc_part(2)
def solve_pt2():
    data = load_input(pt2)
    G = nx.DiGraph()
    for node, edges in data:
        for edge in edges:
            G.add_edge(node, edge)
    reachability = {('out', 'out'): True}
    for node, edges in data:
        for t in ['fft', 'dac', 'out']:
            reachability[(node, t)] = has_path(G, node, t)
    return paths(G, 'svr', 'out', 'fft', 'dac', reachability)


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
