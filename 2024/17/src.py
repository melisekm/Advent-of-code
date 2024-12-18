import dataclasses
import re

from utils import aoc_part


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        registers, program = f.read().split("\n\n")
        return (
            list(map(int, re.findall(r'\d+', registers))),
            list(map(int, re.findall(r'\d+', program)))
        )


@dataclasses.dataclass
class CPU:
    A: int
    B: int
    C: int
    ptr: int
    output: list[int] = dataclasses.field(default_factory=list)

    def __post_init__(self):
        self.op_map = [
            self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv
        ]

    def resolve_combo(self, lit):
        if 0 <= lit <= 3:
            return lit
        if lit == 4:
            return self.A
        if lit == 5:
            return self.B
        if lit == 6:
            return self.C

    def dv(self, lit):
        return self.A // 2 ** self.resolve_combo(lit)

    def adv(self, lit):
        self.A = self.dv(lit)

    def bxl(self, lit):
        self.B ^= lit

    def bst(self, lit):
        self.B = self.resolve_combo(lit) % 8

    def jnz(self, lit):
        if self.A == 0:
            return
        self.ptr = lit

    def bxc(self, lit):
        self.B ^= self.C

    def out(self, lit):
        self.output.append(self.resolve_combo(lit) % 8)

    def bdv(self, lit):
        self.B = self.dv(lit)

    def cdv(self, lit):
        self.C = self.dv(lit)


@aoc_part(1)
def solve_pt1():
    registers, program = load_input()
    cpu = CPU(*registers, 0)
    while cpu.ptr < len(program):
        opcode, operand = program[cpu.ptr], program[cpu.ptr + 1]
        fn = cpu.op_map[opcode]
        fn(operand)
        if opcode == 3 and cpu.A != 0:
            continue
        cpu.ptr += 2
    return ",".join(map(str, cpu.output))


if __name__ == '__main__':
    solve_pt1()
