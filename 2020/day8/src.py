import copy


def solve_pt1(vstup):
    def spocitaj(instrukcie):
        navstivene = [0] * (len(instrukcie))
        acc = 0
        i = 0
        while navstivene[i] != 1:
            navstivene[i] = 1
            if instrukcie[i][0] == "acc":
                acc += int(instrukcie[i][1])
            if instrukcie[i][0] == "jmp":
                i += int(instrukcie[i][1])
            else:
                i += 1
        return acc

    arr = []
    with open(vstup, "r") as file:
        for line in file:
            data = line.strip().split(" ")
            arr.append([data[0], data[1]])

    return spocitaj(arr)


def solve_pt2(vstup):
    def run_code(instrukcie):
        dlzka = len(instrukcie)
        navstivene = [0] * (dlzka)
        acc = 0
        i = 0
        while True:
            navstivene[i] = 1
            if instrukcie[i][0] == "acc":
                acc += int(instrukcie[i][1])
            if instrukcie[i][0] == "jmp":
                i += int(instrukcie[i][1])
            else:
                i += 1

            if i >= dlzka:
                return acc
            if navstivene[i] == 1:
                return False

    def spocitaj(instrukcie):
        for i in range(len(instrukcie)):
            tmp = copy.deepcopy(instrukcie)
            if tmp[i][0] == "jmp":
                tmp[i][0] = "nop"
            elif tmp[i][0] == "nop":
                tmp[i][0] = "jmp"
            else:
                continue
            acc = run_code(tmp)
            if acc is not False:
                return acc

    arr = []
    with open(vstup, "r") as file:
        for line in file:
            data = line.strip().split(" ")
            arr.append([data[0], data[1]])

    return spocitaj(arr)


vstup = "vstup.txt"
result1 = solve_pt1(vstup)
result2 = solve_pt2(vstup)
print(result1)
print(result2)
