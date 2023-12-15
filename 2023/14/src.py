from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f.read().splitlines():
            res.append(list(line.strip()))
    return res


def safe_get(data, idx, jdx):
    if idx < 0 or jdx < 0:
        return None
    try:
        return data[idx][jdx]
    except IndexError:
        return None


moves = {
    "up": lambda idx, jdx: (idx - 1, jdx),
    "down": lambda idx, jdx: (idx + 1, jdx),
    "left": lambda idx, jdx: (idx, jdx - 1),
    "right": lambda idx, jdx: (idx, jdx + 1),
}


def move_rock(data, idx, jdx, fn):
    while True:
        next_idx, next_jdx = fn(idx, jdx)
        next_rock = safe_get(data, next_idx, next_jdx)
        if next_rock == ".":
            data[idx][jdx] = "."
            data[next_idx][next_jdx] = "O"
            idx, jdx = next_idx, next_jdx
        else:
            break


def move_rocks(data, dir_name):
    direction = moves[dir_name]
    if dir_name == 'down':
        iterator = range(len(data) - 1, -1, -1)
    else:
        iterator = range(len(data))

    for idx in iterator:
        R = data[idx]
        if dir_name == 'right':
            R = range(len(R) - 1, -1, -1)
        else:
            R = range(len(R))
        for jdx in R:
            C = data[idx][jdx]
            if C == "O":
                move_rock(data, idx, jdx, direction)


def calc_result(data):
    res = 0
    points = len(data)
    for R in data:
        O_count = R.count("O")
        res += O_count * points
        points -= 1
    return res


@aoc_part(1)
def solve_pt1():
    data = load_input()
    move_rocks(data, "up")
    return calc_result(data)


@aoc_part(2)
def solve_pt2():
    data = load_input()
    nums = []
    for _ in range(165):
        for dir_name in ["up", "left", "down", "right"]:
            move_rocks(data, dir_name)
        nums.append(calc_result(data))

    # after 128 cycles the pattern starts to repeat. pattern is 36 cycles long
    # 128 == 164, 129 == 165

    # so we can calculate the result for 1000000000:
    # get start of the loop nearest to 1000000000 and take the remainder of the division and subtract 1
    # because of indexing

    loop_start = 128
    loop_length = 36
    nearest_loop = 1000000000 - loop_start
    loop = nearest_loop % loop_length
    return nums[loop_start + loop - 1]


solve_pt1()
solve_pt2()
