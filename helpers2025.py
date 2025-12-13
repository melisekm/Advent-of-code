import re


def get_all_integers_from_string(s: str) -> list[int]:
    return [int(x) for x in re.findall(r'\d+', s)]

def get_lines_as_strings(file_name: str) -> list[str]:
    res = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            res.append(line)
    return res