import timeit


def load_input(file_name="in.txt"):
    vpravo = set()
    dolu = set()
    R = 0
    C = 0
    with open(file_name) as f:
        for r, line in enumerate(f):
            line = line.strip()
            R += 1
            C = 0
            for c, symbol in enumerate(line):
                C += 1
                if symbol == "v":
                    dolu.add((r, c))
                elif symbol == ">":
                    vpravo.add((r, c))
    return vpravo, dolu, R, C


def move_vpravo(east, vpravo, dolu, C):
    next_move = (east[0], 0 if east[1] + 1 >= C else east[1] + 1)
    if next_move in vpravo or next_move in dolu:
        return None
    return next_move


def move_dolu(south, vpravo, dolu, R):
    next_move = (0 if south[0] + 1 >= R else south[0] + 1, south[1])
    if next_move in vpravo or next_move in dolu:
        return None
    return next_move


def show(vpravo, dolu, R, C):
    for i in range(R):
        for j in range(C):
            if (i, j) in vpravo:
                print(">", end="")
            elif (i, j) in dolu:
                print("v", end="")
            else:
                print(".", end="")
        print("")


def solve_pt1():
    vpravo, dolu, R, C = load_input()
    res = 0
    while True:
        res += 1
        vpravo_moves = 0
        kopia_vpravo = list(vpravo)
        for east in kopia_vpravo:
            next_move = move_vpravo(east, kopia_vpravo, dolu, C)
            if next_move:
                vpravo.discard((east[0], east[1]))
                vpravo.add(next_move)
                vpravo_moves += 1
        dolu_moves = 0
        kopia_dolu = list(dolu)
        for south in kopia_dolu:
            next_move = move_dolu(south, vpravo, kopia_dolu, R)
            if next_move:
                dolu.discard((south[0], south[1]))
                dolu.add(next_move)
                dolu_moves += 1
        if dolu_moves == 0 and vpravo_moves == 0:
            return res
        print(res)


def solve_pt2():
    data = load_input()

    pass


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Total time pt1: {(end - start):.3f} sec")

# start = timeit.default_timer()
# result2 = solve_pt2()
# end = timeit.default_timer()
# print(result2)
# print(f"Total time pt2: {(end - start):.3f} sec")
