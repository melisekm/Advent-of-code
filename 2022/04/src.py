import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line_split = line.strip().split(",")
            line_tmp = []
            for elf in line_split:
                low, high = elf.split("-")
                line_tmp.append((int(low), int(high)))
            res.append(line_tmp)
    return res


def solve_pt1():
    data = load_input()
    total = 0
    for elf1, elf2 in data:
        low1, high1 = elf1
        low2, high2 = elf2
        if low1 <= low2 and high1 >= high2:
            total += 1
        elif low2 <= low1 and high2 >= high1:
            total += 1
    return total


def solve_pt2():
    data = load_input()
    total = 0
    for elf1, elf2 in data:
        low1, high1 = elf1
        low2, high2 = elf2
        if (low1 <= low2 <= high1) or (low2 <= low1 <= high2):
            total += 1
    return total


def run_part(solve_fn, part_idx):
    start = timeit.default_timer()
    result = solve_fn()
    end = timeit.default_timer()
    print(result)
    print(f"Total time pt{part_idx}: {(end - start):.3f} sec")


run_part(solve_pt1, 1)
run_part(solve_pt2, 2)
