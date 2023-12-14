from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        patterns = f.read().split("\n\n")
        for pattern in patterns:
            horiz = pattern.split("\n")
            vert = ["".join([horiz[i][j] for i in range(len(horiz))]) for j in range(len(horiz[0]))]
            res.append((horiz, vert))
    return res


def safe_get(data, idx):
    if idx < 0:
        return None
    try:
        return data[idx]
    except IndexError:
        return None


def fix_smudge(up, down):
    for i, char in enumerate(up):
        for j, char2 in enumerate(down):
            if char == char2:
                continue

            # attempt to swap the bad character and check if the reflection is ok (both ways)
            new_up = up[:i] + char2 + up[i + 1:]
            if new_up == down:
                return True
            new_down = down[:j] + char + down[j + 1:]
            if new_down == up:
                return True
    return False


def expand(data, current, smudge_fixed=False, p2=False):
    streak = 0
    up = current - 1
    down = current + 2

    while True:
        streak += 1
        curr_up = safe_get(data, up)
        curr_down = safe_get(data, down)

        if curr_up is None:
            # reached the end of reflection
            if p2 and not smudge_fixed:
                # in part 2 smudge has to be fixed
                return 0
            return streak

        # if curr_down is none, attempt to walk up to the end of reflection
        if curr_down is not None:
            if curr_up == curr_down:
                # continue walking, both reflections ok
                pass
            elif p2 and not smudge_fixed:
                # in part 2 if they are different, attempt to fix it, if not possible, break
                if fix_smudge(curr_up, curr_down):
                    smudge_fixed = True
                else:
                    break
            else:
                # in part 1 if they are different and we did not reach the end of the reflection, break
                break
        up -= 1
        down += 1
    return 0


def simulate(seq, p2=False):
    cnt = 0
    for idx, curr_seqs in enumerate(zip(seq, seq[1:])):
        first, second = curr_seqs
        smudge_fixed = False
        if p2:
            if first != second:
                smudge_fixed = fix_smudge(first, second)
        if first == second or smudge_fixed:
            cnt = max(expand(seq, idx, smudge_fixed=smudge_fixed, p2=p2), cnt)
    return cnt


def solve(p2):
    return sum(simulate(pattern[1], p2) + 100 * simulate(pattern[0], p2) for pattern in load_input())


@aoc_part(1)
def solve_pt1():
    return solve(p2=False)


@aoc_part(2)
def solve_pt2():
    return solve(p2=True)


solve_pt1()
solve_pt2()
