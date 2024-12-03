from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            res.append(line)
    return res


@aoc_part(1)
def solve_pt1():
    data = load_input()

    pass


# @aoc_part(2)
# def solve_pt2():
#     data = load_input()
#
#     pass

if __name__ == '__main__':
    solve_pt1()
    # solve_pt2()
