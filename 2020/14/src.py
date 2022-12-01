def solve_pt1(vstup):
    def zapis_cislo(maska, hodnota):
        res = 0
        for idx, bit in enumerate(reversed(maska)):
            if bit == "1" or (bit == "X" and hodnota & (1 << idx)):
                res |= 1 << idx
        return res

    mem = {}
    with open(vstup, "r") as file:
        for line in file:
            line = line.strip().split()
            premenna = line[0]
            hodnota = line[2]
            if premenna == "mask":
                maska = hodnota
            else:
                mem_id = premenna[4:-1]
                mem[mem_id] = zapis_cislo(maska, int(hodnota))
    return sum(list(mem.values()))


def solve_pt2(vstup):
    def vytvor_address_space(maska, mem_id):
        res = ["0"] * 36
        pocet_X = 0
        for idx, bit in enumerate(reversed(maska)):
            if bit == "X":
                pocet_X += 1
                res[idx] = "X"
            elif bit == "0":
                unchanged = mem_id & (1 << idx)
                if unchanged:
                    res[idx] = "1"
                else:
                    res[idx] = "0"
            else:
                res[idx] = "1"
        return pocet_X, res

    def vytvor_kombinacie(pocet):
        res = []
        for i in range(2 ** pocet):
            binarne_cislo = bin(i)[2:].zfill(pocet)
            res.append(binarne_cislo)
        return res

    def ziskaj_adresy(result, kombinacie):
        adresy = []
        for kombinacia in kombinacie:
            adresa = []
            komb_id = 0
            for bit in result:
                if bit == "X":
                    adresa.append(kombinacia[komb_id])
                    komb_id += 1
                else:
                    adresa.append(bit)
            adresa_str = "".join(adresa)
            adresy.append(int(adresa_str[::-1], 2))
        return adresy

    def zapis_cisla(mem, adresy, hodnota):
        for adresa in adresy:
            mem[adresa] = hodnota

    def zapis_cislo(mem, maska, hodnota, mem_id):
        pocet_X, result = vytvor_address_space(maska, mem_id)
        kombinacie = vytvor_kombinacie(pocet_X)
        adresy = ziskaj_adresy(result, kombinacie)
        zapis_cisla(mem, adresy, hodnota)

    mem = {}
    with open(vstup, "r") as file:
        for line in file:
            line = line.strip().split()
            premenna = line[0]
            hodnota = line[2]
            if premenna == "mask":
                maska = hodnota
            else:
                mem_id = premenna[4:-1]
                zapis_cislo(mem, maska, int(hodnota), int(mem_id))
    return sum(list(mem.values()))


vstup = "vstup.txt"
result1 = solve_pt1(vstup)
result2 = solve_pt2(vstup)
print(result1)
print(result2)
