def vypocitaj(boarding_pass, lower, upper, character):
    cislo = lower
    total = upper
    for znak in boarding_pass:
        total //= 2
        if znak == character:
            cislo += total + 1
    return cislo


def get_id(boarding_pass):
    row = vypocitaj(boarding_pass[:-3], 0, 127, "B")
    column = vypocitaj(boarding_pass[-3:], 0, 7, "R")
    return row * 8 + column


def solve_pt1(vstup):
    arr = []
    with open(vstup, "r") as file:
        for line in file:
            boarding_pass = line.strip()
            idx = get_id(boarding_pass)
            arr.append(idx)
    return arr, max(arr)


def solve_pt2(zoznam):
    zoznam.sort()
    for i in range(len(zoznam) - 1):
        if zoznam[i + 1] != zoznam[i] + 1:
            break
    return zoznam[i] + 1


vstup = "vstup.txt"
zoznam, result1 = solve_pt1(vstup)
result2 = solve_pt2(zoznam)
print(result1)
print(result2)
