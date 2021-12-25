import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            res.append(int(line.strip().split(": ")[1]))
    return res[0], res[1]


def move_player(p_pos, dice, p_score):
    dice_roll = 0
    for _ in range(3):
        dice += 1
        if dice == 101:
            dice = 1
        dice_roll += dice
    p_pos += dice_roll
    if p_pos % 10 == 0:
        p_pos = 10
    else:
        p_pos %= 10
    p_score += p_pos
    return dice, p_pos, p_score


def solve_pt1():
    p1_pos, p2_pos = load_input()
    cntr = 0
    dice = 0
    p1_score = p2_score = 0
    while True:
        dice, p1_pos, p1_score = move_player(p1_pos, dice, p1_score)
        cntr += 3
        if p1_score >= 1000:
            return p2_score * cntr
        dice, p2_pos, p2_score = move_player(p2_pos, dice, p2_score)
        cntr += 3
        if p2_score >= 1000:
            return p1_score * cntr


def solve_pt2():
    data = load_input()

    pass


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Total time pt1: {(end - start):.3f} sec")

# start = timeit.default_timer()
# result2 = solve_pt2()
# end = timeit.default_timer()
# print(result2)
# print(f"Total time pt2: {(end - start):.3f} sec")
