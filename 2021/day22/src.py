import timeit


def check_big(riadok):
    for i in [0, 1, 2]:
        for j in [0, 1]:
            if not (-50 < riadok[i][j] < 50):
                return True
    return False


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for nr, line in enumerate(f):
            line = line.strip()
            line = line.split()
            coords = line[1].split(",")
            switch = line[0]
            riadok = []
            for coord in coords:
                coord = coord.split("=")[1]
                coord = coord.split("..")
                riadok.append((int(coord[0]), int(coord[1])))
            res.append((switch, riadok))
    return res


def solve_pt1():
    data = load_input()
    res = set()
    for switch, riadok in data:
        if check_big(riadok):
            continue
        for i in range(riadok[0][0], riadok[0][1] + 1):
            for j in range(riadok[1][0], riadok[1][1] + 1):
                for k in range(riadok[2][0], riadok[2][1] + 1):
                    if switch == "on":
                        res.add((i, j, k))
                    else:
                        res.discard((i, j, k))
    return len(res)


def solve_pt2():
    data = load_input()
    pass



start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Total time pt1: {(end - start):.3f} sec")
#
# start = timeit.default_timer()
# result2 = solve_pt2()
# end = timeit.default_timer()
# print(result2)
# print(f"Total time pt2: {(end - start):.3f} sec")
