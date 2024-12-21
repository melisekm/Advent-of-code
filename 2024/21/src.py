import re
from enum import StrEnum

import networkx as nx
from tqdm import tqdm

from utils import aoc_part


def load_input(file_name="in.txt"):
    pad1 = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["#", "0", "A"]
    ]
    pad2 = [
        ['#', '^', 'A'],
        ['<', 'v', '>']
    ]
    with open(file_name, "r") as f:
        return f.read().splitlines(), pad1, pad2


class Button(StrEnum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'
    ACTIVATE = 'A'


def get_button(curr, target_node) -> Button:
    if curr[0] == target_node[0]:
        if curr[1] < target_node[1]:
            return Button.RIGHT
        else:
            return Button.LEFT
    else:
        if curr[0] < target_node[0]:
            return Button.DOWN
        else:
            return Button.UP


def path_to_buttons(path):
    return [get_button(x, y) for x, y in zip(path, path[1:])]


def create_graph(data, R, C, weight=1):
    G = nx.Graph()
    position_map = {}
    for r in range(R):
        for c in range(C):
            val = data[r][c]
            if val == "#":
                continue
            position_map[val] = (r, c)
            G.add_node((r, c), val=val)
            for dr in [-1, 1]:
                rr = r + dr
                if 0 <= rr < R:
                    new_val = data[rr][c]
                    if new_val != "#":
                        G.add_edge((r, c), (rr, c), weight=weight)
            for dc in [-1, 1]:
                cc = c + dc
                if 0 <= cc < C:
                    new_val = data[r][cc]
                    if new_val != "#":
                        G.add_edge((r, c), (r, cc), weight=weight)
    return G, position_map


def press_all_btns(to_press: list, graph: nx.Graph, position_map: dict):
    main_directions = []
    start_pos = position_map['A']
    for next_point in to_press:
        if hasattr(next_point, 'value'):
            next_point = next_point.value
        next_point_pos = position_map[next_point]
        paths = nx.all_shortest_paths(graph, start_pos, next_point_pos, weight='weight')
        new_directions = []
        for path in paths:
            directions = path_to_buttons(path)
            directions.append(Button.ACTIVATE)
            new_directions.append(directions)

        if not main_directions:
            main_directions = new_directions
        else:
            extended_main_direction = []
            for main_direction in main_directions:
                for new_direction in new_directions:
                    extended_main_direction.append(main_direction + new_direction)
            main_directions = extended_main_direction
        start_pos = next_point_pos

    return main_directions


def recurse(parent_paths, directional_keypad_G, directional_position_map, bot_id, max_id):
    if bot_id == max_id:
        return len(min(parent_paths, key=len))
    shortest = float('inf')
    for parent_path in parent_paths:
        this_paths = press_all_btns(
            parent_path,
            directional_keypad_G,
            directional_position_map
        )
        shortest = min(
            recurse(this_paths, directional_keypad_G, directional_position_map, bot_id + 1, max_id),
            shortest
        )
    return shortest


@aoc_part(1)
def solve_pt1():
    data, pad1, pad2 = load_input()
    numeric_keypad_G, numeric_position_map = create_graph(pad1, len(pad1), len(pad1[0]), 1)
    directional_keypad_G, directional_position_map = create_graph(pad2, len(pad2), len(pad2[0]), 1)

    res = 0
    for code in tqdm(data):
        code_nums = re.search(r'\d+', code).group()
        code = list(code)
        main_directions_all_paths = press_all_btns(
            code, numeric_keypad_G, numeric_position_map
        )

        shortest = recurse(
            main_directions_all_paths, directional_keypad_G, directional_position_map,
            bot_id=0, max_id=2
        )

        res += shortest * int(code_nums)

    return res


# @aoc_part(2)
# def solve_pt2():
#     data = load_input()
#
#     pass

if __name__ == '__main__':
    solve_pt1()
    # solve_pt2()
