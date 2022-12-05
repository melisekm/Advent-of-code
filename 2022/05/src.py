import timeit
import re


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            numbers = re.findall(r'\d+', line)
            res.append(map(int, numbers))
    return res


def load_stacks():
    return [
        'vcdrzgbw', 'gwfcbstv', 'cbsnw', 'qgmnjvcp', 'tslfdhb', 'jvtwmn', 'pflcstg', 'bdz', 'mnzw'
    ]


def solve(pt):
    data = load_stacks()
    movements = load_input()
    for how_many, fromm, to in movements:
        fromm -= 1
        to -= 1
        # string.pop() based on how many should be popped
        data[fromm], result = data[fromm][:-how_many], data[fromm][-how_many:]
        # reverse it if part 1 else same ordering
        data[to] += result[::-1] if pt == 1 else result
    return "".join(string[-1].upper() for string in data)


def solve_pt1():
    return solve(1)


def solve_pt2():
    return solve(2)


def run_part(solve_fn, part_idx):
    start = timeit.default_timer()
    result = solve_fn()
    end = timeit.default_timer()
    print(result)
    print(f"Total time pt{part_idx}: {(end - start):.3f} sec")


run_part(solve_pt1, 1)
run_part(solve_pt2, 2)
