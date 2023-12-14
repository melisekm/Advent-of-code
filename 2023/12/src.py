import re
from dataclasses import dataclass
from typing import List

from tqdm import tqdm

from utils import aoc_part


@dataclass
class Character:
    char: str
    changable: bool


@dataclass
class Arrangement:
    sequence: List[Character]
    numbers: List[int]
    to_add_hashtags: int

    def is_valid(self):
        hashtags = re.findall(r"#+", "".join([x.char for x in self.sequence]))
        if len(hashtags) != len(self.numbers):
            return False
        return all([len(x) == y for x, y in zip(hashtags, self.numbers)])


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            seq, nums = line.split()
            nums = [int(x) for x in nums.split(",")]
            to_add_hashtags = sum(nums) - seq.count("#")
            sequence = []
            for char in seq:
                if char == "?":
                    sequence.append(Character(".", True))
                else:
                    sequence.append(Character(char, False))
            res.append(Arrangement(sequence, nums, to_add_hashtags))
    return res


def try_comb(arrangement, pos):
    arrangement.sequence[pos].char = '#'
    added_hashtags = sum(1 for s in arrangement.sequence if s.char == '#' and s.changable)
    if added_hashtags > arrangement.to_add_hashtags:
        arrangement.sequence[pos].char = '.'
        return 0

    if added_hashtags == arrangement.to_add_hashtags and arrangement.is_valid():
        arrangement.sequence[pos].char = '.'
        return 1
    cntr = 0
    for idx in range(pos + 1, len(arrangement.sequence)):
        if arrangement.sequence[idx].changable:
            cntr += try_comb(arrangement, idx)

    arrangement.sequence[pos].char = '.'
    return cntr


@aoc_part(1)
def solve_pt1():
    data = load_input()
    out = 0
    for arrangement in tqdm(data):
        for idx in range(len(arrangement.sequence)):
            if arrangement.sequence[idx].changable:
                if arrangement.is_valid():
                    out += 1
                    break
                out += try_comb(arrangement, idx)
    return out


@aoc_part(2)
def solve_pt2():
    data = load_input()

    pass


solve_pt1()
# solve_pt2()
