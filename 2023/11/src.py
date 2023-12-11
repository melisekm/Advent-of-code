from concurrent.futures import ProcessPoolExecutor, as_completed

import numpy as np
from tqdm import tqdm

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            res.append(line)
    res = [list(x) for x in res]

    rows_with_dots = []
    for idx, R in enumerate(list(res)):
        if all(x == '.' for x in R):
            rows_with_dots.append(idx)

    columns_with_dots = []
    for idx, C in enumerate(res[0]):
        if all(x == '.' for x in [R[idx] for R in res]):
            columns_with_dots.append(idx)

    galaxy_positions = []
    for idx, R in enumerate(res):
        for jdx, C in enumerate(R):
            if C == '#':
                galaxy_positions.append((idx, jdx))

    return res, galaxy_positions, rows_with_dots, columns_with_dots


# up down left or right
def get_adjacent(data, node):
    res = []
    if node[0] - 1 >= 0:
        res.append((node[0] - 1, node[1]))
    if node[0] + 1 < len(data):
        res.append((node[0] + 1, node[1]))
    if node[1] - 1 >= 0:
        res.append((node[0], node[1] - 1))
    if node[1] + 1 < len(data[0]):
        res.append((node[0], node[1] + 1))
    return res


def bfs(data, source, target):
    visited = set()
    queue = [[source]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == target:
            return path
        elif node not in visited:
            for adjacent in get_adjacent(data, node):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
            visited.add(node)
    return []


@aoc_part(1)
def solve_pt1():
    data, galaxy_positions, rows_with_dots, columns_with_dots = load_input()
    total_length = 0
    pbar = tqdm(enumerate(galaxy_positions), position=0, total=len(galaxy_positions), desc=total_length, disable=False)
    for x in pbar:
        idx, source = x
        for target in tqdm(galaxy_positions[idx + 1:], position=1, leave=False, disable=True):
            path = bfs(data, source, target)
            total_length += len(path) - 1

            for idx, rows_with_dots_idx in enumerate(rows_with_dots):
                for p in path:
                    if p[0] == rows_with_dots_idx:
                        total_length += 2 - 1
            for idx, columns_with_dots_idx in enumerate(columns_with_dots):
                for p in path:
                    if p[1] == columns_with_dots_idx:
                        total_length += 2 - 1

        pbar.set_postfix({'total_length': total_length})
    return total_length


def generic_parallel_execution(func, data, *fn_args, workers=4, add_pbar=False, **fn_kwargs):
    space = np.linspace(0, len(data), workers + 1, dtype=int)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = set()
        for i in range(workers):
            if add_pbar:
                fn_kwargs["pbar_position"] = i
            future = executor.submit(func, data[space[i]: space[i + 1]], *fn_args, **fn_kwargs)
            print(f"Starting worker {future}")
            futures.add(future)

    results = []
    for future in as_completed(futures):
        try:
            results.append(future.result())
        except Exception as e:
            print(f"{future} generated an exception: {e}")
        else:
            print(f"Joining worker {future}")
    return results


def run(galaxy_positions, galaxy_positions_all, data, rows_with_dots, columns_with_dots, universe_size, pbar_position):
    path_values = {}
    pbar = tqdm(enumerate(galaxy_positions), position=pbar_position, total=len(galaxy_positions), disable=False)
    for x in pbar:
        idx, source = x
        for target in galaxy_positions_all:
            path = bfs(data, source, target)
            path_length = len(path) - 1
            for R, C in path:
                if R in rows_with_dots:
                    path_length += universe_size - 1
                if C in columns_with_dots:
                    path_length += universe_size - 1
            path_values[(source, target)] = path_length

    return path_values


@aoc_part(2)
def solve_pt2():
    data, galaxy_positions, rows_with_dots, columns_with_dots = load_input(file_name="in2.txt")
    universe_size = 1000000
    res = generic_parallel_execution(run, galaxy_positions, galaxy_positions, data,
                                     set(rows_with_dots), set(columns_with_dots),
                                     universe_size, workers=6, add_pbar=True)
    all_paths = set()
    out = 0
    for r in res:
        for k, v in r.items():
            if (k[1], k[0]) not in all_paths and (k[0], k[1]) not in all_paths:
                all_paths.add(k)
                out += v
    return out


if __name__ == '__main__':
    # solve_pt1()
    solve_pt2()
