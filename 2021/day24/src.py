import timeit


class ALU:
    def __init__(self):
        self.vars = {"w": 0, "x": 0, "y": 0, "z": 0}

    def handle(self, instruction):
        cmd = instruction["command"]
        L = instruction.get("L", None)
        R = instruction.get("R", None)
        R = (self.vars[R] if isinstance(R, str) else R)
        if cmd == "inp":
            self.vars['w'] = R
        elif cmd == "add":
            self.vars[L] = self.vars[L] + R
        elif cmd == "mul":
            self.vars[L] = self.vars[L] * R
        elif cmd == "div":
            self.vars[L] = self.vars[L] // R
        elif cmd == "mod":
            self.vars[L] = self.vars[L] % R
        elif cmd == "eql":
            self.vars[L] = 1 if self.vars[L] == R else 0

    def __str__(self):
        return f"w={self.vars['w']},x={self.vars['x']},y={self.vars['y']},z={self.vars['z']}"


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip().split()
            instruction = {"command": line[0], "L": line[1]}
            if line[0] != "inp":
                try:
                    val = int(line[2])
                    instruction["R"] = val
                except ValueError:
                    instruction["R"] = line[2]
            res.append(instruction)
    return res


def solve_pt1():
    data = load_input()
    code = list(map(int, list("97919997299495")))
    alu = ALU()
    pos = 0
    for i, instruction in enumerate(data, start=1):
        if instruction["command"] == "inp":
            instruction["R"] = code[pos]
            pos += 1
        alu.handle(instruction)
    print(alu.vars['z'], code)


def solve_pt2():
    data = load_input()

    pass


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
# print(result1)
print(f"Total time pt1: {(end - start):.3f} sec")

# start = timeit.default_timer()
# result2 = solve_pt2()
# end = timeit.default_timer()
# print(result2)
# print(f"Total time pt2: {(end - start):.3f} sec")
