import timeit


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        return f.readlines()


def solve_pt1():
    f = load_input()
    d = 0
    h = 0
    for line in f:
        course = line.strip().split()
        cmd = course[0]
        val = int(course[1])
        if cmd == "forward":
            h += val
        elif cmd == "down":
            d += val
        elif cmd == "up":
            d -= val
    return d * h


def solve_pt2():
    f = load_input()
    d = 0
    h = 0
    a = 0
    for line in f:
        course = line.strip().split()
        cmd = course[0]
        val = int(course[1])
        if cmd == "forward":
            h += val
            d += a * val
        elif cmd == "down":
            a += val
        elif cmd == "up":
            a -= val
    return d * h


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
