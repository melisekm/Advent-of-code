import timeit
from math import prod


def load_input(file_name="in.txt"):
    with open(file_name) as f:
        for line in f:
            return line.strip()


class Transmission:
    def __init__(self, message):
        self.packets = [Packet(self, message)]


class Packet:
    def __init__(self, transmission, binary):
        self.transmission = transmission
        self.version = int(binary[:3], 2)
        self.type = int(binary[3:6], 2)
        self.value = None
        self.lastpos = 0

    def decypher(self, binary):
        if self.type == 4:
            self.get_literals(binary)
        else:
            self.get_operator(binary)

    def get_literals(self, binary):
        code = binary[6:]
        pos = 0
        val = []
        while True:
            val.append(code[pos + 1:pos + 5])
            if code[pos] == '0':
                break
            pos += 5
        self.value = int("".join(val), 2)
        self.lastpos = pos + 5 + 6  # dlzka posledneho batchu a header

    def get_operator(self, binary):
        code = binary[6:]
        own_packets = []
        if code[0] == '0':
            length = int(code[1:16], 2)
            data = code[16:]
            cumsum = 0
            while True:
                pkt = Packet(self.transmission, data)
                self.transmission.packets.append(pkt)
                own_packets.append(pkt)
                pkt.decypher(data)
                cumsum += pkt.lastpos
                if cumsum >= length:
                    break
                data = data[pkt.lastpos:]
            self.lastpos = cumsum + 16 + 6  # dlzka id a header

        elif code[0] == '1':
            pocet = int(code[1:12], 2)
            data = code[12:]
            cumsum = 0
            for _ in range(pocet):
                pkt = Packet(self.transmission, data)
                own_packets.append(pkt)
                self.transmission.packets.append(pkt)
                pkt.decypher(data)
                cumsum += pkt.lastpos
                data = data[pkt.lastpos:]
            self.lastpos = cumsum + 12 + 6  # dlzka id a header

        if self.type == 0:
            self.value = sum(x.value for x in own_packets)
        elif self.type == 1:
            self.value = prod(x.value for x in own_packets)
        elif self.type == 2:
            self.value = min(own_packets, key=lambda x: x.value).value
        elif self.type == 3:
            self.value = max(own_packets, key=lambda x: x.value).value
        elif self.type == 5:
            self.value = 1 if own_packets[0].value > own_packets[1].value else 0
        elif self.type == 6:
            self.value = 1 if own_packets[0].value < own_packets[1].value else 0
        elif self.type == 7:
            self.value = 1 if own_packets[0].value == own_packets[1].value else 0


def solve_pt1():
    data = load_input()
    packetbin = ""
    for s in data:
        packetbin += bin(int(s, 16))[2:].zfill(4)
    transmission = Transmission(packetbin)
    transmission.packets[0].decypher(packetbin)
    res = 0
    for pkt in transmission.packets:
        res += pkt.version
    return res


def solve_pt2():
    data = load_input()
    packetbin = ""
    for s in data:
        packetbin += bin(int(s, 16))[2:].zfill(4)
    transmission = Transmission(packetbin)
    transmission.packets[0].decypher(packetbin)
    return transmission.packets[0].value


start = timeit.default_timer()
result1 = solve_pt1()
end = timeit.default_timer()
print(result1)
print(f"Total time pt1: {(end - start):.3f} sec")

start = timeit.default_timer()
result2 = solve_pt2()
end = timeit.default_timer()
print(result2)
print(f"Total time pt2: {(end - start):.3f} sec")
