import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            res.append(line.strip())
    return res


idxs = []

mapa = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<"
}


def solve_pt1():
    skore = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    data = load_input()
    res = 0
    for line in data:
        stack = []
        for symbol in line:
            if symbol in mapa.keys():
                if stack[-1] == mapa[symbol]:
                    stack.pop(-1)
                else:
                    res += skore[symbol]
                    idxs.append(line)
                    break
            else:
                stack.append(symbol)
    return res


def solve_pt2():
    skore = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4
    }

    data = load_input()
    for idx in idxs:
        data.remove(idx)
    res = []
    for line in data:
        stack = []
        for symbol in line:
            if symbol in mapa.keys():
                if stack[-1] == mapa[symbol]:
                    stack.pop(-1)
            else:
                stack.append(symbol)
        medzi = 0
        for symbol in stack[::-1]:
            medzi *= 5
            medzi += skore[symbol]
        res.append(medzi)
    return sorted(res)[len(res) // 2]


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
