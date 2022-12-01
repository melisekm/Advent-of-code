import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            res.append(line.strip())
    return res


def solve_pt1():
    data = load_input()

    pass


def solve_pt2():
    data = load_input()

    pass


def run_part(solve_fn, part_idx):
    start = timeit.default_timer()
    result = solve_fn()
    end = timeit.default_timer()
    print(result)
    print(f"Total time pt{part_idx}: {(end - start):.3f} sec")


run_part(solve_pt1, 1)

# run_part(solve_pt2, 2)
