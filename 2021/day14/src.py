import timeit
from collections import Counter
from collections import defaultdict


def load_input(file_name="in.txt"):
    rules = {}
    with open(file_name) as f:
        for i, line in enumerate(f):
            if i == 0:
                init = [list(x) for x in line.strip()]
            if i > 1:
                line = line.strip().split(" -> ")
                rules[tuple(line[0])] = line[1]
    return init, rules


def solve_pt1():
    polymer, rules = load_input()
    for _ in range(10):
        for i, s in enumerate(polymer[:-1]):
            s[0] += rules[(polymer[i][0], polymer[i + 1][0])]
        polymer = [list(symbol) for row in polymer for symbols in row for symbol in symbols]
        print(_)
    C = Counter("".join([symbol for row in polymer for symbol in row]))
    return C.most_common(1)[0][1] - C.most_common()[-1][1]


def solve_pt2():
    polymer, rules = load_input()
    pairs = defaultdict(int)
    for i, s in enumerate(polymer[:-1]):
        pairs[("".join(polymer[i]) + "".join(polymer[i + 1]))] += 1
    C = Counter("".join([symbol for row in polymer for symbol in row]))
    for _ in range(40):
        new_pairs = defaultdict(int)
        for pair, pocet in pairs.items():
            symbol = rules[(pair[0], pair[1])]
            C[symbol] += pocet
            new_pairs[pair[0] + symbol] += pocet
            new_pairs[symbol + pair[1]] += pocet
        pairs = new_pairs
    return C.most_common(1)[0][1] - C.most_common()[-1][1]


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Total time pt1: {(end - start):.3f} sec")

start = timeit.default_timer()
result2 = solve_pt2()
end = timeit.default_timer()
print(result2)
print(f"Total time pt2: {(end - start):.3f} sec")
