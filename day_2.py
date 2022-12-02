def get_input():
    with open("inputs/day_2.txt") as f:
        for l in f:
            yield l.split()


def part_one():
    score = 0
    for op_move, my_move in get_input():
        op_move, my_move = ord(op_move) - ord("A"), ord(my_move) - ord("X")
        score += ((my_move - op_move + 1) % 3) * 3 + (my_move + 1)
    return score


def part_two():
    score = 0
    for op_move, outcome in get_input():
        op_move, outcome = ord(op_move) - ord("A"), ord(outcome) - ord("X")
        my_move = (op_move + outcome - 1) % 3
        score += ((my_move - op_move + 1) % 3) * 3 + (my_move + 1)
    return score


assert part_one() == 14069
assert part_two() == 12411
