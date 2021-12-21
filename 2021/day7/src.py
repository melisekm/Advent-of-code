import timeit


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        for line in f:
            return list(map(int, line.strip().split(",")))


def solve_pt1():
    positions = load_input()
    best = None
    for pos in positions:
        cost = 0
        for p in positions:
            cost += abs(p - pos)
        if not best or cost < best:
            best = cost
    return best


def solve_pt2():
    positions = load_input()
    best = None
    for pos in range(max(positions)):
        cost = 0
        for p in positions:
            n = abs(p - pos) + 1
            cost += (n * (n - 1)) // 2
        if not best or cost < best:
            best = cost
    return best


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
