import dataclasses
from dataclasses import dataclass

from tqdm import trange

from utils import aoc_part


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        return [list(line.strip()) for line in f]


@dataclass
class Tile:
    point: str
    visited: bool = False
    visit_directions: list[str] = dataclasses.field(default_factory=list)

    def __eq__(self, other):
        return self.point == other

    def __hash__(self):
        return hash(self.point)


cons = {
    "/": {
        "right": ["up", -1, 0],
        "left": ["down", 1, 0],
        "up": ["right", 0, 1],
        "down": ["left", 0, -1],
    },
    "\\": {
        "right": ["down", 1, 0],
        "left": ["up", -1, 0],
        "up": ["left", 0, -1],
        "down": ["right", 0, 1],
    },
}


@dataclass
class Beam:
    R: int
    C: int
    dr: int
    dc: int
    direction: str

    def move(self, maze: list[list[Tile]]):
        self.R += self.dr
        self.C += self.dc

        if self.R < 0 or self.R >= len(maze) or self.C < 0 or self.C >= len(maze[0]):
            return
        if maze[self.R][self.C].visited and self.direction in maze[self.R][self.C].visit_directions:
            return

        maze[self.R][self.C].visited = True
        maze[self.R][self.C].visit_directions.append(self.direction)
        if maze[self.R][self.C] == "|":
            if self.direction in ("right", "left"):
                new_beam_1 = Beam(self.R, self.C, 1, 0, "down")
                new_beam_2 = Beam(self.R, self.C, -1, 0, "up")
                return [new_beam_1, new_beam_2]

        elif maze[self.R][self.C] == "-":
            if self.direction in ("up", "down"):
                new_beam_1 = Beam(self.R, self.C, 0, 1, "right")
                new_beam_2 = Beam(self.R, self.C, 0, -1, "left")
                return [new_beam_1, new_beam_2]

        elif maze[self.R][self.C] in cons:
            self.direction, self.dr, self.dc = cons[maze[self.R][self.C]][self.direction]

        return [self]


def solve(data, beam):
    beams = [beam]
    tiles = [[Tile(point) for c, point in enumerate(row)] for r, row in enumerate(data)]
    while True:
        new_beams = []
        for beam in beams:
            res = beam.move(tiles)
            if res:
                new_beams.extend(res)
        if not new_beams:
            break
        beams = new_beams
    return sum(t.visited for tile in tiles for t in tile)


@aoc_part(1)
def solve_pt1():
    return solve(load_input(), Beam(0, -1, 0, 1, "right"))


@aoc_part(2)
def solve_pt2():
    data = load_input()
    return max(
        max(solve(data, Beam(r, -1, 0, 1, "right")) for r in trange(len(data))),
        max(solve(data, Beam(r, len(data[0]), 0, -1, "left")) for r in trange(len(data) - 1, -1, -1)),
        max(solve(data, Beam(-1, c, 1, 0, "down")) for c in trange(len(data[0]))),
        max(solve(data, Beam(len(data), c, -1, 0, "up")) for c in trange(len(data[0]) - 1, -1, -1)),
    )


solve_pt1()
solve_pt2()
