class Slope:
    def __init__(self, right, down):
        self.x = self.y = self.pocet = 0
        self.right = right
        self.down = down
        self.end = False

    def check(self, size_x, size_y, mapa):
        if self.end is True:
            return
        self.x = (self.x + self.right) % size_x
        self.y = self.y + self.down
        if self.y >= size_y:
            self.end = True
            return
        if mapa[self.y][self.x] == "#":
            self.pocet += 1


def load_input(vstup):
    arr = []
    with open(vstup, "r") as file:
        for line in file:
            arr.append(line.strip())
    return arr


def koniec(slopes):
    end = 0
    for slope in slopes:
        if slope.end:
            end += 1
    return end == 5


def calc_result(slopes):
    pocet = 1
    for slope in slopes:
        pocet *= slope.pocet
    return pocet


def solve_pt1(vstup):
    mapa = load_input(vstup)
    size_y = len(mapa)
    size_x = len(mapa[0])
    x = y = pocet = 0
    while True:
        x = (x + 3) % size_x
        y = y + 1
        if y >= size_y:
            break
        if mapa[y][x] == "#":
            pocet += 1
    return pocet


def solve_pt2(vstup):
    mapa = load_input(vstup)
    size_y = len(mapa)
    size_x = len(mapa[0])
    slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]
    while not koniec(slopes):
        for slope in slopes:
            slope.check(size_x, size_y, mapa)

    return calc_result(slopes)


vstup = "vstup.txt"
result1 = solve_pt1(vstup)
result2 = solve_pt2(vstup)
print(result1)
print(result2)
