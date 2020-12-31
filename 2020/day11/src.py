import copy

################PT1##################
def solve_pt1(vstup):
    def najdi_susedov(mapa, row, column):
        pozicie = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        susedia = []
        for x, y in pozicie:
            x += column
            y += row
            if 0 <= y < len(mapa):
                if 0 <= x < len(mapa[0]):
                    susedia.append(mapa[y][x])
        return susedia

    def check(mapa, row, column, hladane):
        susedia = najdi_susedov(mapa, row, column)
        cntr = 0
        for sused in susedia:
            if sused == hladane:
                cntr += 1
        return cntr

    def vykonaj_zmenu(tmp_mapa, mapa, row, column):
        res = False
        if mapa[row][column] == "L":
            pocet = check(tmp_mapa, row, column, "#")
            if pocet == 0:
                res = "#"

        elif mapa[row][column] == "#":
            pocet = check(tmp_mapa, row, column, "#")
            if pocet >= 4:
                res = "L"
        if res:
            mapa[row][column] = res
        return res

    def spocitaj_volne(mapa):
        cntr = 0
        for row in mapa:
            for seat in row:
                if seat == "#":
                    cntr += 1
        return cntr

    def vyries(mapa_orig):
        mapa = []
        for i, row in enumerate(mapa_orig):
            mapa.append([])
            for seat in row:
                mapa[i].append(seat)
        while True:
            tmp_mapa = copy.deepcopy(mapa)
            flag = False
            for row, riadok in enumerate(mapa):
                for column, _ in enumerate(riadok):
                    zmena = vykonaj_zmenu(tmp_mapa, mapa, row, column)
                    if zmena:
                        flag = True
            if flag is False:
                return spocitaj_volne(mapa)

    with open(vstup, "r") as file:
        mapa = []
        for line in file:
            mapa.append(line.strip())

    return vyries(mapa)


################PT2##################
def solve_pt2(vstup):
    def najdi_v_smere(x, y, row, column, mapa):
        adj_x = column + x
        adj_y = row + y
        while 0 <= adj_y < len(mapa) and 0 <= adj_x < len(mapa[0]):
            if mapa[adj_y][adj_x] != ".":
                return mapa[adj_y][adj_x]
            adj_x += x
            adj_y += y
        return None

    def najdi_susedov(mapa, row, column):
        pozicie = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        susedia = []
        for x, y in pozicie:
            sused = najdi_v_smere(x, y, row, column, mapa)
            if sused:
                susedia.append(sused)
        return susedia

    def check(mapa, row, column, hladane):
        susedia = najdi_susedov(mapa, row, column)
        cntr = 0
        for sused in susedia:
            if sused == hladane:
                cntr += 1
        return cntr

    def vykonaj_zmenu(tmp_mapa, mapa, row, column):
        res = False
        if mapa[row][column] == "L":
            pocet = check(tmp_mapa, row, column, "#")
            if pocet == 0:
                res = "#"

        elif mapa[row][column] == "#":
            pocet = check(tmp_mapa, row, column, "#")
            if pocet >= 5:
                res = "L"
        if res:
            mapa[row][column] = res
        return res

    def spocitaj_volne(mapa):
        cntr = 0
        for row in mapa:
            for seat in row:
                if seat == "#":
                    cntr += 1
        return cntr

    def vyries(mapa_orig):
        mapa = []
        for i, row in enumerate(mapa_orig):
            mapa.append([])
            for seat in row:
                mapa[i].append(seat)
        while True:
            tmp_mapa = copy.deepcopy(mapa)
            flag = False
            for row, riadok in enumerate(mapa):
                for column, _ in enumerate(riadok):
                    zmena = vykonaj_zmenu(tmp_mapa, mapa, row, column)
                    if zmena:
                        flag = True
            if flag is False:
                return spocitaj_volne(mapa)

    with open(vstup, "r") as file:
        mapa = []
        for line in file:
            mapa.append(line.strip())

    return vyries(mapa)


vstup = "vstup.txt"
result1 = solve_pt1(vstup)
result2 = solve_pt2(vstup)
print(result1)
print(result2)
