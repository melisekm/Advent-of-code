from __future__ import annotations

from collections import defaultdict
from enum import IntEnum
from heapq import heappush, heappop

from tqdm import tqdm

from utils import aoc_part


def load_input(file_name=r"in.txt"):
    with open(file_name) as f:
        return [[int(node) for node in line.strip()] for line in f]


def create_graph(data):
    R = len(data)
    C = len(data[0])
    graph = defaultdict(list)
    for r in range(R):
        for c in range(C):
            for dr in [-1, 1]:
                rr = r + dr
                if 0 <= rr < R:
                    graph[(r, c)].append((data[rr][c], (rr, c)))
            for dc in [-1, 1]:
                cc = c + dc
                if 0 <= cc < C:
                    graph[(r, c)].append((data[r][cc], (r, cc)))
    return graph, (0, 0), (R - 1, C - 1)


class Direction(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def get_direction(curr, target_node) -> Direction:
    if curr[0] == target_node[0]:
        if curr[1] < target_node[1]:
            return Direction.RIGHT
        else:
            return Direction.LEFT
    else:
        if curr[0] < target_node[0]:
            return Direction.DOWN
        else:
            return Direction.UP


def is_reverse(direction: Direction, curr_direction: Direction):
    return direction is not None and (
            direction is Direction.UP and curr_direction is Direction.DOWN or
            direction is Direction.DOWN and curr_direction is Direction.UP or
            direction is Direction.LEFT and curr_direction is Direction.RIGHT or
            direction is Direction.RIGHT and curr_direction is Direction.LEFT
    )


def dijkstra(graph, start, end, part2=False) -> (int, tuple[tuple[int, int], tuple[...]]):
    # State is location, count of same directions in a row, and current direction
    start_state = (start, 1, None)
    queue = [(0, start_state, ())]
    mins = {start_state: 0}
    pbar = tqdm()
    while queue:
        (cost_so_far, curr, path) = heappop(queue)
        curr_node, dir_in_row, curr_direction = curr
        pbar.set_description(f"Cost: {cost_so_far}, HeapSize: {len(queue)}")
        path = (curr_node, path)
        if curr_node == end and (not part2 or dir_in_row >= 4):
            return cost_so_far, path

        for target_cost, target in graph.get(curr_node, ()):
            direction = get_direction(curr_node, target)

            if is_reverse(direction, curr_direction):
                continue

            # if same row, increase, else set to 1
            if direction == curr_direction:
                direction_in_a_row = dir_in_row + 1
            else:
                direction_in_a_row = 1

            # max 10 or 3 in a row
            if direction_in_a_row > (10 if part2 else 3):
                continue

            # if went less than 4 times in a row and now going in a different direction then skip, start doesn't count
            if part2 and curr_direction is not None and dir_in_row < 4 and direction != curr_direction:
                continue

            target_state = (target, direction_in_a_row, direction)
            prev = mins.get(target_state, None)
            next_cost = cost_so_far + target_cost
            if prev is None or next_cost < prev:
                mins[target_state] = next_cost
                heappush(queue, (next_cost, target_state, path))

    return float("inf"), None


def solve(pt2=False):
    data = load_input()
    G, source, target = create_graph(data)
    cost, res = dijkstra(G, source, target, pt2)
    path = []
    while res:
        path.append(res[0])
        res = res[1]
    path.reverse()
    return cost


@aoc_part(1)
def solve_pt1():
    return solve(False)


@aoc_part(2)
def solve_pt2():
    return solve(True)


solve_pt1()
solve_pt2()
