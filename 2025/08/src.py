from dataclasses import dataclass
from functools import reduce

from utils import aoc_part


@dataclass
class Circuit:
    v3s: set[int]

    @property
    def size(self):
        return len(self.v3s)

    def __repr__(self):
        return f'Circuit(size={self.size})'


@dataclass(frozen=True)
class V3:
    x: int
    y: int
    z: int


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = list(map(int, line.strip().split(",")))
            res.append(V3(*line))
    return res


def v3_distance(a: V3, b: V3) -> float:
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2) ** 0.5


def solve(pt: int) -> int:
    data = load_input()
    max_connections = 1000

    distances = {}
    for x in data:
        for y in data:
            if x is y:
                continue
            if (x, y) in distances or (y, x) in distances:
                continue
            dist = v3_distance(x, y)
            distances[(x, y)] = dist

    circuits = []
    sorted_pairs = sorted(distances, key=distances.get)
    for idx, pair in enumerate(sorted_pairs):
        if pt == 1 and idx == max_connections:
            # end after n connections
            break

        comb1, comb2 = pair
        found_circuits = []
        for circuit in circuits:
            if len(found_circuits) == 2: break  # each comb can belong to one circ max

            if comb1 in circuit.v3s:
                found_circuits.append(circuit)
                continue
            if comb2 in circuit.v3s:
                found_circuits.append(circuit)

        if len(found_circuits) == 2:
            ## merge two circuits
            found_circuits[0].v3s.update(found_circuits[1].v3s)
            circuits.remove(found_circuits[1])
        else:
            if not found_circuits:
                # create new circuit
                found_circuits.append(Circuit(set()))
                circuits.append(found_circuits[0])

            # append to circuit, at this point there can only be 1 found circuit
            found_circuits[0].v3s.update([comb1, comb2])

        if pt == 2 and len(circuits) == 1 and len(circuits[0].v3s) == len(data):
            # end if there is only one large circuit
            return comb1.x * comb2.x

    circuits.sort(key=lambda x: x.size, reverse=True)
    return reduce(lambda x, y: x * y, [c.size for c in circuits[:3]])


@aoc_part(1)
def solve_pt1():
    return solve(pt=1)


@aoc_part(2)
def solve_pt2():
    return solve(pt=2)


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
