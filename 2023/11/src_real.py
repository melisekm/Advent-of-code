from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            res.append(line.strip())
    res = [list(x) for x in res]
    rows_with_dots = [idx for idx, R in enumerate(list(res)) if all(x == '.' for x in R)]
    columns_with_dots = [idx for idx, C in enumerate(res[0]) if all(x == '.' for x in [R[idx] for R in res])]
    galaxy_positions = [(idx, jdx) for idx, R in enumerate(res) for jdx, C in enumerate(R) if C == '#']
    return res, galaxy_positions, rows_with_dots, columns_with_dots


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def galaxy_expand(source, target, rows_with_dots, columns_with_dots, expand_value):
    return sum(
        expand_value - 1
        for rows_with_dots_idx in rows_with_dots
        if source[0] <= rows_with_dots_idx <= target[0] or target[0] <= rows_with_dots_idx <= source[0]
    ) + sum(
        expand_value - 1
        for columns_with_dots_idx in columns_with_dots
        if source[1] <= columns_with_dots_idx <= target[1] or target[1] <= columns_with_dots_idx <= source[1]
    )


def solve(expand_value):
    data, galaxy_positions, rows_with_dots, columns_with_dots = load_input()
    return sum(
        dist(source, target) + galaxy_expand(source, target, rows_with_dots, columns_with_dots, expand_value)
        for idx, source in enumerate(galaxy_positions)
        for target in galaxy_positions[idx + 1:]
    )


@aoc_part(1)
def solve_pt1():
    return solve(2)


@aoc_part(1)
def solve_pt2():
    return solve(1000000)


solve_pt1()
solve_pt2()
