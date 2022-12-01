import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            s = []
            for symbol in line:
                s.append({"val": int(symbol), "flashed": False})
            res.append(s)
    return res


def get_smery(i, j, mapa):
    hore = i - 1
    dole = i + 1
    vlavo = j - 1
    vpravo = j + 1
    vlavo_hore = [i - 1, j - 1]
    vpravo_hore = [i - 1, j + 1]
    vlavo_dole = [i + 1, j - 1]
    vpravo_dole = [i + 1, j + 1]
    smeryI = [hore, dole]
    smeryJ = [vlavo, vpravo]
    smeryIJ = [vlavo_hore, vpravo_hore]
    smeryJI = [vlavo_dole, vpravo_dole]
    if i == 0:
        smeryI.remove(hore)
        smeryIJ = []
    if j == 0:
        smeryJ.remove(vlavo)
        if smeryIJ:
            smeryIJ.remove(vlavo_hore)
        if smeryJI:
            smeryJI.remove(vlavo_dole)
    if i == len(mapa) - 1:
        smeryI.remove(dole)
        smeryJI = []
    if j == len(mapa[i]) - 1:
        smeryJ.remove(vpravo)
        if smeryIJ:
            smeryIJ.remove(vpravo_hore)
        if smeryJI:
            smeryJI.remove(vpravo_dole)

    return smeryI, smeryJ, smeryIJ, smeryJI


res = 0


def solve_pt1and2():
    def doit(i, j, symbol, mapa):
        if not mapa[i][j]["flashed"]:
            symbol["val"] += 1
            if symbol["val"] > 9:
                symbol["flashed"] = True
                global res
                res += 1
                symbol["val"] = 0
                poobzeraj_sa(i, j, mapa)

    def poobzeraj_sa(i, j, mapa):
        smeryI, smeryJ, smeryIJ, smeryJI = get_smery(i, j, mapa)

        for i_ in smeryI:
            doit(i_, j, mapa[i_][j], mapa)
        for j_ in smeryJ:
            doit(i, j_, mapa[i][j_], mapa)
        for el in smeryIJ + smeryJI:
            i_ = el[0]
            j_ = el[1]
            doit(i_, j_, mapa[i_][j_], mapa)

    mapa = load_input()
    step = 0
    p2 = None
    while True:
        step += 1
        for i, line in enumerate(mapa):
            for j, symbol in enumerate(line):
                doit(i, j, symbol, mapa)

        yep = True
        for i, line in enumerate(mapa):
            for j, symbol in enumerate(line):
                if symbol["val"] != 0:
                    yep = False
                symbol["flashed"] = False
        if step == 100:
            global res
            print(res)
            if p2:
                return p2
        if yep:
            p2 = step
            if step > 100 and p2:
                return p2


start = timeit.default_timer()
result1 = solve_pt1and2()
end = timeit.default_timer()
print(result1)
print(f"Cas vykonavania pt1+pt2:{end - start} sec")
