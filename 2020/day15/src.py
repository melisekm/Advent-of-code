import timeit


def solve_pt1(vstup):
    stop = 2020

    def vyries(cisla, stop, last_number):
        cntr = len(cisla)
        while cntr != stop:
            cntr += 1
            if cisla[last_number][0] is None:
                cisla[0] = [cisla[0][1], cntr]
                last_number = 0
            else:
                new_number = cisla[last_number][1] - cisla[last_number][0]
                if new_number in cisla:
                    cisla[new_number] = [cisla[new_number][1], cntr]
                else:
                    cisla[new_number] = [None, cntr]
                last_number = new_number
        return last_number

    with open(vstup, "r") as file:
        cisla = {}
        for line in file:
            data = list(map(int, line.strip().split(",")))
        for idx, cislo in enumerate(data):
            cisla[cislo] = [None, idx + 1]
    return vyries(cisla, stop, data[-1])


def solve_pt2(vstup):
    stop = 30000000

    def vyries(cisla, stop, last_number):
        cntr = len(cisla)
        while cntr != stop:
            cntr += 1
            if cisla[last_number][0] is None:
                cisla[0] = [cisla[0][1], cntr]
                last_number = 0
            else:
                last_number = cisla[last_number][1] - cisla[last_number][0]
                if last_number in cisla:
                    cisla[last_number] = [cisla[last_number][1], cntr]
                else:
                    cisla[last_number] = [None, cntr]
        return last_number

    with open(vstup, "r") as file:
        cisla = {}
        for line in file:
            data = list(map(int, line.strip().split(",")))
        for idx, cislo in enumerate(data):
            cisla[cislo] = [None, idx + 1]
    return vyries(cisla, stop, data[-1])


vstup = "vstup.txt"

start = timeit.default_timer()
result1 = solve_pt1(vstup)
print(result1)
print(f"Cas vykonavania pt1:{timeit.default_timer() - start} sec")


start = timeit.default_timer()
result2 = solve_pt2(vstup)
print(result2)
print(f"Cas vykonavania pt2:{timeit.default_timer() - start} sec")
