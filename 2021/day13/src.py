import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        a = f.readlines()
        nl = a.index("\n")
        for line in a[:nl]:
            res.append(line.strip().split(","))
        rules = []
        for line in a[nl + 1:]:
            splitted = line.strip().split("=")
            axis = splitted[0][-1]
            rules.append((axis, int(splitted[1])))
    return res, rules


def solve_pt1():
    data, rules = load_input()
    mapa = {}
    for coord in data:
        x = int(coord[0])
        y = int(coord[1])
        if rules[0][0] == "y" and y > rules[0][1]:
            mapa[(x, abs(y - rules[0][1] * 2))] = "#"
        elif rules[0][0] == "x" and x > rules[0][1]:
            mapa[(abs(x - rules[0][1] * 2), y)] = "#"
        else:
            mapa[(x, y)] = "#"
    return len(mapa)


def solve_pt2():
    data, rules = load_input()
    mapa = set()
    minX = float('inf')
    minY = float('inf')

    for coord in data:
        x = int(coord[0])
        y = int(coord[1])
        mapa.add((x, y))

    for rule in rules:
        for x, y in list(mapa):
            if rule[0] == "y" and y > rule[1]:
                mapa.add((x, abs(y - rule[1] * 2)))
                mapa.remove((x, y))
                if minY > rule[1]:
                    minY = rule[1]
            elif rule[0] == "x" and x > rule[1]:
                mapa.add((abs(x - rule[1] * 2), y))
                mapa.remove((x, y))
                if minX > rule[1]:
                    minX = rule[1]

    for y in range(minY):
        for x in range(minX):
            if (x, y) in mapa:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print("\n", end="")


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Cas vykonavania pt1:{end - start} sec")

start = timeit.default_timer()
solve_pt2()
end = timeit.default_timer()
if end - start > 1:
    print(f"Cas vykonavania pt2:{end - start} sec")
else:
    print("Total time : %.1f ms" % (1000 * (end - start)))
