from tqdm import tqdm

from helpers2025 import get_all_integers_from_string
from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            for l in line.split(','):
                k = get_all_integers_from_string(l)
                res.append(k)
    return res


def check_num(num: int, maxr: int) -> bool:
    if num > maxr:
        return False
    str_n = str(num)
    size = len(str_n)
    if size % 2 == 1:
        return False
    str_n_cut1 = str_n[: size // 2]
    str_n_cut2 = str_n[size // 2:]
    if str_n_cut1 == str_n_cut2:
        return True
    return False


def make_num(num: int) -> tuple[int, int]:
    str_n = str(num)
    size = len(str_n)
    if size % 2 == 1:
        raise ValueError
    str_n_cut = str_n[: size // 2]
    return int(f"{str_n_cut}{str_n_cut}"), int(str_n_cut)


def solve_for(low_r: int, maxr: int):
    res = 0
    try:
        newn, str_n_cut = make_num(low_r)
    except ValueError:
        return res
    while True:
        if newn >= low_r:
            if check_num(newn, maxr):
                res += newn
            else:
                return res
        str_n_cut += 1
        newn = int(f"{str_n_cut}{str_n_cut}")


def ceil_to_next_power_of_10(n):
    digits = len(str(n))
    if digits % 2 == 1:
        return 10 ** digits
    return n


@aoc_part(1)
def solve_pt1():
    data = load_input()
    res = 0
    for l, r in data:
        l = ceil_to_next_power_of_10(l)
        res += solve_for(l, r)

    return res


def pt2_solve_for(k: int):
    str_k = str(k)
    for size in range(1, len(str_k) + 1):
        part = str_k[:size]
        for i in range(2, 12):
            check = part * i
            if len(check) > len(str_k):
                break
            if str_k == check:
                return True

    return False


@aoc_part(2)
def solve_pt2():
    data = load_input()
    res = 0
    for l, r in tqdm(data):
        for k in range(l, r + 1):
            if pt2_solve_for(k):
                res += k

    return res


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
