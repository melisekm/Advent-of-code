import timeit
import copy


def solve_pt1(vstup):
    def rozhodni(cislo, ranges):
        for _range in ranges:
            r1 = _range[0]
            r2 = _range[1]
            if r1[0] <= cislo <= r1[1] or r2[0] <= cislo <= r2[1]:
                return True

    def posud(ranges, ticket, result):
        tmp = set()
        for cislo in ticket:
            if rozhodni(cislo, ranges):
                tmp.add(cislo)
        flag = True
        for val in ticket:
            if val not in tmp:
                result.append(val)
                flag = False
        return flag

    with open(vstup, "r") as file:
        ranges = []
        names = []
        while (line := file.readline()) != "\n":
            line = line.strip().split(":")
            names.append(line[0])
            _ranges = line[1].strip().split()
            range1 = list(map(int, _ranges[0].split("-")))
            range2 = list(map(int, _ranges[2].split("-")))
            ranges.append([range1, range2])
        file.readline()
        my_ticket = list(map(int, file.readline().strip().split(",")))
        while "nearby" not in file.readline():
            pass
        result = []
        valid_tickets = []
        while ticket := file.readline():
            ticket = list(map(int, ticket.strip().split(",")))
            if posud(ranges, ticket, result):
                valid_tickets.append(ticket)
        return sum(result), valid_tickets, my_ticket, names, ranges


def solve_pt2(valid_tickets, my_ticket, names, ranges):
    def pories_column(valid_tickets, column_id, ranges):
        tmp_ranges = copy.deepcopy(ranges)
        valid_columns = list(range(len(ranges)))
        for ticket_fields in valid_tickets:
            cislo = ticket_fields[column_id]
            for idx, _range in enumerate(tmp_ranges):
                r1 = _range[0]
                r2 = _range[1]
                if not (r1[0] <= cislo <= r1[1] or r2[0] <= cislo <= r2[1]):
                    valid_columns.pop(idx)
                    tmp_ranges.remove(_range)
                if len(valid_columns) == 1:
                    return tuple(tuple(x) for x in ranges.pop(valid_columns[0]))
        return -1

    range2field = {tuple(tuple(y) for y in x): name for x, name in zip(ranges, names)}
    field2column = {}
    solved_columns = [False] * len(valid_tickets[0])
    ok = column_id = 0
    while ok != len(valid_tickets[0]):
        if solved_columns[column_id] is False:
            found_range = pories_column(valid_tickets, column_id, ranges)
            if found_range != -1:
                field = range2field[found_range]
                field2column[field] = column_id
                solved_columns[column_id] = True
                ok += 1
        column_id += 1
        column_id %= len(valid_tickets[0])

    res = 1
    for key, value in field2column.items():
        if "departure" in key:
            res *= my_ticket[value]
    return res


vstup = "vstup.txt"

start = timeit.default_timer()
result1, valid_tickets, my_ticket, names, ranges = solve_pt1(vstup)
print(result1)
print(f"Cas vykonavania pt1:{timeit.default_timer() - start} sec")


start = timeit.default_timer()
result2 = solve_pt2(valid_tickets, my_ticket, names, ranges)
print(result2)
print(f"Cas vykonavania pt2:{timeit.default_timer() - start} sec")
