import timeit


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        for line in f:
            return list(map(int, line.strip().split(",")))


def solve_pt1():
    fishes = load_input()
    for _ in range(80):
        for i, fish in enumerate(fishes[:]):
            fishes[i] -= 1
            if fish == 0:
                fishes.append(8)
                fishes[i] = 6
    return len(fishes)


def solve_pt2():
    def load_dict(file_name="in.txt"):
        res = {}
        for day in range(9):
            res[day] = 0
        with open(file_name) as f:
            for line in f:
                line = line.strip().split(",")
                for timer in line:
                    res[int(timer)] += 1
        return res

    fishes = load_dict()
    for _ in range(256):
        zeros = fishes[0]
        for i in range(len(fishes) - 1):
            fishes[i] = fishes[i + 1]
        fishes[6] += zeros
        fishes[8] = zeros
    pocet = 0
    for v in fishes.values():
        pocet += v
    return pocet


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Cas vykonavania pt1:{end - start} sec")

start = timeit.default_timer()
result2 = solve_pt2()
end = timeit.default_timer()
print(result2)
print(f"Cas vykonavania pt2:{end - start} sec")
