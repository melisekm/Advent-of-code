import timeit
from functools import reduce


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            row = []
            line = line.strip()
            for c in line:
                row.append(int(c))
            res.append(row)
    return res


idxs = []


def get_smery(i, j, mapa):
    hore = i - 1
    dole = i + 1
    vlavo = j - 1
    vpravo = j + 1
    smeryI = [hore, dole]
    smeryJ = [vlavo, vpravo]
    if i == 0:
        smeryI.remove(hore)
    if j == 0:
        smeryJ.remove(vlavo)
    if i == len(mapa) - 1:
        smeryI.remove(dole)
    if j == len(mapa[i]) - 1:
        smeryJ.remove(vpravo)

    return smeryI, smeryJ


def solve_pt1(p2=False):
    def poobzeraj_sa(i, j, val, mapa):
        smeryI, smeryJ = get_smery(i, j, mapa)
        for i_ in smeryI:
            if mapa[i_][j] <= val:
                return False
        for j_ in smeryJ:
            if mapa[i][j_] <= val:
                return False

        return True

    mapa = load_input()
    res = 0
    for i, row in enumerate(mapa):
        for j, val in enumerate(row):
            if poobzeraj_sa(i, j, val, mapa):
                res += val + 1
                if p2:
                    idxs.append((i, j))
    return res


class Node:
    def __init__(self, val, i, j):
        self.val = val
        self.i = i
        self.j = j
        self.edges = None

    def __str__(self):
        return str(self.i) + "," + str(self.j) + ",val=" + str(self.val)


class Edge:
    def __init__(self, target):
        self.target = target


def poobzeraj_sa(i, j, mapa):
    smeryI, smeryJ = get_smery(i, j, mapa)
    nns = []
    for i_ in smeryI:
        nns.append([i_, j])
    for j_ in smeryJ:
        nns.append([i, j_])
    return nns


class Graph:
    def __init__(self, mapa):
        self.G = {}
        self.mapa = mapa
        self.curr = 0

    def create_edges(self, nns):
        edges = []
        for neighbor in nns:
            n_i = neighbor[0]
            n_j = neighbor[1]
            if (n_i, n_j) not in self.G:
                self.G[(n_i, n_j)] = Node(self.mapa[n_i][n_j], n_i, n_j)
            edges.append(Edge(self.G[(n_i, n_j)]))
        return edges

    def dfs(self, node, visited):
        visited.add(node)
        self.curr += 1
        for edge in node.edges:
            if edge.target not in visited:
                if edge.target.val != 9:
                    self.dfs(edge.target, visited)


def solve_pt2():
    mapa = load_input()
    graph = Graph(mapa)
    lows = idxs
    solve_pt1(True)
    for i, row in enumerate(mapa):
        for j, val in enumerate(row):
            nns = poobzeraj_sa(i, j, mapa)
            node = Node(val, i, j)
            if (i, j) not in graph.G:
                graph.G[(i, j)] = node
            graph.G[(i, j)].edges = graph.create_edges(nns)
    visited = set()
    res = []
    for pos, node in graph.G.items():
        if pos in lows:
            graph.dfs(node, visited)
            res.append(graph.curr)
            graph.curr = 0

    return reduce((lambda x, y: x * y), sorted(res, reverse=True)[:3])


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Cas vykonavania pt1:{end - start} sec")

start = timeit.default_timer()
result2 = solve_pt2()
end = timeit.default_timer()
print(result2)
print(f"Cas vykonavania pt2:{end - start} sec")
