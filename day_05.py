from utils import chunks
from collections import namedtuple

Procedure = namedtuple("Procedure", "count stack_from stack_to")


def get_input():
    def get_starting_stacks(stacks_str):
        stacks_str = stacks_str.split("\n")
        total_stacks = int(stacks_str.pop().split()[-1])
        stacks = [[] for _ in range(total_stacks)]
        for row in stacks_str[::-1]:
            for i, c in enumerate(chunks(row, 4)):
                c = c.strip()
                if c:
                    stacks[i].append(c[1])

        return stacks

    def get_procedures(procedure_str):
        procedures = []
        for procedure in procedure_str.split("\n"):
            p = procedure.split()
            count, stack_from, stack_to = int(p[1]), int(p[3]), int(p[5])
            procedures.append(Procedure(count, stack_from - 1, stack_to - 1))
        return procedures

    with open("inputs/day_05.txt") as f:
        starting, procedures = f.read().split("\n\n")
        return get_starting_stacks(starting), get_procedures(procedures)


def part_one():
    stacks, procedures = get_input()
    for p in procedures:
        for _ in range(p.count):
            stacks[p.stack_to] += stacks[p.stack_from].pop()

    return "".join(s[-1] for s in stacks)


def part_two():
    stacks, procedures = get_input()
    for p in procedures:
        frm_stack = stacks[p.stack_from]
        stacks[p.stack_to] += frm_stack[-p.count:]
        del frm_stack[-p.count:]

    return "".join(s[-1] for s in stacks)


assert part_one() == "JCMHLVGMG"
assert part_two() == "LVMRWSSPZ"
