import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip().split()
            if len(line) == 2:
                line[1] = int(line[1])
            res.append(line)
    return res


def solve_pt1():
    data = load_input()
    X = 1
    cycles_total = 0
    cycles_to_watch = [20, 60, 100, 140, 180, 220]
    accum = 0
    for instruction in data:
        if instruction[0] == 'noop':
            op, num, cycles = instruction[0], None, 1
        else:
            op, num, cycles = instruction[0], instruction[1], 2
        for cycle in range(cycles):
            cycles_total += 1
            if cycles_total in cycles_to_watch:
                accum += cycles_total * X
        if op == "addx":
            X += num
    return accum


def draw(X, current_sprite):
    if 0 <= X < 40:
        current_sprite[X] = '#'


def solve_pt2():
    data = load_input()
    current_sprite = list('###') + list('.') * 37
    position = 0
    X = 1
    CRT_row = ''
    for instruction in data:
        if instruction[0] == 'noop':
            op, num, cycles = instruction[0], None, 1
        else:
            op, num, cycles = instruction[0], instruction[1], 2
        for cycle in range(cycles):
            CRT_row += current_sprite[position]
            position += 1
            if position == 40:
                position = 0
                CRT_row += '\n'
        if op == "addx":
            X += num
        current_sprite = list('.') * 40
        draw(X, current_sprite)
        draw(X - 1, current_sprite)
        draw(X + 1, current_sprite)

    return CRT_row


def run_part(solve_fn, part_idx):
    start = timeit.default_timer()
    result = solve_fn()
    end = timeit.default_timer()
    print(result)
    print(f"Total time pt{part_idx}: {(end - start):.3f} sec")


run_part(solve_pt1, 1)
run_part(solve_pt2, 2)
