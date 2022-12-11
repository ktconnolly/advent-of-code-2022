import math
import operator
import re

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}


class Test:
    def __init__(self, value, true, false):
        self.value = value
        self.true = true
        self.false = false

    def run(self, val):
        return self.true if val % self.value == 0 else self.false


class Monkey:
    def __init__(self):
        self.items = []
        self.op_value = None
        self.op = None
        self.test = None
        self.inspected = 0

    def add_item(self, item):
        self.items.append(item)

    def inspect(self, item):
        self.inspected += 1
        if self.op_value == "old":
            return OPS[self.op](item, item)
        return OPS[self.op](item, int(self.op_value))

    def get_next_monkey(self, level):
        return self.test.run(level)


def get_monkeys():
    monkeys = []
    with open("inputs/day_11.txt") as f:
        for m in f.read().split("\n\n"):
            _, items, op, *test = m.split("\n")
            monkey = Monkey()
            monkey.items = list(map(int, re.findall(r"\d+", items)))
            monkey.op, monkey.op_value = re.findall(r"old (.) (.+)", op)[0]
            monkey.test = Test(*map(lambda x: int(x.split()[-1]), test))
            monkeys.append(monkey)

    return monkeys


def run(monkeys, rounds, n=None):
    for _ in range(rounds):
        for m in monkeys:
            for item in m.items:
                item = m.inspect(item)
                item = item % n if n is not None else item // 3
                outcome = m.get_next_monkey(item)
                monkeys[outcome].add_item(item)

            m.items = []

    return operator.mul(*sorted(m.inspected for m in monkeys)[-2:])


def part_one():
    monkeys = get_monkeys()
    return run(monkeys, 20)


def part_two():
    monkeys = get_monkeys()
    n = math.prod(m.test.value for m in get_monkeys())
    return run(monkeys, 10_000, n)


assert part_one() == 121450
assert part_two() == 28244037010
