def histogram1(lines):
    slovnik = set()
    for line in lines:
        for znak in line:
            slovnik.add(znak)
    return len(slovnik)


def solve_pt1(vstup):
    with open(vstup, "r") as file:
        arr = []
        pocet = 0
        while True:
            line = file.readline()
            if line == "\n" or not line:
                hodnota = histogram1(arr)
                if hodnota:
                    pocet += hodnota
                arr = []
            else:
                arr.append(line.strip())
            if not line:
                break
        return pocet


def histogram2(lines):
    slovnik = {}
    for line in lines:
        for znak in line:
            if znak in slovnik:
                slovnik[znak] += 1
            else:
                slovnik[znak] = 1

    res = 0
    for value in slovnik.values():
        if value == len(lines):
            res += 1
    return res


def solve_pt2(vstup):
    with open(vstup, "r") as file:
        arr = []
        pocet = 0
        while True:
            line = file.readline()
            if line == "\n" or not line:
                hodnota = histogram2(arr)
                if hodnota:
                    pocet += hodnota
                arr = []
            else:
                arr.append(line.strip())
            if not line:
                break
        return pocet


vstup = "vstup.txt"
result1 = solve_pt1(vstup)
result2 = solve_pt2(vstup)
print(result1)
print(result2)
