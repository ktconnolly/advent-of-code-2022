import ast
import functools


def compare_packets(l1, l2):
    for left, right in zip(l1, l2):
        if type(left) == list and type(right) == list:
            outcome = compare_packets(left, right)
            if outcome != 0:
                return outcome
        elif type(left) == list:
            outcome = compare_packets(left, [right])
            if outcome != 0:
                return outcome
        elif type(right) == list:
            outcome = compare_packets([left], right)
            if outcome != 0:
                return outcome
        else:
            if right < left:
                return -1
            if left < right:
                return 1

    if len(l1) > len(l2):
        return -1
    if len(l2) > len(l1):
        return 1
    return 0


def get_packets():
    with open("inputs/day_13.txt") as f:
        for i, pair in enumerate(f.read().split("\n\n"), 1):
            p1, p2 = pair.split("\n")
            yield ast.literal_eval(p1), ast.literal_eval(p2)


def part_one():
    return sum(i if compare_packets(*p) == 1 else 0 for i, p in
               enumerate(get_packets(), 1))


def part_two():
    d1, d2 = [[6]], [[2]]
    packets = [d1, d2]
    for p in get_packets():
        packets.extend(p)

    packets.sort(key=functools.cmp_to_key(compare_packets), reverse=True)
    return (packets.index(d1) + 1) * (packets.index(d2) + 1)


assert part_one() == 5843
assert part_two() == 26289
