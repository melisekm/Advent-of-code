from collections import defaultdict

from utils import aoc_part

Position = tuple[int, int]
PositionsToSwap = tuple[Position, Position]


def make_p2(data: str):
    return (
        data
        .replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
    )


def load_input(file_name="in.txt", p2=False):
    res = defaultdict(lambda: ".")
    robot = None
    with open(file_name) as f:
        data, moves = f.read().split("\n\n")
        if p2:
            data = make_p2(data)
        for idx, line in enumerate(data.split("\n")):
            line = line.strip()
            for jdx, char in enumerate(line):
                if char == '@':
                    robot = (idx, jdx)
                res[(idx, jdx)] = char
    return res, "".join(moves.replace("\n", '')), robot


def attempt_to_move(grid: dict, thing: Position, move: Position, stack: list[PositionsToSwap], p2=False):
    if any(thing == x[0] for x in stack):
        # a force is being already applied, do not continue
        return
    new_pos = thing[0] + move[0], thing[1] + move[1]
    if grid[new_pos] == '#':
        # if at any point something cant be moved, stop
        raise ValueError
    if grid[new_pos] == '.':
        # we are at the end of recursion and can move it
        # add it to list of things being moved
        stack.append((thing, new_pos))
        return

    # apply force to the main side
    attempt_to_move(grid, new_pos, move, stack, p2)
    # unrolling recursion, we can move it if exception was not raised
    stack.append((thing, new_pos))
    if not p2:
        return

    if grid[new_pos] == ']':
        other_side_pos = (new_pos[0], new_pos[1] - 1)
    elif grid[new_pos] == '[':
        other_side_pos = (new_pos[0], new_pos[1] + 1)
    else:
        assert False
    # attempt to move other side too
    attempt_to_move(grid, other_side_pos, move, stack, p2)


def solve(char_to_find: str, p2=False):
    grid, moves, robot = load_input(p2=p2)
    move_map = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }

    for idx, move in enumerate(moves):
        dy, dx = move_map[move]
        new_pos = robot[0] + dy, robot[1] + dx
        stack = []
        try:
            attempt_to_move(grid, robot, move_map[move], stack, p2=p2)
            # do not move things multiple times, but keep list ordered
            for a, b in dict.fromkeys(stack):
                grid[b], grid[a] = grid[a], grid[b]
            robot = new_pos
        except ValueError:
            pass
    return sum(
        100 * y + x for (y, x), char in grid.items() if char == char_to_find
    )


@aoc_part(1)
def solve_pt1():
    return solve('O', p2=False)


@aoc_part(2)
def solve_pt2():
    return solve('[', p2=True)


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
