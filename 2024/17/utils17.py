import dataclasses
import re


def make_output(output: list[int]):
    return int("".join(map(str, output)))


def load_input(file_name="in.txt") -> list[int]:
    with open(file_name) as f:
        registers, program = f.read().split("\n\n")
        return list(map(int, re.findall(r'\d+', program)))


program = load_input()
expected_output = make_output(program)


@dataclasses.dataclass
class CPU:
    A: int
    B: int = 0
    C: int = 0
    ptr: int = 0
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