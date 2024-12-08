import itertools
from collections import defaultdict

from utils import aoc_part


def shortest_path_with_directions(start, end):
    x1, y1 = start
    x2, y2 = end
    directions = []

    # Move horizontally towards the target
    while x1 != x2:
        dx = 1 if x1 < x2 else -1  # Determine direction in x-axis
        x1 += dx
        directions.append((dx, 0))

    # Move vertically towards the target
    while y1 != y2:
        dy = 1 if y1 < y2 else -1  # Determine direction in y-axis
        y1 += dy
        directions.append((0, dy))

    return directions


def load_input(file_name="in.txt"):
    positions = defaultdict(list)
    R = C = 0
    with open(file_name) as f:
        for idx, line in enumerate(f):
            C = len(line)
            for jdx, char in enumerate(line.strip()):
                if char != '.':
                    positions[char].append((idx, jdx))
            R += 1
    return positions, R, C


def calculate_new_point(point, directions, R, C):
    r, c = point
    for (dir_r, dir_c) in directions:
        r += dir_r
        c += dir_c
    res = (r, c)
    if res[0] < 0 or res[0] >= R:
        raise ValueError(res)
    if res[1] < 0 or res[1] >= C:
        raise ValueError(res)
    return res


def solve(p2=False):
    data, R, C = load_input()
    seen = set()
    for v in data.values():
        for (start, end) in itertools.combinations(v, 2):
            if p2:
                # in p2 the points are always included for some reason
                seen.add(start)
                seen.add(end)
            directions_S_E = shortest_path_with_directions(start, end)
            directions_E_S = shortest_path_with_directions(end, start)
            search1 = search2 = True  # whether to execute the search
            while search1 or search2:
                if search1:
                    try:
                        new_point_S_E = calculate_new_point(start, directions_E_S, R, C)
                        if new_point_S_E not in seen:
                            seen.add(new_point_S_E)
                        # in p2, the next point becomes the origin
                        start = new_point_S_E
                    except ValueError:
                        search1 = False
                if search2:
                    try:
                        new_point_E_S = calculate_new_point(end, directions_S_E, R, C)
                        if new_point_E_S not in seen:
                            seen.add(new_point_E_S)
                        end = new_point_E_S
                    except ValueError:
                        search2 = False
                if not p2:
                    # if its not p2 we do not continue with search
                    search1 = search2 = False
    return len(seen)


@aoc_part(1)
def solve_pt1():
    return solve()


@aoc_part(2)
def solve_pt2():
    return solve(p2=True)


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
