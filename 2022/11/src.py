import timeit
import re
from operator import mul, add


class Monkey:
    def __init__(self, idx):
        self.idx = idx
        self.items = []
        self.inspect = 0


def get_nums_from_line(line):
    return [int(num) for num in re.findall(r'\d+', line)]


def load_input(file_name="in.txt", pt=1, max_rounds=20):
    res = {}
    round_ = 0
    total_mod = 9699690
    with open(file_name) as f:
        f = f.readlines()
        while round_ != max_rounds:
            round_ += 1
            for monkey_lines in range(0, len(f), 7):
                monkey_lines = f[monkey_lines:monkey_lines + 7]
                monkey_id = get_nums_from_line(monkey_lines[0])[0]
                if monkey_id in res:
                    curr = res[monkey_id]
                else:
                    curr = Monkey(monkey_id)
                    res[monkey_id] = curr
                if round_ == 1:
                    items = get_nums_from_line(monkey_lines[1])
                    curr.items = items + curr.items

                operation = get_nums_from_line(monkey_lines[2])
                test = get_nums_from_line(monkey_lines[3])[0]
                true_result = get_nums_from_line(monkey_lines[4])[0]
                false_result = get_nums_from_line(monkey_lines[5])[0]

                op = mul if "*" in monkey_lines[2] else add

                for item in list(curr.items):
                    curr.inspect += 1
                    if len(operation) == 1:
                        worry = op(item, operation[0])
                    else:
                        worry = op(item, item)
                    if pt == 1:
                        worry //= 3
                    else:
                        worry %= total_mod

                    if worry % test == 0:
                        target = true_result
                    else:
                        target = false_result
                    if target not in res:
                        res[target] = Monkey(target)
                    curr.items.remove(item)
                    res[target].items.append(worry)

    return res


def solve_pt1():
    data = load_input(pt=1, max_rounds=20)
    sorted_data = sorted(data.values(), key=lambda x: x.inspect, reverse=True)[:2]
    return sorted_data[0].inspect * sorted_data[1].inspect


def solve_pt2():
    data = load_input(pt=2, max_rounds=10000)
    sorted_data = sorted(data.values(), key=lambda x: x.inspect, reverse=True)[:2]
    return sorted_data[0].inspect * sorted_data[1].inspect


def run_part(solve_fn, part_idx):
    start = timeit.default_timer()
    result = solve_fn()
    end = timeit.default_timer()
    print(result)
    print(f"Total time pt{part_idx}: {(end - start):.3f} sec")


run_part(solve_pt1, 1)
run_part(solve_pt2, 2)
