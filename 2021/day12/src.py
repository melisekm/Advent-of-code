import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            r_ = line.strip().split("-")
            res.append([r_[0], r_[1]])
    return res


class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, target):
        self.target = target


class Graph:
    def __init__(self):
        self.G = {}

    # find all disticnt paths in from start to end
    def find_all_pathsP1(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in start.edges:
            if node.name.isupper() or node.name.islower() and node not in path:
                newpaths = self.find_all_pathsP1(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    # find all disticnt paths in from start to end
    def find_all_pathsP2(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in start.edges:
            if node.name == 'start':
                continue

            rule = True
            if node.name.islower():
                lower = list(filter(lambda x: x.name.islower(), path))  # filter only lowercase
                if len(set(lower)) < len(lower):  # if contains something twice
                    rule = node not in path

            if node.name.isupper() or rule:
                newpaths = self.find_all_pathsP2(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


def solve_pt1():
    data = load_input()
    graph = Graph()
    for edge in data:
        A = edge[0]
        B = edge[1]
        if A not in graph.G:
            graph.G[A] = Node(A)
        if B not in graph.G:
            graph.G[B] = Node(B)
        graph.G[A].edges.append(graph.G[B])
        graph.G[B].edges.append(graph.G[A])
    paths = graph.find_all_pathsP1(graph.G['start'], graph.G['end'], [])
    return len(paths)


def solve_pt2():
    data = load_input()
    graph = Graph()
    for edge in data:
        A = edge[0]
        B = edge[1]
        if A not in graph.G:
            graph.G[A] = Node(A)
        if B not in graph.G:
            graph.G[B] = Node(B)
        graph.G[A].edges.append(graph.G[B])
        graph.G[B].edges.append(graph.G[A])
    paths = graph.find_all_pathsP2(graph.G['start'], graph.G['end'], [])
    return len(paths)


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Total time pt1: {(end - start):.3f} sec")

start = timeit.default_timer()
result2 = solve_pt2()
end = timeit.default_timer()
print(result2)
print(f"Total time pt2: {(end - start):.2f} sec")
