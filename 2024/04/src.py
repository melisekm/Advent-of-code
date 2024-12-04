from utils import aoc_part


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        return f.read().splitlines()


def run(data, RR, CC, target_letter, direction):
    r, c = direction
    new_r, new_c = RR + r, CC + c
    if new_r < 0 or new_r >= len(data) or new_c < 0 or new_c >= len(data[0]):
        raise ValueError
    if data[new_r][new_c] == target_letter:
        return new_r, new_c
    raise ValueError


def try_directions(target_word, data, RR, CC, word_idx, direction, pos):
    if word_idx >= len(target_word):
        return
    rr, cc = run(data, RR, CC, target_word[word_idx], direction)
    pos[target_word[word_idx]] = rr, cc
    try_directions(target_word, data, rr, cc, word_idx + 1, direction, pos)


def solve(directions, target_word, p2=False):
    data = load_input()
    res = 0
    a_pos = set()
    for RR in range(len(data)):
        for CC in range(len(data[0])):
            val = data[RR][CC]
            if val != target_word[0]:
                continue
            for direction in directions:
                pos = {}
                try:
                    try_directions(target_word, data, RR, CC, 1, direction, pos)
                    if p2:
                        if pos["A"] in a_pos:
                            res += 1
                        a_pos.add(pos["A"])
                    else:
                        res += 1
                except (IndexError, ValueError):
                    pass
    return res


@aoc_part(1)
def solve_pt1():
    directions = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1],
    ]
    return solve(directions, "XMAS")


@aoc_part(2)
def solve_pt2():
    directions = [
        [-1, -1],
        [-1, 1],
        [1, -1],
        [1, 1],
    ]
    return solve(directions, "MAS", p2=True)


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
