import timeit

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


def calculate_shortest_path_weight(data, N):
    G = createGraph(data, N)
    path = nx.shortest_path(G, source=(0, 0), target=(N - 1, N - 1), weight="weight")
    cena = 0
    for node in path[1:]:
        cena += data[node[0]][node[1]]
    return cena


def solve_pt1():
    data = load_input()
    N = len(data)
    return calculate_shortest_path_weight(data, N)


def solve_pt2():
    def createBigMap():
        bigMap = [[0] * N * 5 for _ in range(N * 5)]
        for i in range(N):
            for j in range(N):
                point = data[i][j]
                tmp = point
                for row in range(5):
                    prev = tmp
                    for column in range(5):
                        val = tmp
                        bigMap[N * row + i][N * column + j] = val
                        tmp = (tmp % 9) + 1
                    tmp = (prev % 9) + 1
        return bigMap

    data = load_input()
    N = len(data)
    data = createBigMap()
    return calculate_shortest_path_weight(data, N * 5)


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Total time pt1: {(end - start):.3f} sec")

start = timeit.default_timer()
result2 = solve_pt2()
end = timeit.default_timer()
print(result2)
print(f"Total time pt2: {(end - start):.3f} sec")
