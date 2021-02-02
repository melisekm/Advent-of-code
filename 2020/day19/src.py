import timeit


def solve_pt1(vstup):
    def posud(line, rules):
        pass

    def get_rule(cisla):
        rule = []
        for cislo in cisla.strip().split(" "):
            try:
                rule.append(int(cislo))
            except ValueError:
                rule.append(cislo.replace('"', ""))
        return rule

    rules = {}
    with open(vstup, "r") as file:
        lines = file.readlines()
        idx = 0
        for line in lines:
            if line == "\n":
                break
            line = line.strip().split(":")
            idx = int(line[0])
            cisla = line[1].split("|")
            rule = []
            rule.append(get_rule(cisla[0]))
            if len(cisla) == 2:
                rule.append(get_rule(cisla[1]))
            rules[idx] = rule
            idx += 1
        res = 0
        for line in lines[idx + 1 :]:
            if posud(line, rules):
                res += 1

    return res


vstup = "day19/vstup.txt"

start = timeit.default_timer()
result1 = solve_pt1(vstup)
print(result1)
print(f"Cas vykonavania pt1:{timeit.default_timer() - start} sec")

"""
start = timeit.default_timer()
result2 = solve_pt2(vstup)
print(result2)
print(f"Cas vykonavania pt2:{timeit.default_timer() - start} sec")
"""
