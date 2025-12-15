from collections import deque
import re

import helpers2025
from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            toggles = re.search(r"\[(.*?)]", line).group(1)
            btns = [[int(i) for i in x.split(",")] for x in re.findall(r"\((.*?)\)", line)]
            pt2_goal = helpers2025.get_all_integers_from_string(re.search(r"{(.*?)}", line).group(1))
            res.append((toggles, btns, pt2_goal))
    return res


def solve(buttons: list[int], goal: int) -> int:
    queue = deque([(button ^ 0, 1) for button in buttons])
    visited = set()

    while queue:
        state, curr = queue.popleft()
        if state == goal:
            return curr

        if state in visited:
            continue
        visited.add(state)


        for btn in buttons:
            queue.append((state ^ btn, curr + 1))


@aoc_part(1)
def solve_pt1():
    data = load_input()
    ans = 0
    for d in data:
        toggles, btns, _ = d
        buttons = []
        for btn in btns:
            s = ["0"] * len(toggles)
            for i in btn:
                s[i] = "1"
            joined = "".join(s)
            num = int(joined, 2)
            buttons.append(num)
        goal = int(toggles.replace(".", "0").replace("#", "1"), 2)
        ans += solve(buttons, goal)
    return ans


def _add(state: list[int], button: list[int]) -> tuple:
    n = [x for x in state]
    for i in range(len(button)):
        n[i] = state[i] + button[i]
    return tuple(n)


def solve2(buttons: list[list[int]], pt2_goal: list[int]) -> int:
    pt2_goal = tuple(pt2_goal)
    initial_state = [0] * len(pt2_goal)
    queue = deque([(_add(initial_state, button), 1) for button in buttons])
    DP = {}

    while queue:
        state, curr = queue.popleft()

        if state not in DP:
            DP[state] = curr
        else:
            if curr >= DP[state]:
                continue
            else:
                DP[state] = curr

        if state == pt2_goal:
            return curr
        print(len(queue), state, curr)

        for btn in buttons:
            queue.append((_add(state, btn), curr + 1))


@aoc_part(2)
def solve_pt2():
    data = load_input()
    ans = 0
    for d in data:
        _, btns, pt2_goal = d
        buttons = []
        for btn in btns:
            s = [0] * len(pt2_goal)
            for i in btn:
                s[i] = 1
            buttons.append(s)
        ans += solve2(buttons, pt2_goal)
        # break
    return ans


if __name__ == '__main__':
    solve_pt1()
    # solve_pt2()
