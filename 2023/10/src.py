from utils import aoc_part


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        res = f.read().splitlines()

    res.insert(0, '.' * len(res[0]))
    res.append('.' * len(res[0]))
    for idx, R in enumerate(res):
        res[idx] = '.' + R + '.'
    S = []
    for idx, R in enumerate(res):
        for jdx, C in enumerate(R):
            if C == 'S':
                S = [idx, jdx]

    return [list(x) for x in res], S


class DIRECTION:
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


class CHAR:
    VP: str = '|'
    HP: str = '-'
    NE: str = 'L'
    NW: str = 'J'
    SW: str = '7'
    SE: str = 'F'


cons = {
    CHAR.VP: {
        DIRECTION.UP: [CHAR.VP, CHAR.SW, CHAR.SE],
        DIRECTION.DOWN: [CHAR.VP, CHAR.NW, CHAR.NE],
    },
    CHAR.HP: {
        DIRECTION.LEFT: [CHAR.HP, CHAR.NE, CHAR.SE],
        DIRECTION.RIGHT: [CHAR.HP, CHAR.NW, CHAR.SW],
    },
    CHAR.NE: {
        DIRECTION.UP: [CHAR.VP, CHAR.SW, CHAR.SE],
        DIRECTION.RIGHT: [CHAR.HP, CHAR.NW, CHAR.SW],
    },
    CHAR.NW: {
        DIRECTION.UP: [CHAR.VP, CHAR.SW, CHAR.SE],
        DIRECTION.LEFT: [CHAR.HP, CHAR.NE, CHAR.SE],
    },
    CHAR.SW: {
        DIRECTION.DOWN: [CHAR.VP, CHAR.NE, CHAR.NW],
        DIRECTION.LEFT: [CHAR.HP, CHAR.NE, CHAR.SE],
    },
    CHAR.SE: {
        DIRECTION.DOWN: [CHAR.VP, CHAR.NE, CHAR.NW],
        DIRECTION.RIGHT: [CHAR.HP, CHAR.SW, CHAR.NW],
    },
}


def fill_maze():
    maze, pos = load_input()
    maze[pos[0]][pos[1]] = 'J'  # change start to J (based on the input)
    cnt = 0
    last_pos = None
    while True:
        cnt += 1
        for way in [DIRECTION.UP, DIRECTION.DOWN, DIRECTION.LEFT, DIRECTION.RIGHT]:
            next_tile = maze[pos[0] + way[0]][pos[1] + way[1]]
            next_pos = [pos[0] + way[0], pos[1] + way[1]]
            current_char = maze[pos[0]][pos[1]]
            if next_tile in cons.get(current_char, {}).get(way, {}) and next_pos != last_pos:
                maze[pos[0]][pos[1]] = 'X' + current_char
                last_pos = pos
                pos = next_pos
                break
        else:
            maze[pos[0]][pos[1]] = 'X' + maze[pos[0]][pos[1]]
            break
    return cnt, maze


@aoc_part(1)
def solve_pt1():
    cnt, _ = fill_maze()
    return cnt // 2


@aoc_part(2)
def solve_pt2():
    _, maze = fill_maze()
    res = 0
    inside = False
    start_of_inside = None
    for idx, R in enumerate(maze):
        for jdx, C in enumerate(R):
            if C[0] != 'X' and inside:  # not part of the loop and inside
                res += 1
                continue
            C = C[1:]

            # https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm
            # | flips (new segment)
            # ╔ --- ╝ flips (new segment)
            # ╚ --- ╗ flips (new segment)
            # ╔ --- ╗ doesnt change (same segment)
            # ╚ --- ╝ doesnt change (same segment)

            if C == CHAR.VP:
                inside = not inside
            elif C in [CHAR.NE, CHAR.SE]:
                start_of_inside = C
            elif start_of_inside == CHAR.SE and C == CHAR.NW:
                inside = not inside
            elif start_of_inside == CHAR.NE and C == CHAR.SW:
                inside = not inside

    return res


solve_pt1()
solve_pt2()
