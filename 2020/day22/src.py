import timeit
import copy


def solve_pt1(vstup):
    with open(vstup, "r") as file:
        p1 = []
        p2 = []
        k = []
        for line in file:
            if "Player" in line:
                p1 = copy.deepcopy(k)
                continue
            else:
                k.append(int(line.strip()))
        p2 = copy.deepcopy(k)

    return 0


vstup = "day22/vstup.txt"

start = timeit.default_timer()
result1 = solve_pt1(vstup)
print(result1)
print(f"Cas vykonavania pt1:{timeit.default_timer() - start} sec")

"""
start = timeit.default_timer()
result2 = solve_pt2(vstup)
print(result2)
print(f"Cas vykonavania pt2:{timeit.default_timer() - start} sec")
"""
