import operator
from collections import defaultdict
from enum import IntEnum
from heapq import heappop, heappush

from tqdm import tqdm

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            res.append(list(line))
    return res


def create_graph(data):
    R = len(data)
    C = len(data[0])
    graph = defaultdict(list)
    start = None
    end = None
    for r in range(R):
        for c in range(C):
            val = data[r][c]
            if val == "S":
                start = (r, c)
            elif val == 'E':
                end = (r, c)

            if val not in ['.', 'E', 'S']:
                continue
            for dr in [-1, 1]:
                rr = r + dr
                if 0 <= rr < R:
                    new_val = data[rr][c]
                    if new_val in ['.', 'E', 'S']:
                        graph[(r, c)].append((rr, c))
            for dc in [-1, 1]:
                cc = c + dc
                if 0 <= cc < C:
                    new_val = data[r][cc]
                    if new_val in ['.', 'E', 'S']:
                        # if need weight add it here as val and unpack when getting neighbors in dijkstra body
                        graph[(r, c)].append((r, cc))
    return graph, start, end


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


@aoc_part(1)
def solve_pt1():
    data = load_input()
    G, source, target = create_graph(data)
    cost, res = dijkstra(G, source, target)
    return cost


def is_reverse(direction: Direction, curr_direction: Direction):
    return direction is not None and (
            direction is Direction.UP and curr_direction is Direction.DOWN or
            direction is Direction.DOWN and curr_direction is Direction.UP or
            direction is Direction.LEFT and curr_direction is Direction.RIGHT or
            direction is Direction.RIGHT and curr_direction is Direction.LEFT
    )


def dijkstra(graph, start, end, all_paths=False):
    start_state = (start, Direction.RIGHT)
    queue = [(0, start_state, ())]
    mins = {start_state: 0}
    results = []  # needed for all paths
    min_cost = None
    pbar = tqdm()
    cmp_op = operator.le if all_paths else operator.lt

    while queue:
        cost_so_far, curr_state, path = heappop(queue)
        curr_node, curr_direction = curr_state
        path = (curr_node, path)
        if min_cost and cost_so_far > min_cost:
            continue
        pbar.set_description(f"Cost: {cost_so_far}, HeapSize: {len(queue)}")
        if curr_node == end:
            if not all_paths:
                return cost_so_far, path
            if min_cost is None or cost_so_far <= min_cost:
                min_cost = cost_so_far
                results.append((cost_so_far, path))
            continue

        for target in graph.get(curr_node, ()):
            direction = get_direction(curr_node, target)

            if is_reverse(direction, curr_direction):
                continue

            if direction is curr_direction:
                target_cost = 1
            else:
                target_cost = 1001

            target_state = (target, direction)
            prev = mins.get(target_state, None)
            next_cost = cost_so_far + target_cost
            if prev is None or cmp_op(next_cost, prev):  # <= for all paths, < for single path
                mins[target_state] = next_cost
                heappush(queue, (next_cost, target_state, path))
    return results


@aoc_part(2)
def solve_pt2():
    data = load_input()
    G, source, target = create_graph(data)
    results = dijkstra(G, source, target, all_paths=True)
    paths = [x[1] for x in results]
    visited = set()
    for p in paths:
        while p:
            visited.add(p[0])
            p = p[1]

    return len(visited)


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
