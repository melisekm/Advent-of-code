from collections import Counter
from functools import cmp_to_key

from utils import aoc_part


def load_input(file_name="in.txt"):
    res = []
    with open(file_name, encoding='UTF-8') as f:
        for line in f:
            line = line.strip().split()
            res.append((line[0], int(line[1])))
    return res


power_mapping = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    **{str(x): x for x in range(2, 10)},
}


def evaluate_hand(hand, p2=False):
    if p2 and 'J' in hand:
        best = 0
        be = None
        for p in power_mapping.keys():
            if p == 'J':
                continue
            h = hand.replace('J', p, 1)
            evaluated = evaluate_hand(h, p2)
            if evaluated[1] > best:
                best = evaluated[1]
                be = evaluated
        return be

    if len(set(hand)) == 1:
        return 'five of a kind', 7
    counts = Counter(hand)
    if 4 in counts.values():
        return 'four of a kind', 6
    if sorted(counts.values()) == [2, 3]:
        return 'full house', 5
    if 3 in counts.values():
        return 'three of a kind', 4
    if sorted(counts.values()) == [1, 2, 2]:
        return 'two pair', 3
    if 2 in counts.values():
        return 'pair', 2
    return 'high card', 1


def comparator(hand1, hand2):
    if hand1[0][1] != hand2[0][1]:
        return hand1[0][1] - hand2[0][1]

    for x, y in zip(hand1[1][0], hand2[1][0]):
        if x != y:
            return power_mapping[x] - power_mapping[y]
    return 0


def solve(data, pt2):
    return sum(
        idx * hand[1][1]
        for idx, hand in enumerate(
            sorted(((evaluate_hand(hand[0], p2=pt2), hand) for hand in data), key=cmp_to_key(comparator)), start=1
        )
    )


@aoc_part(1)
def solve_pt1():
    power_mapping['J'] = 11
    data = load_input()
    return solve(data, False)


@aoc_part(2)
def solve_pt2():
    power_mapping['J'] = 0
    data = load_input()
    return solve(data, True)


solve_pt1()
solve_pt2()
