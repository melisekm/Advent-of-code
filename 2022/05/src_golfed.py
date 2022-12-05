def solve(pt):
    import re
    data = ['vcdrzgbw', 'gwfcbstv', 'cbsnw', 'qgmnjvcp', 'tslfdhb', 'jvtwmn', 'pflcstg', 'bdz', 'mnzw']
    for how_many, fromm, to in [map(int, re.findall(r'\d+', line)) for line in open('in.txt')]:
        data[fromm - 1], result = data[fromm - 1][:-how_many], data[fromm - 1][-how_many:]
        data[to - 1] += result[::-1] if pt == 1 else result
    print("".join(string[-1].upper() for string in data))

solve(1)
solve(2)