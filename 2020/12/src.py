def solve_pt1(vstup):
    class Lod:
        def __init__(self, facing):
            self.facing = facing
            self.pos = [0, 0]
            self.cislo_smer = ["N", "E", "S", "W"]

        def convert(self, cislo):
            return self.cislo_smer[cislo]

        def otoc(self, smer, hodnota):
            if hodnota == 90:
                res = 1
            elif hodnota == 180:
                res = 2
            elif hodnota == 270:
                res = 3
            if smer == "L":
                self.facing = abs((self.facing - res) % 4)
            else:
                self.facing = abs((self.facing + res) % 4)

        def pohni(self, smer, hodnota):
            if smer == "N":
                self.pos[1] += hodnota
            elif smer == "S":
                self.pos[1] -= hodnota
            elif smer == "E":
                self.pos[0] += hodnota
            elif smer == "W":
                self.pos[0] -= hodnota

        def vykonaj(self, instrukcia):
            smer = instrukcia[0]
            hodnota = instrukcia[1]
            if smer in ("L", "R"):
                self.otoc(smer, hodnota)
            elif smer in ("N", "S", "E", "W"):
                self.pohni(smer, hodnota)
            else:
                self.pohni(self.cislo_smer[self.facing], hodnota)

    lod = Lod(1)
    with open(vstup, "r") as file:
        for line in file:
            line = line.strip()
            cmd = line[0]
            num = int(line[1:])
            lod.vykonaj((cmd, num))
    return abs(lod.pos[0]) + abs(lod.pos[1])


def solve_pt2(vstup):
    class Lod:
        def __init__(self):
            self.pos = [0, 0]
            self.waypoint_pos = [10, 1]

        def forward(self, hodnota):
            self.pos[0] += hodnota * self.waypoint_pos[0]
            self.pos[1] += hodnota * self.waypoint_pos[1]

        def move_waypoint(self, smer, hodnota):
            if smer == "N":
                self.waypoint_pos[1] += hodnota
            elif smer == "S":
                self.waypoint_pos[1] -= hodnota
            elif smer == "E":
                self.waypoint_pos[0] += hodnota
            elif smer == "W":
                self.waypoint_pos[0] -= hodnota

        def rotate_waypoint(self, smer, hodnota):
            if hodnota == 180:
                self.waypoint_pos[0] *= -1
                self.waypoint_pos[1] *= -1
            elif smer == "R" and hodnota == 90 or smer == "L" and hodnota == 270:
                self.waypoint_pos[0], self.waypoint_pos[1] = self.waypoint_pos[1], -self.waypoint_pos[0]
            else:
                self.waypoint_pos[0], self.waypoint_pos[1] = -self.waypoint_pos[1], self.waypoint_pos[0]

        def vykonaj(self, instrukcia):
            smer = instrukcia[0]
            hodnota = instrukcia[1]
            if smer in ("L", "R"):
                self.rotate_waypoint(smer, hodnota)
            elif smer in ("N", "S", "E", "W"):
                self.move_waypoint(smer, hodnota)
            else:
                self.forward(hodnota)

    lod = Lod()
    with open(vstup, "r") as file:
        for line in file:
            line = line.strip()
            cmd = line[0]
            num = int(line[1:])
            lod.vykonaj((cmd, num))
    return abs(lod.pos[0]) + abs(lod.pos[1])


vstup = "vstup.txt"
result1 = solve_pt1(vstup)
result2 = solve_pt2(vstup)
print(result1)
print(result2)
