import math
import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip().split()
            direction, num = line[0], int(line[1])
            res.append((direction, num))
    return res


# based on location calculate the direction to move
def get_next_pos(first, second):
    return 1 if first > second else -1 if first < second else 0


class MainHead:
    def __init__(self):
        self.pos = (0, 0)
        self.direction_map = {
            "R": (1, 0),
            "L": (-1, 0),
            "U": (0, 1),
            "D": (0, -1)
        }

    def move(self, x, y):
        self.pos = (self.pos[0] + x, self.pos[1] + y)


class Tail:
    def __init__(self):
        self.pos = (0, 0)
        self.visited = {self.pos}
        self.target = None

    def move(self):
        dx = self.target.pos[0] - self.pos[0]
        dy = self.target.pos[1] - self.pos[1]
        if math.sqrt(dx ** 2 + dy ** 2) > math.sqrt(2):  # move if more than 1 step
            self.pos = (self.pos[0] + get_next_pos(self.target.pos[0], self.pos[0]),  # X
                        self.pos[1] + get_next_pos(self.target.pos[1], self.pos[1]))  # Y
            self.visited.add(self.pos)


def solve(max_tails):
    data = load_input()
    main_head = MainHead()
    tails = [Tail() for _ in range(max_tails)]
    tails[0].target = main_head
    for idx in range(1, max_tails):
        tails[idx].target = tails[idx - 1]
    for direction, num in data:
        x, y = main_head.direction_map[direction]
        for _ in range(num):
            main_head.move(x, y)
            for tail in tails:  # move all tails to follow the target
                tail.move()

    return len(tails[-1].visited)


def solve_pt1():
    return solve(1)


def solve_pt2():
    return solve(9)


def run_part(solve_fn, part_idx):
    start = timeit.default_timer()
    result = solve_fn()
    end = timeit.default_timer()
    print(result)
    print(f"Total time pt{part_idx}: {(end - start):.3f} sec")


run_part(solve_pt1, 1)
run_part(solve_pt2, 2)
