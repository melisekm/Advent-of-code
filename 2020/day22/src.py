import timeit
import copy


def solve_pt1(vstup):
    def playGame(p1, p2):
        end = len(p1) + len(p2)
        while len(p1) != end and len(p2) != end:
            r1 = p1.pop(0)
            r2 = p2.pop(0)
            if r1 > r2:
                p1.append(r1)
                p1.append(r2)
            else:
                p2.append(r2)
                p2.append(r1)
        return p1 if len(p1) == end else p2

    def calcResult(winner):
        res = 0
        for i, card in enumerate(winner[::-1], start=1):
            res += card * i
        return res

    with open(vstup, "r") as file:
        k = []
        file.readline()
        for line in file:
            if "Player" in line:
                p1 = copy.deepcopy(k)
                k.clear()
                continue
            if line == "\n":
                continue
            k.append(int(line.strip()))
        p2 = copy.deepcopy(k)
        winner = playGame(p1, p2)
        res = calcResult(winner)

    return res


def solve_pt2(vstup):
    class Player:
        def __init__(self, desk):
            self.desk = desk
            self.configurations = []

    def playGame(p1, p2):
        end = len(p1.desk) + len(p2.desk)
        while len(p1.desk) != end and len(p2.desk) != end:
            if p1.desk in p1.configurations or p2.desk in p2.configurations:
                return (p1, 1)
            p1.configurations.append(copy.deepcopy(p1.desk))
            p2.configurations.append(copy.deepcopy(p2.desk))
            r1 = p1.desk.pop(0)
            r2 = p2.desk.pop(0)
            if len(p1.desk) >= r1 and len(p2.desk) >= r2:
                _, idx = playGame(Player(p1.desk[:r1]), Player(p2.desk[:r2]))
                if idx == 1:
                    p1.desk.append(r1)
                    p1.desk.append(r2)
                else:
                    p2.desk.append(r2)
                    p2.desk.append(r1)
            else:
                if r1 > r2:
                    p1.desk.append(r1)
                    p1.desk.append(r2)
                else:
                    p2.desk.append(r2)
                    p2.desk.append(r1)

        return (p1, 1) if len(p1.desk) == end else (p2, 2)

    def calcResult(winner):
        res = 0
        for i, card in enumerate(winner[::-1], start=1):
            res += card * i
        return res

    with open(vstup, "r") as file:
        k = []
        file.readline()
        for line in file:
            if "Player" in line:
                p1 = copy.deepcopy(k)
                k.clear()
                continue
            if line == "\n":
                continue
            k.append(int(line.strip()))
        p2 = copy.deepcopy(k)

        winner, _ = playGame(Player(p1), Player(p2))

        res = calcResult(winner.desk)
        return res


vstup = "vstup.txt"

start = timeit.default_timer()
result1 = solve_pt1(vstup)
print(result1)
print(f"Cas vykonavania pt1:{timeit.default_timer() - start} sec")


start = timeit.default_timer()
result2 = solve_pt2(vstup)
print(result2)
print(f"Cas vykonavania pt2:{timeit.default_timer() - start} sec")
