import timeit
from collections import defaultdict


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip().replace(",", " ").split(" -> ")
            first = list(map(int, line[0].split()))
            second = list(map(int, line[1].split()))
            res.append([first, second])
    return res


def solve_pt1():
    lines = load_input()
    mapa = {}
    for line in lines:
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]
        if y1 == y2:
            delta = 1 if x1 < x2 else -1
            pocet = abs(x2 - x1)
            for i in range(pocet + 1):
                if y1 not in mapa:
                    mapa[y1] = defaultdict(int)
                mapa[y1][x1 + i * delta] += 1

        elif x1 == x2:
            delta = 1 if y1 < y2 else -1
            pocet = abs(y2 - y1)
            for i in range(pocet + 1):
                y = y1 + i * delta
                if y not in mapa:
                    mapa[y] = defaultdict(int)
                mapa[y][x1] += 1
    res = 0
    for value in mapa.values():
        for num in value.values():
            if num > 1:
                res += 1
    return res


def solve_pt2():
    lines = load_input()
    mapa = {}
    for line in lines:
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]
        if y1 == y2:
            delta = 1 if x1 < x2 else -1
            pocet = abs(x2 - x1)
            for i in range(pocet + 1):
                if y1 not in mapa:
                    mapa[y1] = defaultdict(int)
                mapa[y1][x1 + i * delta] += 1

        elif x1 == x2:
            delta = 1 if y1 < y2 else -1
            pocet = abs(y2 - y1)
            for i in range(pocet + 1):
                y = y1 + i * delta
                if y not in mapa:
                    mapa[y] = defaultdict(int)
                mapa[y][x1] += 1
        else:
            deltaX = 1 if x1 < x2 else -1
            deltaY = 1 if y1 < y2 else -1
            pocet = abs(y2 - y1)
            for i in range(pocet + 1):
                y = y1 + i * deltaY
                x = x1 + i * deltaX
                if y not in mapa:
                    mapa[y] = defaultdict(int)
                mapa[y][x] += 1
    res = 0
    for value in mapa.values():
        for num in value.values():
            if num > 1:
                res += 1
    return res


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
