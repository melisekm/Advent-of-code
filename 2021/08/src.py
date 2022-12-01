import copy
import itertools
import timeit
from collections import defaultdict


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip().split(" | ")
            first = line[0].split()
            second = line[1].split()
            res.append([first, second])
    return res


def solve_pt1():
    codes = {2, 4, 3, 7}
    f = load_input()
    res = 0
    for line in f:
        for code in line[1]:
            length = len(code)
            if length in codes:
                res += 1
    return res


def create_histogram(strings):
    res = defaultdict(list)
    for string in strings:
        res[len(string)].append(string)
    return res


to_remove = {
    0: {"length": 6, "pos": [3]},
    6: {"length": 6, "pos": [2]},
    9: {"length": 6, "pos": [4]},
    2: {"length": 5, "pos": [1, 5]},
    3: {"length": 5, "pos": [1, 4]},
    5: {"length": 5, "pos": [2, 4]},
}


def over_riesenie(combination, stringsInput):
    for k, v in to_remove.items():
        c_copy = copy.deepcopy(combination)
        remove = []
        for n in v["pos"]:
            remove.append(c_copy[n])
        for el in remove:
            c_copy.remove(el)
        c_copy.sort()
        good = False
        for string in stringsInput[v["length"]]:
            sortnuty = sorted(string)
            if c_copy == sortnuty:
                good = True
        if not good:
            return False
    return True


def vyjadri_output(board, codes):
    res = []
    res_map = {
        2: 1,
        3: 7,
        4: 4,
        7: 8,
    }

    for code in codes:
        if len(code) in res_map:
            res.append(res_map[len(code)])
        else:
            sortnuty = sorted(code)
            for k, v in to_remove.items():
                c_copy = copy.deepcopy(board)
                remove = []
                for n in v["pos"]:
                    remove.append(c_copy[n])
                for el in remove:
                    c_copy.remove(el)
                c_copy.sort()

                if c_copy == sortnuty:
                    res.append(k)

    return int("".join(list(map(str, res))))


pozicie = [
    [2, 5],
    [1, 3],
    [4, 6]
]


def solve_pt2():
    def solve_(i, code_):
        if i == 3:
            if over_riesenie(code_, histogram):
                return code_
        else:
            permutacie = list(itertools.permutations(important[i], 2))
            for mutate in permutacie:
                code_c = copy.deepcopy(code_)
                j = 0
                for pos in pozicie[i]:
                    code_c[pos] = mutate[j]
                    j += 1
                riesenie = solve_(i + 1, code_c)
                if riesenie:
                    return riesenie
        return None

    f = load_input()
    res = 0
    for line in f:
        output_codes = line[1][:]
        line[0].sort(key=lambda x: len(x))
        histogram = create_histogram(line[0])
        input_codes = list(map(lambda x: set(x), line[0]))
        code = ['X'] * 7
        code[0] = list(input_codes[1] - input_codes[0])[0]
        important = [input_codes[0], input_codes[2] - input_codes[0], input_codes[9] - input_codes[2] - input_codes[1]]
        vys = solve_(0, code)
        res += vyjadri_output(vys, output_codes)
    return res


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Cas vykonavania pt1:{end - start} sec")

start = timeit.default_timer()
result2 = solve_pt2()
end = timeit.default_timer()
print(result2)
print(f"Cas vykonavania pt2:{end - start} sec")
