import dataclasses
from dataclasses import dataclass
from functools import reduce, cache

from utils import aoc_part


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        return f.read().strip().split(",")


@cache
def h(x):
    return reduce(lambda acc, char: ((acc + (ord(char))) * 17) % 256, x, 0)


@aoc_part(1)
def solve_pt1():
    return sum(h(x) for x in load_input())


@dataclass
class Item:
    name: str
    lens: int


@dataclass
class Box:
    items: list[Item] = dataclasses.field(default_factory=list)

    def add(self, new_item: Item):
        for idx, item in enumerate(self.items):
            if item.name == new_item.name:
                self.items[idx] = new_item
                break
        else:
            self.items.append(new_item)

    def remove(self, item_to_be_removed: str):
        for idx, item in enumerate(self.items):
            if item.name == item_to_be_removed:
                self.items.pop(idx)
                break


@aoc_part(2)
def solve_pt2():
    data = load_input()
    boxes = [Box() for _ in range(256)]
    for item in data:
        if "=" in item:
            name, lens = item.split("=")
            lens = int(lens)
            boxes[h(name)].add(Item(name, lens))
        elif '-' in item:
            name = item[:-1]
            boxes[h(name)].remove(name)

    return sum(
        idx * jdx * item.lens
        for idx, box in enumerate(boxes, start=1)
        for jdx, item in enumerate(box.items, start=1)
    )


solve_pt1()
solve_pt2()
