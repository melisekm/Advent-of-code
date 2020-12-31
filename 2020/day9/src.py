def solve_pt1(vstup):
    def check(arr, nove):
        tabulka = set()
        for cislo in arr:
            rozdiel = nove - cislo
            if rozdiel in tabulka:
                return True
            tabulka.add(cislo)
        return False

    arr = []
    preamble = 25
    with open(vstup, "r") as file:
        for _ in range(preamble):
            cislo = int(file.readline().strip())
            arr.append(cislo)
        while True:
            nove = int(file.readline().strip())
            ok = check(arr, nove)
            if not ok:
                return nove
            arr.append(nove)
            arr.pop(0)


def solve_pt2(vstup, hladane):
    def vyries(cisla, hladane):
        for idx, prve in enumerate(cisla):
            arr = [prve]
            for j, _ in enumerate(cisla, start=(idx + 1)):
                arr.append(cisla[j])
                suma = sum(arr)
                if suma == hladane:
                    return min(arr) + max(arr)
                if suma > hladane:
                    break

    arr = []
    with open(vstup, "r") as file:
        for line in file:
            arr.append(int(line.strip()))
    return vyries(arr, hladane)


vstup = "vstup.txt"
result1 = solve_pt1(vstup)
result2 = solve_pt2(vstup, result1)
print(result1)
print(result2)
