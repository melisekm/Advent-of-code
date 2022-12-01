import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        tmp = []
        for line in f:
            if line == "\n":
                res.append(tmp)
                tmp = []
            else:
                tmp.append(int(line.strip()))
        res.append(tmp)
    return res


def solve_pt1():
    return max(map(sum, load_input()))


def solve_pt2():
    return sum(sorted(map(sum, load_input()), reverse=True)[:3])



def run_part(solve_fn, part_idx):
    start = timeit.default_timer()
    result = solve_fn()
    end = timeit.default_timer()
    print(result)
    print(f"Total time pt{part_idx}: {(end - start):.3f} sec")


run_part(solve_pt1, 1)
run_part(solve_pt2, 2)
