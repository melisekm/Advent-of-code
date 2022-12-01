def solve_pt1(vstup):
    def search(key, content, hladam, slovnik):
        if len(slovnik[key]) == 0:
            return False
        if hladam in content:
            return True
        for bag in content:
            if search(bag, slovnik[bag], hladam, slovnik):
                return True
        return False

    def spocitaj(slovnik):
        pocet = 0
        hladam = "shiny gold"
        for key, value in slovnik.items():
            if search(key, value, hladam, slovnik):
                pocet += 1
        return pocet

    def get_farby(info):
        data = []
        for i in range(0, len(info) - 3, 4):
            if info[i] == "no":
                break
            data.append(info[i + 1] + " " + info[i + 2])
        return data

    slovnik = {}
    with open(vstup, "r") as file:
        for line in file:
            info = line.strip().split(" ")
            nazov = info[0] + " " + info[1]
            slovnik[nazov] = get_farby(info[4:])
    return spocitaj(slovnik)


def solve_pt2(vstup):
    def get_farby(info):
        data = []
        for i in range(0, len(info) - 3, 4):
            if info[i] == "no":
                break
            data.append([info[i], info[i + 1] + " " + info[i + 2]])
        return data

    def search(key, content, slovnik):
        if len(slovnik[key]) == 0:
            return 0
        pocet = 0
        for velkost, bag in content:
            pocet += int(velkost) + int(velkost) * search(bag, slovnik[bag], slovnik)
        return pocet

    def spocitaj(slovnik):
        pocet = 0
        moj = "shiny gold"
        pocet += search(moj, slovnik[moj], slovnik)
        return pocet

    slovnik = {}
    with open(vstup, "r") as file:
        for line in file:
            info = line.strip().split(" ")
            nazov = info[0] + " " + info[1]
            slovnik[nazov] = get_farby(info[4:])
    return spocitaj(slovnik)


vstup = "vstup.txt"
result1 = solve_pt1(vstup)
result2 = solve_pt2(vstup)
print(result1)
print(result2)
