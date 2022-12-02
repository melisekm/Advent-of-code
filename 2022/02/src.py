import timeit


def convert_to_num(char, start):
    return ord(char) - ord(start) + 1


def calc_res(them, me):
    return (them + 3 - me) % 3


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            them, me = line.strip().split(' ')
            res.append((convert_to_num(them, 'A'), convert_to_num(me, 'X')))
    return res


def solve_pt1():
    data = load_input()
    outcome_map_1 = {
        0: 3,
        1: 0,
        2: 6
    }
    return sum(outcome_map_1[calc_res(them, me)] + me for them, me in data)


def solve_pt2():
    data = load_input()
    outcome_map_2 = {
        1: 1,
        2: 0,
        3: 2
    }
    total = 0
    for game in data:
        them, what_should_it_been = game
        for me in range(1, 4):
            if calc_res(them, me) == outcome_map_2[what_should_it_been]:
                total += me + (what_should_it_been - 1) * 3
                break

    return total


def run_part(solve_fn, part_idx):
    start = timeit.default_timer()
    result = solve_fn()
    end = timeit.default_timer()
    print(result)
    print(f"Total time pt{part_idx}: {(end - start):.3f} sec")


run_part(solve_pt1, 1)
run_part(solve_pt2, 2)
