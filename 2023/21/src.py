from utils import aoc_part


def load_input(file_name="in.txt"):
    walls = set()
    with open(file_name) as f:
        lines = f.read().splitlines()
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char == "#":
                    walls.add((r, c))
                if char == 'S':
                    start = (r, c)
    return walls, start


def do_step(position, walls):
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    new_positions = set()
    for direction in directions:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if new_position not in walls:
            new_positions.add(new_position)
    return new_positions


@aoc_part(1)
def solve_pt1():
    walls, start = load_input()
    positions = {start}
    for _ in range(64):
        new_positions = set()
        for position in positions:
            new_positions.update(do_step(position, walls))
        positions = new_positions
    return len(positions)


#
# @aoc_part(2)
# def solve_pt2():
#     data = load_input()
#
#     pass


solve_pt1()
# solve_pt2()
