import timeit


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        return f.readlines()


def solve_pt1():
    f = load_input()
    res = 0
    prev = None
    for line in f:
        curr = int(line.strip())
        if prev is not None and curr > prev:
            res += 1
        prev = curr
    return res


def solve_pt2():
    f = load_input()
    first = []
    second = []
    prev = None
    res = 0
    for line in f:
        curr = int(line.strip())
        if prev:
            second.append(curr)
        if len(first) == 3:
            if sum(second) > sum(first):
                res += 1
            first.pop(0)
            second.pop(0)
        first.append(curr)
        prev = curr

    return res


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
