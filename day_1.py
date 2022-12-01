def part_one():
    with open("inputs/day_1.txt") as f:
        return max(sum(map(int, elf.split())) for elf in f.read().split("\n\n"))


def part_two():
    with open("inputs/day_1.txt") as f:
        return sum(sorted(sum(map(int, elf.split())) for elf in f.read().split("\n\n"))[-3:])


assert part_one() == 73211
assert part_two() == 213958
