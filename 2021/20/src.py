import timeit


def load_input(file_name="in.txt"):
    algo = []
    mapa = []
    with open(file_name) as f:
        lines = f.readlines()
        nl = lines.index("\n")
        for line in lines[:nl]:
            line = line.strip()
            for symbol in line:
                algo.append(symbol)
        for line in lines[nl + 1:]:
            line = line.strip()
            mapa.append(line)

    return algo, mapa


def run_algo(data, algo, BOUNDARY, R, C, pnt):
    new_map = {}
    for i in range(-BOUNDARY, R + BOUNDARY):
        for j in range(-BOUNDARY, C + BOUNDARY):
            binary_number = ""
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    point = (i + dr, j + dc)
                    point_symbol = data.get(point, pnt)
                    if point_symbol == "#":
                        binary_number += "1"
                    else:
                        binary_number += "0"
            idx = int(binary_number, 2)
            new_map[(i, j)] = algo[idx]
    return new_map


def solve_pt1():
    algo, mapa = load_input()
    data = {}
    for i, row in enumerate(mapa):
        for j, symbol in enumerate(row):
            data[(i, j)] = symbol

    data = run_algo(data, algo, 2, len(mapa), len(mapa[0]), ".")
    data = run_algo(data, algo, 2, len(mapa), len(mapa[0]), "#")

    res = 0
    for k, v in data.items():
        if v == "#":
            res += 1

    return res


def solve_pt2():
    algo, mapa = load_input()
    data = {}
    for i, row in enumerate(mapa):
        for j, symbol in enumerate(row):
            data[(i, j)] = symbol

    onoff = [".", "#"]
    for i in range(50):
        data = run_algo(data, algo, 2 + i, len(mapa), len(mapa[0]), onoff[i % 2])

    res = 0
    for k, v in data.items():
        if v == "#":
            res += 1

    return res


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
