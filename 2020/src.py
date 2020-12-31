import timeit
import copy


def solve_pt1(vstup):
    ACTIVE = "#"
    INACTIVE = "."

    class Point:
        def __init__(self, x, y, z, symbol):
            self.x = x
            self.y = y
            self.z = z
            self.symbol = symbol

    def make_pos(x, y, z):
        return f"{x},{y},{z}"

    def check_neighbors(point, priestor):
        active = 0
        for x in [-1, 0, 1]:
            new_x = point.x + x
            for y in [-1, 0, 1]:
                new_y = point.y + y
                for z in [-1, 0, 1]:
                    new_z = point.z + z
                    suradnice = make_pos(new_x, new_y, new_z)
                    sused = priestor.get(suradnice, None)
                    if sused is None or sused == point:
                        continue
                    if sused.symbol == ACTIVE:
                        active += 1

        if point.symbol == INACTIVE and active == 3:
            return ACTIVE
        if point.symbol == ACTIVE:
            if 2 <= active <= 3:
                return None
            else:
                return INACTIVE
        else:
            return None

    def pridaj_rohove_body(orig):
        for point in list(priestor.values()):
            for x in [-1, 0, 1]:
                new_x = point.x + x
                for y in [-1, 0, 1]:
                    new_y = point.y + y
                    for z in [-1, 0, 1]:
                        new_z = point.z + z
                        suradnice = make_pos(new_x, new_y, new_z)
                        sused = orig.get(suradnice, None)
                        if sused is None:
                            orig[suradnice] = Point(new_x, new_y, new_z, INACTIVE)

    def vykonaj_zmeny(priestor):
        to_change = []
        pridaj_rohove_body(priestor)
        for point in list(priestor.values()):
            symbol = check_neighbors(point, priestor)
            if symbol:
                changed = copy.deepcopy(point)
                changed.symbol = symbol
                to_change.append(changed)
        for changed in to_change:
            pos = make_pos(changed.x, changed.y, changed.z)
            priestor[pos] = changed

    def vyries(priestor):
        for _ in range(6):
            vykonaj_zmeny(priestor)

        res = 0
        for point in priestor.values():
            if point.symbol == ACTIVE:
                res += 1
        return res

    with open(vstup, "r") as file:
        priestor = {}
        y = 0
        for line in file:
            x = 0
            line = line.strip()
            for char in line:
                pos = make_pos(x, y, 0)
                priestor[pos] = Point(x, y, 0, char)
                x += 1
            y += 1

    return vyries(priestor)


def solve_pt2(vstup):
    ACTIVE = "#"
    INACTIVE = "."

    class Point:
        def __init__(self, x, y, z, w, symbol):
            self.x = x
            self.y = y
            self.z = z
            self.w = w
            self.symbol = symbol

    def make_pos(x, y, z, w):
        return f"{x},{y},{z},{w}"

    def check_neighbors(point, priestor):
        active = 0
        for x in [-1, 0, 1]:
            new_x = point.x + x
            for y in [-1, 0, 1]:
                new_y = point.y + y
                for z in [-1, 0, 1]:
                    new_z = point.z + z
                    for w in [-1, 0, 1]:
                        new_w = point.w + w
                        suradnice = make_pos(new_x, new_y, new_z, new_w)
                        sused = priestor.get(suradnice, None)
                        if sused is None or sused == point:
                            continue
                        if sused.symbol == ACTIVE:
                            active += 1

        if point.symbol == INACTIVE and active == 3:
            return ACTIVE
        if point.symbol == ACTIVE:
            if 2 <= active <= 3:
                return None
            else:
                return INACTIVE
        else:
            return None

    def pridaj_rohove_body(orig):
        for point in list(priestor.values()):
            for x in [-1, 0, 1]:
                new_x = point.x + x
                for y in [-1, 0, 1]:
                    new_y = point.y + y
                    for z in [-1, 0, 1]:
                        new_z = point.z + z
                        for w in [-1, 0, 1]:
                            new_w = point.w + w
                            suradnice = make_pos(new_x, new_y, new_z, new_w)
                            sused = orig.get(suradnice, None)
                            if sused is None:
                                orig[suradnice] = Point(new_x, new_y, new_z, new_w, INACTIVE)

    def vykonaj_zmeny(priestor):
        to_change = []
        pridaj_rohove_body(priestor)
        for point in list(priestor.values()):
            symbol = check_neighbors(point, priestor)
            if symbol:
                changed = copy.deepcopy(point)
                changed.symbol = symbol
                to_change.append(changed)
        for changed in to_change:
            pos = make_pos(changed.x, changed.y, changed.z, changed.w)
            priestor[pos] = changed

    def vyries(priestor):
        for _ in range(6):
            vykonaj_zmeny(priestor)

        res = 0
        for point in priestor.values():
            if point.symbol == ACTIVE:
                res += 1
        return res

    with open(vstup, "r") as file:
        priestor = {}
        y = 0
        for line in file:
            x = 0
            line = line.strip()
            for char in line:
                pos = make_pos(x, y, 0, 0)
                priestor[pos] = Point(x, y, 0, 0, char)
                x += 1
            y += 1

    return vyries(priestor)


vstup = "vstup.txt"

start = timeit.default_timer()
result1 = solve_pt1(vstup)
print(result1)
print(f"Cas vykonavania pt1:{timeit.default_timer() - start} sec")


start = timeit.default_timer()
result2 = solve_pt2(vstup)
print(result2)
print(f"Cas vykonavania pt2:{timeit.default_timer() - start} sec")
