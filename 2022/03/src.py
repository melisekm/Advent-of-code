import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            res.append(line.strip())
    return res


def solve_pt1():
    data = load_input()
    total = 0
    for rucksack in data:
        first = set(rucksack[:len(rucksack) // 2])
        second = set(rucksack[len(rucksack) // 2:])
        common = list((first & second))[0]
        if common.isupper():
            common = ord(common) - ord('A') + 26 + 1
        else:
            common = ord(common) - ord('a') + 1
        total += common

    return total


def solve_pt2():
    data = load_input()
    last = None
    common = None
    total = 0
    for idx, rucksack in enumerate(data):
        if idx % 3 == 0:
            common = None
        elif common:
            common = list(set("".join(list(common))) & set(rucksack))[0]
            if common.isupper():
                total += ord(common) - ord('A') + 26 + 1
            else:
                total += ord(common) - ord('a') + 1
        elif last:
            common = set(rucksack) & set(last)
        last = rucksack

    return total


def run_part(solve_fn, part_idx):
    start = timeit.default_timer()
    result = solve_fn()
    end = timeit.default_timer()
    print(result)
    print(f"Total time pt{part_idx}: {(end - start):.3f} sec")


run_part(solve_pt1, 1)
run_part(solve_pt2, 2)
