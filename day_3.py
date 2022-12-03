from collections import defaultdict
import string


def part_one():
    score = 0
    with open("inputs/day_3.txt") as f:
        for bag in f:
            h1, h2 = bag[:len(bag) // 2], bag[len(bag) // 2:]
            common = set(h1).intersection(h2)
            score += string.ascii_letters.index(common.pop()) + 1
    return score


def part_two():
    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    score = 0
    with open("inputs/day_3.txt") as f:
        bags = list(chunks([l.strip() for l in f.readlines()], 3))
        for group in bags:
            common = set(group[0]).intersection(*group)
            score += string.ascii_letters.index(common.pop()) + 1
    return score


assert part_one() == 8039
assert part_two() == 2510
