import math


def solve_pt1(vstup):
    def zisti(earliest, departure):
        return (earliest // departure) * departure + departure

    with open(vstup, "r") as file:
        lines = file.readlines()
        earliest = int(lines[0].strip())
        busses = lines[1].split(",")
        departures = [int(x) for x in busses if x != "x"]
        _min = math.inf
        index = 0
        for idx, departure in enumerate(departures):
            cislo = zisti(earliest, departure)
            if cislo < _min:
                _min = cislo
                index = idx
        return (_min - earliest) * departures[index]


def solve_pt2(vstup):
    def zisti(a, b):
        return (a // b) * b

    def max_val_index(departures):
        val = max([x[0] for x in departures])
        idx = [x[0] for x in departures].index(val)
        return val, idx

    def vyries(departures):
        curr = 0
        max_val, max_idx = max_val_index(departures)
        while True:
            curr += max_val
            cntr = 0
            for idx, departure in enumerate(departures):
                if idx == max_idx:
                    continue
                zistil = zisti(curr, departure[0])
                if idx > max_idx:
                    zistil += departure[0]
                if zistil == curr - departures[max_idx][1] + departure[1]:
                    cntr += 1
                else:
                    break
            if cntr == len(departures) - 1:
                return curr - departures[max_idx][1]

    with open(vstup, "r") as file:
        lines = file.readlines()
        busses = lines[1].split(",")
        departures = [(int(x), idx) for idx, x in enumerate(busses) if x != "x"]

    return vyries(departures)


vstup = "vstup.txt"
result1 = solve_pt1(vstup)
result2 = solve_pt2(vstup)
print(result1)
print(result2)
