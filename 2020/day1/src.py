def load_input(vstup):
    arr = []
    with open(vstup, "r") as file:
        for line in file:
            arr.append(line.strip())
    return list(map(int, arr))


def solve_pt1(vstup):
    dlzka = len(vstup)
    for idx, cislo in enumerate(vstup):
        for j in range(idx, dlzka):
            if cislo + vstup[j] == 2020:
                return cislo * vstup[j]


def solve_pt2(vstup):
    dlzka = len(vstup)
    for idx, cislo in enumerate(vstup):
        for j in range(idx, dlzka):
            for k in range(j, dlzka):
                if cislo + vstup[j] + vstup[k] == 2020:
                    return cislo * vstup[j] * vstup[k]


vstup = load_input("vstup.txt")
result1 = solve_pt1(vstup)
result2 = solve_pt2(vstup)
print(result1, result2)
