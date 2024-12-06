import itertools

from tqdm import trange

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    pos = None
    R = 0
    with open(file_name) as f:
        for idx, line in enumerate(f):
            line = line.strip()
            C = len(line)
            for jdx, char in enumerate(line):
                if char == '#':
                    res.append((idx, jdx))
                elif char == '^':
                    pos = (idx, jdx)
            R += 1
    assert pos
    return res, pos, (R, C)


def calc_result(new_pos, pos) -> list[tuple[int, int]]:
    # Extract coordinates
    x1, y1 = new_pos
    x2, y2 = pos

    # Ensure positions are aligned vertically or horizontally
    if x1 != x2 and y1 != y2:
        raise ValueError("Positions must be aligned vertically or horizontally")

    # Generate intermediate positions
    result = []
    if x1 == x2:  # Vertical alignment
        step = 1 if y1 > y2 else -1
        result = [(x1, y) for y in range(y2 + step, y1 + step, step)]
    elif y1 == y2:  # Horizontal alignment
        step = 1 if x1 > x2 else -1
        result = [(x, y1) for x in range(x2 + step, x1 + step, step)]

    return result


def get_next_pos(data, pos, direction, size):
    pos_i, pos_j = pos
    closest = None
    for wall in data:
        idx, jdx = wall
        if direction == 1:
            if jdx == pos_j:
                if idx < pos_i:
                    closest = (idx, jdx) if not closest or closest[0] < idx else closest
        elif direction == 2:
            if idx == pos_i:
                if jdx > pos_j:
                    closest = (idx, jdx) if not closest or closest[1] > jdx else closest
        elif direction == 3:
            if jdx == pos_j:
                if idx > pos_i:
                    closest = (idx, jdx) if not closest or closest[0] > idx else closest
        elif direction == 4:
            if idx == pos_i:
                if jdx < pos_j:
                    closest = (idx, jdx) if not closest or closest[1] < jdx else closest

    if not closest:
        end = True
        if direction == 1:
            new_pos = (0, pos_j)
        elif direction == 2:
            new_pos = (pos_i, size[1] - 1)
        elif direction == 3:
            new_pos = (size[0] - 1, pos_j)
        elif direction == 4:
            new_pos = (pos_i, 0)
    else:
        end = False
        if direction == 1:
            new_pos = (closest[0] + 1, pos_j)
        elif direction == 2:
            new_pos = (pos_i, closest[1] - 1)
        elif direction == 3:
            new_pos = (closest[0] - 1, pos_j)
        elif direction == 4:
            new_pos = (pos_i, closest[1] + 1)
        else:
            raise ValueError
    result = calc_result(new_pos, pos)
    return new_pos, result, end


@aoc_part(1)
def solve_pt1():
    data, pos, size = load_input()
    res = {pos}
    dirs = itertools.cycle([1, 2, 3, 4])
    while True:
        pos, result, end = get_next_pos(data, pos, next(dirs), size)
        res.update(result)
        if end:
            break

    return len(res)


def solve(pos, data, size):
    # we need to keep track of direction that we went
    res = {(pos, 1)}
    dirs = itertools.cycle([1, 2, 3, 4])
    while True:
        direction = next(dirs)
        pos, result, end = get_next_pos(data, pos, direction, size)
        newly_added = set((r, direction) for r in result)
        diff = newly_added - res
        if newly_added and not diff:
            # if we discover that we already went that direction among same steps, then is a loop
            # only counts if we done some steps at all
            return True
        res.update(newly_added)
        if end:
            # has normal end and not a loop
            return False


@aoc_part(2)
def solve_pt2():
    data, pos, size = load_input()
    total = 0
    pbar = trange(size[0])
    for i in pbar:
        for j in range(size[1]):
            added_pos = (i, j)
            if added_pos in data:
                continue
            data.append(added_pos)
            total += solve(pos, data, size)
            data.remove(added_pos)
        pbar.set_description(str(total))

    return total


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
