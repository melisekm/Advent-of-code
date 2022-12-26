from utils import aoc_part
import re


class Node:
    def __init__(self, name, rate, neighbors):
        self.name = name
        self.rate = rate
        self.neighbors = neighbors
        self.distances = None

    def calculate_distances_to_all_nodes(self):
        distances = {self: 0}
        queue = [self]
        while queue:
            node = queue.pop(0)
            for neighbor in node.neighbors:
                if neighbor not in distances:
                    distances[neighbor] = distances[node] + 1
                    queue.append(neighbor)
        # get rid of self, and nodes which have rate 0
        distances = {k: v + 1 for k, v in distances.items() if k != self and k.rate != 0}
        self.distances = distances

    def __repr__(self):
        return f'{self.name}: rate={self.rate}, neighbors={[c.name for c in self.neighbors]}'

    def __str__(self):
        return self.__repr__()


def load_input(file_name="in.txt"):
    nodes = {}
    with open(file_name) as f:
        for line in f:
            line = re.findall(r'\b[A-Z0-9]{1,}\b', line)
            node_name = line[0]
            rate = int(line[1])
            neighbors = []
            if node_name not in nodes:
                node = Node(node_name, rate, neighbors)
                nodes[node_name] = node
            else:
                node = nodes[node_name]
                node.rate = rate

            for child in line[2:]:
                if child not in nodes:
                    nodes[child] = Node(child, 0, [])
                node.neighbors.append(nodes[child])
    return nodes


@aoc_part(1)
def solve_pt1():
    raise NotImplementedError
    nodes = load_input()
    for node in nodes:
        nodes[node].calculate_distances_to_all_nodes()
    first_node = nodes['AA']

    max_minute = 1000
    DP = [(0, [])] * max_minute
    DP[0] = (first_node.rate, [first_node])

    for minute in range(max_minute):
        rate, path = DP[minute]
        if not path:
            # DP[minute] =
            continue
        last_node = path[-1]
        for node, distance in last_node.distances.items():
            if node not in path:
                rate_at_distance = rate + sum(pathnode.rate for pathnode in path) * distance + node.rate
                if distance + minute < max_minute and DP[distance + minute][0] < rate_at_distance:
                    DP[distance + minute] = (rate_at_distance, path + [node])
        pass
    pass


#

@aoc_part(2)
def solve_pt2():
    data = load_input()
    pass


# solve_pt1()
# solve_pt2()
