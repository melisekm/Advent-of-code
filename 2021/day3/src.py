import timeit


def load_input(file_name="in.txt"):
    res = []
    with open(file_name) as f:
        for line in f:
            res.append(line.strip())
        return res


def solve_pt1():
    f = load_input()
    gamma = ""
    epsilon = ""
    for i in range(len(f[0])):
        ones = 0
        zeros = 0
        for code in f:
            if code[i] == "0":
                zeros += 1
            else:
                ones += 1
        if ones > zeros:
            mcb = "1"
            lcb = "0"
        else:
            mcb = "0"
            lcb = "1"
        gamma += mcb
        epsilon += lcb
    return int(gamma, 2) * int(epsilon, 2)


def solve_pt2():
    f = load_input()

    def prune_report(report, criteria):
        ones = []
        zeros = []
        for code in report:
            if code[i] == "0":
                zeros.append(code)
            else:
                ones.append(code)
        if criteria == "oxy":
            return ones if len(ones) >= len(zeros) else zeros
        return zeros if len(ones) >= len(zeros) else ones

    reportco2 = f[:]
    reportoxy = f[:]

    for i in range(len(f[0])):
        if len(reportco2) != 1:
            reportco2 = prune_report(reportco2, "co2")
        if len(reportoxy) != 1:
            reportoxy = prune_report(reportoxy, "oxy")

    return int(reportco2[0], 2) * int(reportoxy[0], 2)


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
