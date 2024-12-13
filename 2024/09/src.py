from tqdm import tqdm

from utils import aoc_part


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        return f.read().strip()


@aoc_part(1)
def solve_pt1():
    blob = make_blob()

    ptr = blob.index(".")
    ptr2 = len(blob) - 1
    while ptr != ptr2:
        if blob[ptr2] == '.':
            ptr2 -= 1
            continue

        if blob[ptr] == ".":
            blob[ptr], blob[ptr2] = blob[ptr2], blob[ptr]

        ptr += 1

    res = 0
    for i, num in enumerate(blob):
        if num == '.':
            return res
        res += i * int(num)
    return res


def make_blob():
    data = load_input()
    blob = []
    idx = 0
    for i, char in enumerate(data):
        num = int(char)
        new_char = idx
        if i % 2 == 1:
            new_char = '.'
            idx += 1

        new_block = [new_char] * num
        blob.extend(new_block)
    return blob


def move(blob, ptr, ptr2, max_to_move):
    ptr2_orig_data = blob[ptr2]
    moved = 0
    while blob[ptr] == '.':
        blob[ptr], blob[ptr2] = blob[ptr2], blob[ptr]
        ptr2 -= 1
        ptr += 1
        moved += 1
        if moved == max_to_move:
            # if we were moving more than needed it could switch same pieces between each other
            return

        if blob[ptr2] != ptr2_orig_data:
            return


def find_consecutive_space_of(blob, length_to_find, max_search_space):
    idx = blob.index(".")
    while idx <= max_search_space:
        start = idx
        found = 0
        if blob[idx] != '.':
            idx += 1
            continue
        while idx <= max_search_space and blob[idx] == '.':
            idx += 1
            found += 1
            if found == length_to_find:
                return start
    return None


@aoc_part(2)
def solve_pt2():
    blob = make_blob()
    ptr2 = len(blob) - 1
    pbar = tqdm()
    while ptr2 > 0:
        pbar.set_description(str(ptr2))
        if blob[ptr2] == '.':
            ptr2 -= 1
            continue
        length_to_find = blob.count(blob[ptr2])
        ptr = find_consecutive_space_of(blob, length_to_find, ptr2)
        if ptr is None:
            ptr2 -= length_to_find
            continue

        move(blob, ptr, ptr2, length_to_find)
        ptr2 -= length_to_find

    res = 0
    for i, num in enumerate(blob):
        if num == '.':
            continue
        res += i * int(num)
    return res


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
