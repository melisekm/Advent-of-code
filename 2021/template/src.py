import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            res.append(line.strip())
    return res


def solve_pt1():
    f = load_input()
    for line in f:
        pass


def solve_pt2():
    f = load_input()
    for line in f:
        pass


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Cas vykonavania pt1:{end - start} sec")


# start = timeit.default_timer()
# result2 = solve_pt2()
# end = timeit.default_timer()
# print(result2)
# print(f"Cas vykonavania pt2:{end - start} sec")

