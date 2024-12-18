from collections import defaultdict

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = defaultdict(lambda: ".")
    player = None
    with open(file_name) as f:
        data, moves = f.read().split("\n\n")
        for idx, line in enumerate(data.split("\n")):
            line = line.strip()
            for jdx, char in enumerate(line):
                if char == '@':
                    player = (idx, jdx)
                res[(idx, jdx)] = char
    return res, "".join(moves.replace("\n", '')), player, idx, jdx


move_map = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}


def switch(grid, a, b):
    grid[b], grid[a] = grid[a], grid[b]


def doit(grid: dict, player: tuple[int, int], move: tuple[int, int]):
    dy, dx = move
    new_pos = player[0] + dy, player[1] + dx
    if grid[new_pos] == '.':
        switch(grid, new_pos, player)
        return True
    elif grid[new_pos] == '#':
        return False
    elif grid[new_pos] == 'O':
        if doit(grid, new_pos, move):
            switch(grid, new_pos, player)
            return True
        else:
            return False


@aoc_part(1)
def solve_pt1():
    grid, moves, player, R, C = load_input()
    for idx, move in enumerate(moves):
        # print(idx, move)
        dy, dx = move_map[move]
        new_pos = player[0] + dy, player[1] + dx
        if doit(grid, player, move_map[move]):
            player = new_pos
        # for k, char in grid.items():
        #     y, x = k
        #     print(char, end='')
        #     if x == C:
        #         print("\n", end='')
        # print()

    res = 0
    for k, char in grid.items():
        y, x = k
        if char == 'O':
            res += 100 * y + x
    return res


def doit2(grid: dict, player: tuple[int, int], move: tuple[int, int]):
    dy, dx = move
    new_pos = player[0] + dy, player[1] + dx
    if grid[new_pos] == '.':
        switch(grid, new_pos, player)
        return True
    if grid[new_pos] == '#':
        return False

    if grid[new_pos] == 'O':
        if doit(grid, new_pos, move):
            switch(grid, new_pos, player)
            return True
        else:
            return False


@aoc_part(2)
def solve_pt2():
    grid, moves, player, R, C = load_input()
    for idx, move in enumerate(moves):
        # print(idx, move)
        dy, dx = move_map[move]
        new_pos = player[0] + dy, player[1] + dx
        if doit(grid, player, move_map[move]):
            player = new_pos
        # for k, char in grid.items():
        #     y, x = k
        #     print(char, end='')
        #     if x == C:
        #         print("\n", end='')
        # print()

    res = 0
    for k, char in grid.items():
        y, x = k
        if char == 'O':
            res += 100 * y + x
    return res

if __name__ == '__main__':
    solve_pt1()
    # solve_pt2()
