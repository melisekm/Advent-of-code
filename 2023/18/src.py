import re

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip().split(" ")
            direction = line[0]
            value = int(line[1])
            code = re.sub(r"[()#]", "", line[2])
            res.append((direction, value, code))
    return res


def draw_maze(maze):
    min_maze = (min(maze, key=lambda x: x[0])[0], min(maze, key=lambda x: x[1])[1])
    max_maze = (max(maze, key=lambda x: x[0])[0], max(maze, key=lambda x: x[1])[1])
    real_maze = []
    for i in range(min_maze[0], max_maze[0] + 1):
        real_maze.append([])
        for j in range(min_maze[1], max_maze[1] + 1):
            real_maze[i + (min_maze[0]) * -1].append("#" if (i, j) in maze else ".")
    return real_maze


def flood_fill(grid, i=200, j=200, old_color=".", new_color="#"):
    stack = [(i, j)]
    while stack:
        i, j = stack.pop(0)
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            continue
        if grid[i][j] != old_color:
            continue
        grid[i][j] = new_color
        stack.append((i + 1, j))
        stack.append((i - 1, j))
        stack.append((i, j + 1))
        stack.append((i, j - 1))
    return grid


dir_map = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0)
}


@aoc_part(1)
def solve_pt1():
    data = load_input()
    maze = set()
    position = (0, 0)
    maze.add(position)
    for direction, value, _ in data:
        for i in range(value):
            position = (position[0] + dir_map[direction][0], position[1] + dir_map[direction][1])
            maze.add(position)

    real_maze = draw_maze(maze)
    res = flood_fill(real_maze)
    count = sum(res[i][j] == "#" for i in range(len(res)) for j in range(len(res[0])))
    return count


# @aoc_part(2)
# def solve_pt2():
#     data = load_input()
#
#     pass


solve_pt1()
# solve_pt2()
