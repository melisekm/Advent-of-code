import re
from dataclasses import dataclass

from utils import aoc_part


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Robot:
    position: Point
    velocity: Point

    def move(self, R, C):
        self.position.x = (self.position.x + self.velocity.x) % C
        self.position.y = (self.position.y + self.velocity.y) % R


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = list(map(int, re.findall(r'-?\d+', line.strip())))
            res.append([line[:2], line[2:]])
    return res


@aoc_part(1)
def solve_pt1():
    C, R, robots = move_bots()
    mid_R = R // 2
    mid_C = C // 2
    q1 = q2 = q3 = q4 = 0
    for bot in robots:
        x, y = bot.position.x, bot.position.y
        if x == mid_C or y == mid_R:
            continue
        if y < mid_R:
            if x < mid_C:
                q1 += 1
            else:
                q2 += 1
        else:
            if x < mid_C:
                q3 += 1
            else:
                q4 += 1
    return q1 * q2 * q3 * q4


def move_bots(max_steps=100):
    data = load_input()
    R = 103
    C = 101
    robots = [Robot(Point(*robot[0]), Point(*robot[1])) for robot in data]
    for _ in range(max_steps):
        for robot in robots:
            robot.move(R, C)
    return C, R, robots


@aoc_part(2)
def solve_pt2():
    result = 7569
    C, R, robots = move_bots(result)
    TO_DRAW = [1 + 94 + i * C for i in range(100)]
    draw(robots, R, C, result, TO_DRAW, mode="w")

    return result


def draw(robots, R, C, step, TO_DRAW, mode="a"):
    if step not in TO_DRAW:
        return

    buf = [
        ["." for _ in range(C)] for _ in range(R)
    ]
    for robot in robots:
        buf[robot.position.y][robot.position.x] = "X"

    with open("tree.txt", mode) as f:
        f.write(f"{step}\n")
        f.write("\n".join(''.join(line) for line in buf))


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
