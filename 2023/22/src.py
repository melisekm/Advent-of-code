import copy
from collections import defaultdict
from dataclasses import dataclass

from tqdm import tqdm

from utils import generic_parallel_execution, aoc_part


def load_input(file_name=r"in.txt", test_str=None):
    res = []
    with open(file_name) as f:
        if test_str:
            f = test_str.strip().splitlines()
        for line in f:
            start, end = line.strip().split("~")
            start = start.split(",")
            end = end.split(",")
            res.append(BrickLine(int(start[0]), int(start[1]), int(start[2]), int(end[0]), int(end[1]), int(end[2])))
    res.sort(key=lambda x: x.start_z)
    return res


@dataclass
class BrickLine:
    start_x: int
    start_y: int
    start_z: int
    end_x: int
    end_y: int
    end_z: int
    name: str = None


def do_lines_intersect(line1: tuple, line2: tuple):
    x1, y1, z1, x2, y2, z2 = line1
    x3, y3, z3, x4, y4, z4, = line2

    # Check if lines overlap in both X and Y dimensions
    overlap_x = max(x1, x2) >= min(x3, x4) and min(x1, x2) <= max(x3, x4)
    overlap_y = max(y1, y2) >= min(y3, y4) and min(y1, y2) <= max(y3, y4)

    # Check if lines overlap in Z dimension
    overlap_z = max(z1, z2) >= min(z3, z4) and min(z1, z2) <= max(z3, z4)

    # Lines intersect if they overlap in both X and Y dimensions, and Z dimension
    return overlap_x and overlap_y and overlap_z


def get_removable_bricks(SUPPORT, data):
    single_support = set()
    # Bricks that are sole support to other bricks CAN'T be removed
    for support in SUPPORT.values():
        if len(support) == 1:
            single_support.add(support[0])
    # Bricks that are not sole support to other bricks and do not belong to single_support CAN be removed
    can_remove = set()
    for support in SUPPORT.values():
        if len(support) > 1:
            for brick in support:
                if brick not in single_support:
                    can_remove.add(brick)
    # Bricks that do not support anything CAN be removed (they are just lying on other bricks)
    for brick in data:
        found_support = False
        for supporting_bricks in SUPPORT.values():
            for supporting_brick in supporting_bricks:
                if supporting_brick == brick.name:
                    found_support = True
                    break
            if found_support:
                break
        if not found_support:
            can_remove.add(brick.name)
    return can_remove


def get_support(data):
    support = defaultdict(list)
    for brick in data:
        for other_brick in data:
            if other_brick == brick:
                continue
            # if distance on z axis between bricks is 1
            if brick.start_z - other_brick.end_z == 1:
                # if bricks overlap on x and y axis
                if do_lines_intersect(
                        (brick.start_x, brick.start_y, 0, brick.end_x, brick.end_y, 0),
                        (other_brick.start_x, other_brick.start_y, 0, other_brick.end_x, other_brick.end_y, 0)
                ):
                    support[brick.name].append(other_brick.name)
    return support


def simulate_falling(orig_data, disable_tdqm=False):
    data = copy.deepcopy(orig_data)
    Z = defaultdict(list)
    max_z_length = 0
    for brick in data:
        Z[brick.start_z].append(brick)
        max_z_length = max(max_z_length, brick.end_z - brick.start_z)

    for brick in tqdm(data, disable=disable_tdqm):
        falling = True
        while falling:
            new_start_z = brick.start_z - 1
            new_end_z = brick.end_z - 1
            if new_start_z < 1:
                break
            # the longest brick is max_z_length so we need to check only bricks that are max_z_length away from new_start_z
            to_check = sum([Z.get(x, []) for x in range(new_start_z - max_z_length, new_start_z + 1)], [])
            for other_brick in to_check:
                if other_brick == brick:
                    continue
                if do_lines_intersect(
                        (brick.start_x, brick.start_y, new_start_z, brick.end_x, brick.end_y, new_end_z),
                        (other_brick.start_x, other_brick.start_y, other_brick.start_z, other_brick.end_x,
                         other_brick.end_y, other_brick.end_z)
                ):
                    falling = False
                    break
            if falling:
                Z[brick.start_z].remove(brick)
                brick.start_z = new_start_z
                brick.end_z = new_end_z
                Z[brick.start_z].append(brick)
    return data


def solve(data):
    for idx, brick in enumerate(data):
        brick.name = idx
    data = simulate_falling(data)
    SUPPORT = get_support(data)
    can_remove = get_removable_bricks(SUPPORT, data)
    return can_remove, data


@aoc_part(1)
def solve_pt1(test_str=None):
    data = load_input(test_str=test_str)
    can_remove, _ = solve(data)
    return len(can_remove)


def run_pt2(check_portion, data, pbar_position=None):
    res = 0
    pbar = tqdm(check_portion, position=pbar_position)
    for brick in pbar:
        new_data = copy.deepcopy(data)
        new_data.remove(new_data[brick])
        diff = simulate_falling(new_data, disable_tdqm=True)
        for orig, new in zip(new_data, diff):
            if orig.start_z != new.start_z:
                res += 1
        pbar.set_postfix({"res": res})
    return res


@aoc_part(2)
def solve_pt2():
    data = load_input()
    can_be_removed, data = solve(data)
    need_to_check = set([brick.name for brick in data]) - can_be_removed
    res = generic_parallel_execution(run_pt2, list(need_to_check), data, workers=4,
                                     executor="process", add_pbar=True)
    return sum(res)


t1 = """
0,0,1~0,1,1
1,1,1~1,1,1
0,0,2~0,0,2
0,1,2~1,1,2
"""

t2 = """
0,0,1~0,0,1
1,1,1~1,1,1
0,0,2~0,1,2
0,1,3~1,1,3
"""

t3 = """
0,0,1~0,0,2
1,0,1~2,0,1
1,0,2~1,0,2
0,0,3~1,0,3
"""

t4 = """
0,0,2~0,0,4
1,0,3~2,0,3
1,0,4~1,0,5
0,0,6~1,0,6
"""

t5 = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""

if __name__ == '__main__':
    assert [3,2,3,3,5] == [solve_pt1(t) for t in [t1, t2, t3, t4, t5]]
    solve_pt1()
    solve_pt2()
