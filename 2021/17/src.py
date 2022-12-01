import timeit
from concurrent.futures import ProcessPoolExecutor

import numpy as np


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        for line in f:
            line = line.strip().split(": ")[1]
            line = line.split(", ")
            x = line[0].split("=")[1].split("..")
            x = [int(x[0]), int(x[1])]
            y = line[1].split("=")[1].split("..")
            y = [int(y[0]), int(y[1])]
            return {
                "x": {"start": x[0], "end": x[1]},
                "y": {"start": y[0], "end": y[1]},
            }


class Ball:
    def __init__(self, dx, dy):
        self.initDX = dx
        self.initDY = dy
        self.x = 0
        self.y = self.maxY = 0
        self.dx = dx
        self.dy = dy

    def check_in(self, target):
        return target["x"]["start"] <= self.x <= target["x"]["end"] \
               and target["y"]["start"] <= self.y <= target["y"]["end"]

    def check_out(self, target):
        return self.x > target["x"]["end"] or (self.y < target["y"]["end"] and self.dy < target["y"]["end"])

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.dx > 0:
            self.dx -= 1
        elif self.dx < 0:
            self.dx += 1
        self.dy -= 1

        self.maxY = max(self.maxY, self.y)

    def flight_control(self, target):
        return self.check_in(target) or self.check_out(target)


def solve_pt1():
    target = load_input()
    heights = []
    balls = [Ball(x, y) for x in range(1, target["x"]["end"]) for y in range(1, 100)]
    while balls:
        for ball in list(balls):
            ball.move()
            if ball.check_in(target):
                heights.append(ball.maxY)
                balls.remove(ball)
            elif ball.check_out(target):
                balls.remove(ball)
    return max(heights)


def shoot_balls(balls, target):
    x = 0
    while balls:
        for ball in list(balls):
            ball.move()
            if ball.check_in(target):
                x += 1
                balls.remove(ball)
            elif ball.check_out(target):
                balls.remove(ball)
    return x


def solve_pt2():
    target = load_input()
    balls = [Ball(x, y) for x in range(1, target["x"]["end"] + 1) for y in range(target["y"]["start"], 500)]
    workers = 4
    space = np.linspace(0, len(balls), num=workers + 1, dtype=int)
    xs = [0] * workers
    with ProcessPoolExecutor(max_workers=workers) as executor:
        for i in range(workers):
            xs[i] = executor.submit(shoot_balls, balls[space[i]:space[i + 1]], target)

    # noinspection PyUnresolvedReferences
    return sum(x.result() for x in xs)


if __name__ == '__main__':
    start = timeit.default_timer()
    result1 = solve_pt1()
    end = timeit.default_timer()
    print(result1)
    print(f"Total time pt1: {(end - start):.3f} sec")

    start = timeit.default_timer()
    result2 = solve_pt2()
    end = timeit.default_timer()
    print(result2)
    print(f"Total time pt2: {(end - start):.3f} sec")
