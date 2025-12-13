from collections import defaultdict
from dataclasses import dataclass
from heapq import heappop, heappush

from tqdm import tqdm

from utils import aoc_part, generic_parallel_execution


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            res.append(list(map(int, line)))
    return res


@aoc_part(1)
def solve_pt1():
    data = load_input()
    res = 0
    for battery in data:
        curr = 0
        for i in range(len(battery)):
            for j in range(i + 1, len(battery)):
                curr = max(curr, int(f"{battery[i]}{battery[j]}"))
        res += curr

    return res


@dataclass(eq=True, frozen=True)
class State:
    node: int
    length: int


@dataclass
class QueueItem:
    cost_so_far: int
    curr_state: State
    parent: "QueueItem | None"

    def __lt__(self, other):
        return self.cost_so_far > other.cost_so_far


def make_graph(battery: list[int]):
    graph = defaultdict(list)
    for i in range(len(battery)):
        for j in range(i + 1, len(battery)):
            graph[i].append(j)
    return graph


def longest_path_with_length_of_n(battery: list[int], graph: dict[int, list[int]], start_node: int, max_path_length):
    start_state = State(node=start_node, length=1)
    queue = [QueueItem(battery[start_node], start_state, None)]
    maxs = {start_state: battery[start_node]}
    result = None
    max_cost = None

    while queue:
        item = heappop(queue)
        state = item.curr_state

        if state.length == max_path_length:
            if max_cost is None or item.cost_so_far >= max_cost:
                max_cost = item.cost_so_far
                result = item
            continue

        for target in graph[state.node]:
            target_state = State(node=target, length=state.length + 1)
            prev = maxs.get(target_state, None)
            next_cost = int(f"{item.cost_so_far}{battery[target]}")
            if prev is None or next_cost > prev:
                maxs[target_state] = next_cost
                heappush(queue, QueueItem(next_cost, target_state, item))

    return result


def solve(data: list[list[int]], pbar_position):
    total_res = 0
    max_path_length = 12
    for battery in tqdm(data, position=pbar_position):
        G = make_graph(battery)
        res = 0
        for i in range(len(battery)):
            out = longest_path_with_length_of_n(battery, G, i, max_path_length)
            if not out:
                break
            res = max(res, out.cost_so_far)
        total_res += res
    return total_res


@aoc_part(2)
def solve_pt2():
    data = load_input()
    return sum(generic_parallel_execution(solve, data, workers=8, add_pbar=True))


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
