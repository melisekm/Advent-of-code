from tqdm import tqdm
from tqdm.contrib import tenumerate

from utils import generic_parallel_execution, aoc_part

SequenceList = list[dict[tuple[int, ...], int]]


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            res.append(int(line))
    return res


@aoc_part(1)
def solve_pt1():
    return sum(
        perform_calc(num) for num in load_input()
    )


def perform_calc(num):
    for _ in range(2000):
        num = next_val(num)
    return num


def next_val(num):
    tmp = num * 64
    num ^= tmp
    num %= 16777216
    tmp = num // 32
    num ^= tmp
    num %= 16777216
    tmp = num * 2048
    num ^= tmp
    num %= 16777216
    return num


@aoc_part(2)
def solve_pt2():
    data = load_input()
    all_sequences = []
    for num in tqdm(data, ascii=True):
        per_num_sequences = {}
        last_4 = []
        prev = None
        for i in range(2000):
            last_digit = num % 10
            if len(last_4) >= 4:
                last_4_tpl = tuple(last_4)
                if last_4_tpl not in per_num_sequences:
                    per_num_sequences[tuple(last_4)] = prev
                last_4.pop(0)
            if prev is not None:
                diff = last_digit - prev
                last_4.append(diff)

            num = next_val(num)
            prev = last_digit

        all_sequences.append(per_num_sequences)

    results = generic_parallel_execution(
        solve, all_sequences, all_sequences, workers=min(len(all_sequences), 6), add_pbar=True
    )
    return min(results)


def solve(all_sequences: SequenceList, full_sequence_list: SequenceList, pbar_position=None):
    best_subtotal = 0
    for idx, num_sequence_outer in tenumerate(all_sequences, ascii=True, position=pbar_position):
        for seq, val in num_sequence_outer.items():
            subtotal = val
            for jdx, num_sequence_inner in enumerate(full_sequence_list):
                if idx == jdx:
                    continue
                val2 = num_sequence_inner.get(seq, 0)
                subtotal += val2
            if subtotal >= best_subtotal:
                best_subtotal = subtotal
    return best_subtotal


if __name__ == '__main__':
    solve_pt1()
    solve_pt2()
