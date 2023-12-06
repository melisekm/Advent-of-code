import sys
from functools import lru_cache

from utils import aoc_part
import re


def load_input(file_name="in.txt"):
    with open(file_name, encoding='UTF-8') as f:
        lines = f.read().split("\n")
    seeds = list(map(int, re.findall(r'\d+', lines[0])))
    lines = "\n".join(lines[2:]).split("\n\n")
    res = [map_line.split("\n") for map_line in lines]
    return res, seeds


@lru_cache(maxsize=None)
def resolve_nums(rest):
    return [list(map(int, re.findall(r'\d+', i))) for i in rest]


@aoc_part(1)
def solve_pt1():
    data, seeds = load_input()
    res = sys.maxsize
    for seed in seeds:
        location = seed
        for point in data:
            nums = resolve_nums(tuple(point[1:]))
            for idx, line in enumerate(nums, start=1):
                dst, src, leng = line
                if src <= location < src + leng:
                    location += dst - src
                    break
        res = min(res, location)
    return res


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# five cases of interval overlap
# 1. interval is completely outside of map, we do not change anything
# 2. interval is covers map, we shift whole interval accordingly
# 3. interval is partially inside of map, from right side, we split interval into two
#   [start, map_start-1] and [map_start + shift, end + shift]
# 4. interval is partially inside of map, from left side, we split interval into two
#   [map_end + 1, end] and [start + shift, map_end + shift]
# 5. interval is completely inside of map, we split interval into three
#   [start, map_start-1], [map_end + 1, end] and [map_start + shift, map_end + shift]
@aoc_part(2)
def solve_pt2():
    data, seeds = load_input()
    holders = []
    for i in range(0, len(seeds), 2):
        holders.append([Interval(seeds[i], seeds[i] + seeds[i + 1] - 1)])
    global_low = sys.maxsize

    for holder in holders:
        for point in data:
            nums = resolve_nums(tuple(point[1:]))
            for line_idx, line in enumerate(nums, start=1):
                dst, src_start, leng = line
                src_end = src_start + leng - 1
                shift = dst - src_start
                for idx, interval in enumerate(holder[:]):
                    if src_start > interval.end or src_end < interval.start:
                        continue

                    if interval.start >= src_start and interval.end <= src_end:
                        holder.append(Interval(interval.start + shift, interval.end + shift))

                    elif src_start > interval.start and interval.end < src_end:
                        holder.append(Interval(interval.start, src_start - 1))  # A
                        holder.append(Interval(src_start + shift, interval.end + shift))  # B1 B2

                    elif src_start < interval.start and interval.end > src_end:
                        holder.append(Interval(src_end + 1, interval.end))  # B
                        holder.append(Interval(interval.start + shift, src_end + shift))  # C1 C2

                    elif src_start > interval.start and src_end < interval.end:
                        holder.append(Interval(interval.start, src_start - 1))  # A
                        holder.append(Interval(src_end + 1, interval.end))  # B
                        holder.append(Interval(src_start + shift, src_end + shift))  # B1 C2

                    # remove old interval, because it was changed/split
                    holder.remove(interval)

        for interval in holder:
            global_low = min(global_low, interval.start)

    return global_low


solve_pt1()
solve_pt2()
