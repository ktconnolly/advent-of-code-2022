class CPU:
    def __init__(self, instructions):
        self.instructions = instructions
        self.x = 1
        self.cycle_count = 1
        self.crt_count = 0
        self.strength = 0
        self.screen = [['.' for _ in range(40)] for _ in range(6)]

    def run(self):
        for instr in self.instructions:
            if len(instr) == 1:
                self.cycle()
            else:
                self.cycle(2)
                self.x += int(instr[1])

    def calculate_strength(self):
        if self.cycle_count in range(20, 221, 40):
            self.strength += self.x * self.cycle_count

    def draw(self):
        row = (self.crt_count % 240) // 40
        col = self.crt_count % 40
        self.screen[row][col] = "#" if abs(self.x - col) <= 1 else "."

    def cycle(self, n=1):
        for _ in range(n):
            self.calculate_strength()
            self.draw()
            self.cycle_count += 1
            self.crt_count += 1


def part_one():
    with open("inputs/day_10.txt") as f:
        cpu = CPU([l.split() for l in f])

    cpu.run()
    return cpu.strength


def part_two():
    with open("inputs/day_10.txt") as f:
        cpu = CPU([l.split() for l in f])

    cpu.run()

    crt = "\n"
    for row in cpu.screen:
        crt += "".join(row) + "\n"
    return crt


assert part_one() == 14760
assert part_two() == """
####.####..##..####.###..#..#.###..####.
#....#....#..#.#....#..#.#..#.#..#.#....
###..###..#....###..#..#.#..#.#..#.###..
#....#....#.##.#....###..#..#.###..#....
#....#....#..#.#....#.#..#..#.#.#..#....
####.#.....###.####.#..#..##..#..#.####.
"""
