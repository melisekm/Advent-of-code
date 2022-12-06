data = open("in.txt").read().strip()
print([next(i for i in range(length, len(data)) if len(set(data[i - length:i])) == length) for length in (4, 14)])