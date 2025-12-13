from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            res.append(list(line))
    return res


def solve(pt2=False):
    data = load_input()
    C = len(data)
    R = len(data[0])
    ans = 0
    while True:
        k = 0
        for r in range(R):
            for c in range(C):
                if data[r][c] != '@':
                    continue
                res = 0
                for dr, dc in ((-1, -1), (-1, 0), (-1, 1),
                               (0, -1),           (0, 1),
                               (1, -1), (1, 0), (1, 1)):
                    rr = r + dr
                    cc = c + dc
                    if rr == r and cc == c:
                        continue
                    if rr < 0 or rr >= R:
                        continue
                    if cc < 0 or cc >= C:
                        continue

                    if data[rr][cc] == '@':
                        res += 1
                if res < 4:
                    k += 1
                    if pt2:
                        data[r][c] = '.'
                    else:
                        ans += 1
        if pt2:
            ans += k
            if k == 0:
                return ans
        else:
            return ans


@aoc_part(1)
def solve_pt1():
    return solve()


@aoc_part(2)
def solve_pt2():
    return solve(pt2=True)


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
