def check_passport1(passport_data):
    data = {
        "byr": 0,
        "iyr": 0,
        "eyr": 0,
        "hgt": 0,
        "hcl": 0,
        "ecl": 0,
        "pid": 0,
    }
    for line in passport_data:
        for udaj in line:
            typ = udaj.split(":")[0]
            data[typ] = 1
    for value in data.values():
        if value != 1:
            return False
    return True


def solve_pt1(vstup):
    pocet = 0
    with open(vstup, "r") as file:
        passport_data = []
        while True:
            line = file.readline()
            if line == "\n" or not line:
                if check_passport1(passport_data):
                    pocet += 1
                passport_data = []
            else:
                passport_data.append(line.strip().split(" "))
            if not line:
                break
    return pocet


def check_range(hodnota, l_index, r_index):
    return l_index <= hodnota <= r_index


def valid(typ, data):
    if typ == "byr":
        if len(data) == 4:
            return check_range(int(data), 1920, 2002)
    elif typ == "iyr":
        if len(data) == 4:
            return check_range(int(data), 2010, 2020)
    elif typ == "eyr":
        if len(data) == 4:
            return check_range(int(data), 2020, 2030)
    elif typ == "hgt":
        try:
            if data[-2:] == "cm":
                return check_range(int(data[:-2]), 150, 193)
            elif data[-2:] == "in":
                return check_range(int(data[:-2]), 59, 76)
        except ValueError:
            return False
    elif typ == "hcl":
        if data[0] == "#":
            if len(data[1:]) == 6:
                try:
                    int(data[1:], 16)
                except ValueError:
                    return False
                else:
                    return True
    elif typ == "ecl":
        return data in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    elif typ == "pid":
        return len(data) == 9
    elif typ == "cid":
        return True
    return False


def check_passport2(passport_data):
    data = {
        "byr": 0,
        "iyr": 0,
        "eyr": 0,
        "hgt": 0,
        "hcl": 0,
        "ecl": 0,
        "pid": 0,
    }
    for line in passport_data:
        for udaj in line:
            precitane_udaje = udaj.split(":")
            if not valid(precitane_udaje[0], precitane_udaje[1]):
                return False
            data[precitane_udaje[0]] = 1
    for value in data.values():
        if value != 1:
            return False
    return True


def solve_pt2(vstup):
    pocet = 0
    with open(vstup, "r") as file:
        passport_data = []
        while True:
            line = file.readline()
            if line == "\n" or not line:
                if check_passport2(passport_data):
                    pocet += 1
                passport_data = []
            else:
                passport_data.append(line.strip().split(" "))
            if not line:
                break
    return pocet


vstup = "vstup.txt"
result1 = solve_pt1(vstup)
result2 = solve_pt2(vstup)
print(result1)
print(result2)
