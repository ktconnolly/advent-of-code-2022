def solve(n):
    with open("inputs/day_6.txt") as f:
        seq = f.read()
        for i in range(len(seq) - n + 1):
            if len(set(seq[i: i + n])) == n:
                return i + n


def part_one():
    return solve(4)


def part_two():
    return solve(14)


assert part_one() == 1361
assert part_two() == 3263
