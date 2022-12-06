import timeit


def solve(length):
    data = open("in.txt").read().strip()
    for i in range(length, len(data)):
        if len(set(data[i - length:i])) == length:
            return i


def solve_pt1():
    return solve(4)


def solve_pt2():
    return solve(14)


def run_part(solve_fn, part_idx):
    start = timeit.default_timer()
    result = solve_fn()
    end = timeit.default_timer()
    print(result)
    print(f"Total time pt{part_idx}: {(end - start):.3f} sec")


run_part(solve_pt1, 1)
run_part(solve_pt2, 2)
