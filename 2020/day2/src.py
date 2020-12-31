def valid1(_range, pismeno, string):
    pocet = string.count(pismeno)
    if _range[0] <= pocet <= _range[1]:
        return True
    return False


def solve_pt1(vstup):
    pocet = 0
    with open(vstup, "r") as file:
        for line in file:
            stlpec = line.strip().split(" ")
            _range = list(map(int, stlpec[0].split("-")))
            pismeno = stlpec[1][0]
            string = stlpec[2]
            if valid1(_range, pismeno, string):
                pocet += 1
    return pocet


def valid2(loc, pismeno, string):
    if (
        string[loc[0] - 1] == pismeno
        and string[loc[1] - 1] != pismeno
        or string[loc[0] - 1] != pismeno
        and string[loc[1] - 1] == pismeno
    ):
        return True
    return False


def solve_pt2(vstup):
    pocet = 0
    with open(vstup, "r") as file:
        for line in file:
            stlpec = line.strip().split(" ")
            _range = list(map(int, stlpec[0].split("-")))
            pismeno = stlpec[1][0]
            string = stlpec[2]
            if valid2(_range, pismeno, string):
                pocet += 1
    return pocet


vstup = "vstup.txt"
result1 = solve_pt1(vstup)
result2 = solve_pt2(vstup)
print(result1, result2)
