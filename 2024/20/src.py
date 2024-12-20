import copy
from collections import defaultdict, Counter
from dataclasses import dataclass
from heapq import heappop, heappush

from tqdm import tqdm


# from utils import aoc_part


def load_input():
    for name in ["2024/20/in.txt", "in.txt"]:
        try:
            res = []
            with open(name) as f:
                for line in f:
                    line = line.strip()
                    res.append(list(line))
            return res
        except FileNotFoundError:
            pass


@dataclass(eq=True, frozen=True)
class DijkstraState:
    node: tuple


@dataclass
class QueueItem:
    cost_so_far: int
    curr_state: DijkstraState
    path: tuple

    def __lt__(self, other):
        return self.cost_so_far < other.cost_so_far


def create_graph(data):
    R = len(data)
    C = len(data[0])
    graph = defaultdict(list)
    start = None
    end = None
    dot_positions = []
    for r in range(R):
        for c in range(C):
            val = data[r][c]
            if val == "S":
                start = (r, c)
            elif val == 'E':
                end = (r, c)
            if val not in ['.', 'E', 'S']:
                continue
            dot_positions.append((r, c))
            for dr in [-1, 1]:
                rr = r + dr
                if 0 <= rr < R:
                    new_val = data[rr][c]
                    if new_val not in ['.', 'E', 'S']:
                        continue
                    graph[(r, c)].append((rr, c))
            for dc in [-1, 1]:
                cc = c + dc
                if 0 <= cc < C:
                    new_val = data[r][cc]
                    if new_val not in ['.', 'E', 'S']:
                        continue
                    graph[(r, c)].append((r, cc))
    return graph, start, end, dot_positions


def dijkstra(graph, start, end):
    start_state = DijkstraState(node=start)
    queue = [QueueItem(0, start_state, ())]
    mins = {start_state: 0}

    while queue:
        queue_item = heappop(queue)
        path = (queue_item.curr_state.node, queue_item.path)
        if queue_item.curr_state.node == end:
            return queue_item.cost_so_far, path

        for target in graph.get(queue_item.curr_state.node, ()):
            target_cost = 1
            target_state = DijkstraState(node=target)
            prev = mins.get(target_state, None)
            next_cost = queue_item.cost_so_far + target_cost
            if prev is None or next_cost < prev:
                mins[target_state] = next_cost
                heappush(queue, QueueItem(next_cost, target_state, path))
    return float('inf'), None


RESULTS = set()


def flatten_path(p):
    res = []
    while p:
        res.append(p[0])
        p = p[1]
    return tuple(res)


def validate_path(flattened_path, new_cheat_path):
    # result is cost and path, new_cheat_path is the path with cheats
    # the path must contain all the cheats
    for cheat in new_cheat_path:
        if cheat not in flattened_path:
            return False
    return flattened_path


def handle_new_val(data, rr, c, cheat_path, removed_walls, source, target, R, C, remaining_cheats):
    new_val = data[rr][c]
    if new_val != '#':
        return
    cheat = (rr, c)
    new_cheat_path = cheat_path + (cheat,)
    # check_path = (new_cheat_path[0], new_cheat_path[-1])
    if cheat in removed_walls:
        return
    removed_walls.add(cheat)
    data_copy = copy.deepcopy(data)
    data_copy[rr][c] = '.'
    new_graph = create_graph(data_copy)[0]
    result = dijkstra(new_graph, source, target)
    # flattened_path = flatten_path(result[1])
    # if validate_path(flattened_path, new_cheat_path):
    RESULTS.add((result[0], cheat))
    make_special_graphs(data_copy, R, C, rr, c, source, target, new_cheat_path, remaining_cheats - 1,
                        removed_walls)


def make_special_graphs(data, R, C, r, c, source, target, cheat_path, remaining_cheats, removed_walls):
    if remaining_cheats == 0:
        return
    for dr in [-1, 1]:
        rr = r + dr
        if 0 <= rr < R:
            handle_new_val(data, rr, c, cheat_path, removed_walls, source, target, R, C, remaining_cheats)

    for dc in [-1, 1]:
        cc = c + dc
        if 0 <= cc < C:
            handle_new_val(data, r, cc, cheat_path, removed_walls, source, target, R, C, remaining_cheats)


# @aoc_part(1)
def solve_pt1():
    data = load_input()
    max_cost = Counter([char for line in data for char in line])['.'] + 1
    R = len(data)
    C = len(data[0])
    min_time_to_save = 100
    G, source, target, dot_positions = create_graph(data)
    removed_walls: set[tuple[int, int]] = set()
    for r, c in tqdm(dot_positions, ascii=True):
        make_special_graphs(data, R, C, r, c, source, target, ((r, c),), remaining_cheats=1,
                            removed_walls=removed_walls)

    res = defaultdict(int)
    for cost, cheat in RESULTS:
        time_saved = max_cost - cost
        if time_saved >= min_time_to_save:
            res[time_saved] += 1

    res = sorted(res.items(), key=lambda x: x[0], reverse=False)
    return sum([x[1] for x in res])


# @aoc_part(2)
# def solve_pt2():
#     data = load_input()
#
#     pass

if __name__ == '__main__':
    print(solve_pt1())
    # solve_pt2()
