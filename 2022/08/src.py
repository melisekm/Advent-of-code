import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            tmp = []
            for char in line.strip():
                tmp.append(int(char))
            res.append(tmp)
    return res


def is_visible(max_range, i_mult, j_mult, i, j, data):
    for k in range(1, max_range):
        if data[i + (k * i_mult)][j + (k * j_mult)] >= data[i][j]:
            return False
    return True


def solve_pt1():
    total = 0
    data = load_input()
    C = len(data)
    R = len(data[0])
    for i in range(C):
        if i == 0 or i == len(data) - 1:
            total += C
            continue
        for j in range(R):
            if j == 0 or j == C - 1:
                total += 1
                continue
            # LEFT or RIGHT or UP or DOWN
            total += is_visible(j + 1, 0, -1, i, j, data) or is_visible(C - j, 0, 1, i, j, data) or \
                     is_visible(i + 1, -1, 0, i, j, data) or is_visible(C - i, 1, 0, i, j, data)
    return total


def can_see_trees(max_range, i_mult, j_mult, i, j, data):
    trees = 0
    for k in range(1, max_range):
        trees += 1
        if data[i + (k * i_mult)][j + (k * j_mult)] >= data[i][j]:
            break
    return trees


def solve_pt2():
    data = load_input()
    total_max = 0
    C = len(data)
    R = len(data[0])
    for i in range(C):
        if i == 0 or i == len(data) - 1:
            continue
        for j in range(R):
            if j == 0 or j == C - 1:
                continue
            # LEFT or RIGHT or UP or DOWN
            scenic_score = can_see_trees(j + 1, 0, -1, i, j, data) * can_see_trees(C - j, 0, 1, i, j, data) * \
                           can_see_trees(i + 1, -1, 0, i, j, data) * can_see_trees(C - i, 1, 0, i, j, data)
            total_max = max(total_max, scenic_score)
    return total_max


def run_part(solve_fn, part_idx):
    start = timeit.default_timer()
    result = solve_fn()
    end = timeit.default_timer()
    print(result)
    print(f"Total time pt{part_idx}: {(end - start):.3f} sec")


run_part(solve_pt1, 1)
run_part(solve_pt2, 2)
