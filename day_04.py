import re

pattern = re.compile("(\d+)-(\d+),(\d+)-(\d+)")


def get_ranges():
    with open("inputs/day_04.txt") as f:
        for l in f:
            m = pattern.match(l)
            r1 = range(int(m[1]), int(m[2]) + 1)
            r2 = range(int(m[3]), int(m[4]) + 1)
            yield r1, r2


def part_one():
    def in_range(r1, r2):
        return (r1.start >= r2.start and r1.stop <= r2.stop) or (
                r2.start >= r1.start and r2.stop <= r1.stop)

    return sum(in_range(r2, r1) for r1, r2 in get_ranges())


def part_two():
    return sum(bool(set(r1).intersection(r2)) for r1, r2 in get_ranges())


assert part_one() == 483
assert part_two() == 874
