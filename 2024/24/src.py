import re
from dataclasses import dataclass
from enum import StrEnum

from utils import aoc_part


class Gate(StrEnum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"


@dataclass
class Instruction:
    wire1: str
    gate: Gate
    wire2: str
    target: str


def load_input(file_name="2024/24/in.txt"):
    res = []
    states = {}
    with open(file_name) as f:
        initial, pairs = f.read().split("\n\n")
        for line in initial.split("\n"):
            name, value = line.split(": ")
            states[name] = int(value.strip())
        for line in pairs.split("\n"):
            parsed_line = re.search(r'(\w{3}) (\w{2,3}) (\w{3}) -> (\w{3})', line)
            if parsed_line:
                res.append(
                    Instruction(
                        parsed_line.group(1), Gate(parsed_line.group(2)),
                        parsed_line.group(3), parsed_line.group(4))
                )

    return states, res


@aoc_part(1)
def solve_pt1():
    states, instructions = load_input()
    perform_instructions(instructions, states)
    return bin2num(states, 'z')


def perform_instructions(instructions, states):
    ptr = 0
    seen = set()
    while len(seen) != len(instructions):
        if ptr in seen:
            ptr += 1
            continue
        instruction = instructions[ptr]
        if instruction.wire1 in states and instruction.wire2 in states:
            state1 = states[instruction.wire1]
            state2 = states[instruction.wire2]
            if instruction.gate == Gate.AND:
                states[instruction.target] = state1 & state2
            elif instruction.gate == Gate.OR:
                states[instruction.target] = state1 | state2
            elif instruction.gate == Gate.XOR:
                states[instruction.target] = state1 ^ state2
            seen.add(ptr)
            ptr = 0
        else:
            ptr += 1


def bin2num(states, char):
    res = ""
    for state, val in sorted(states.items(), key=lambda x: x[0]):
        if state.startswith(char):
            res = str(val) + res
    return int(res, 2)


@aoc_part(2)
def solve_pt2():
    pass


if __name__ == '__main__':
    solve_pt1()
    # solve_pt2()
