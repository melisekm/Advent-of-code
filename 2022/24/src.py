from utils import aoc_part


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        return f.read().splitlines()


class Blizzard:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, maze):
        # if we hit a wall, reappear on the other side of the maze
        if self.direction == ">":
            self.x += 1
            if maze[self.y][self.x] == "#":
                self.x = 1
        elif self.direction == "<":
            self.x -= 1
            if maze[self.y][self.x] == "#":
                self.x = len(maze[0]) - 2
        elif self.direction == "^":
            self.y -= 1
            if maze[self.y][self.x] == "#":
                self.y = len(maze) - 2
        elif self.direction == "v":
            self.y += 1
            if maze[self.y][self.x] == "#":
                self.y = 1


def get_neighbors(maze, current, blizzards):
    x, y = current
    neighbors = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x = x + dx
        new_y = y + dy
        if new_y < 0 or new_y >= len(maze) or new_x < 0 or new_x >= len(maze[0]):
            continue
        if maze[new_y][new_x] != "#" and (new_x, new_y) not in blizzards:
            neighbors.append((new_x, new_y))
    return neighbors


def create_blizzard_states(valley_map):
    blizzards = [
        Blizzard(x, y, char)
        for y, line in enumerate(valley_map)
        for x, char in enumerate(line) if char in ["<", ">", "^", "v"]
    ]
    states = []
    while True:
        encoded_blizzards = frozenset((blizzard.x, blizzard.y) for blizzard in blizzards)
        if encoded_blizzards in states:
            break
        states.append(encoded_blizzards)
        for blizzard in blizzards:
            blizzard.move(valley_map)
    return states


def bfs(states, valley_map, current, end, minute):
    visited = set()
    queue = [(current, minute)]
    while queue:
        current, minute = queue.pop(0)
        blizzard = states[minute % len(states)]
        if (current, blizzard) in visited:
            continue
        if current not in blizzard:
            queue.append((current, minute + 1))
        for neighbor in get_neighbors(valley_map, current, blizzard):
            queue.append((neighbor, minute + 1))
            if neighbor == end:
                return minute
        visited.add((current, blizzard))
    return -1


@aoc_part(1)
def solve_pt1():
    valley_map = load_input()
    return bfs(create_blizzard_states(valley_map), valley_map, (1, 0), (len(valley_map[0]) - 2, len(valley_map) - 1), 1)


@aoc_part(2)
def solve_pt2():
    valley_map = load_input()
    blizzards = create_blizzard_states(valley_map)
    start = (1, 0)
    end = (len(valley_map[0]) - 2, len(valley_map) - 1)
    finish_minute = bfs(blizzards, valley_map, start, end, 1)
    start_minute = bfs(blizzards, valley_map, end, start, finish_minute)
    finish_total = bfs(blizzards, valley_map, start, end, start_minute)
    return finish_total


solve_pt1()
solve_pt2()
