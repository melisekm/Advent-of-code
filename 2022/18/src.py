from utils import aoc_part


def load_input(file_name="in.txt"):
    res = set()
    with open(file_name) as f:
        for line in f:
            x, y, z = line.strip().split(",")
            x, y, z = int(x) + 1, int(y) + 1, int(z) + 1  # add 1 to avoid not being able to reach edges
            res.add((x, y, z))
    return res


def generate_numbers(num):
    for i in range(3):  # iterate through the elements of the tuple
        for delta in [-1, 0, 1]:  # try decrementing, leaving unchanged, or incrementing the element
            new_num = num[:i] + (num[i] + delta,) + num[i + 1:]
            if new_num == num:
                continue
            yield new_num


@aoc_part(1)
def solve_pt1():
    data = load_input()
    total = 0
    for point in data:
        sides = 6
        for new_point in generate_numbers(point):
            if new_point in data:
                sides -= 1
        total += sides

    return total


GRID_SIZE = 25


def flood_fill_recursion(grid3d, i, j, k, old_color, new_color):
    if i < 0 or i >= GRID_SIZE or j < 0 or j >= GRID_SIZE or k < 0 or k >= GRID_SIZE:
        return
    if grid3d[i][j][k] != old_color:
        return
    grid3d[i][j][k] = new_color
    flood_fill_recursion(grid3d, i + 1, j, k, old_color, new_color)
    flood_fill_recursion(grid3d, i - 1, j, k, old_color, new_color)
    flood_fill_recursion(grid3d, i, j + 1, k, old_color, new_color)
    flood_fill_recursion(grid3d, i, j - 1, k, old_color, new_color)
    flood_fill_recursion(grid3d, i, j, k + 1, old_color, new_color)
    flood_fill_recursion(grid3d, i, j, k - 1, old_color, new_color)


def flood_fill(grid3d, i, j, k, old_color, new_color):
    stack = [(i, j, k)]
    while stack:
        i, j, k = stack.pop(0)
        if i < 0 or i >= GRID_SIZE or j < 0 or j >= GRID_SIZE or k < 0 or k >= GRID_SIZE:
            continue
        if grid3d[i][j][k] != old_color:
            continue
        grid3d[i][j][k] = new_color
        stack.append((i + 1, j, k))
        stack.append((i - 1, j, k))
        stack.append((i, j + 1, k))
        stack.append((i, j - 1, k))
        stack.append((i, j, k + 1))
        stack.append((i, j, k - 1))


@aoc_part(2)
def solve_pt2():
    nodes = load_input()
    grid3d = [[['-' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for node in nodes:
        grid3d[node[0]][node[1]][node[2]] = "#"
    flood_fill(grid3d, 0, 0, 0, '-', 'a')

    total = 0
    for point in nodes:
        look_around = set(generate_numbers(point))
        for new_point in look_around:
            i, j, k = new_point
            if i < 0 or i >= GRID_SIZE or j < 0 or j >= GRID_SIZE or k < 0 or k >= GRID_SIZE:
                continue
            if grid3d[i][j][k] == 'a':
                total += 1
    return total


solve_pt1()
solve_pt2()
