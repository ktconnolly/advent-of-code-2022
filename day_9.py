from dataclasses import dataclass

LEFT = "L"
RIGHT = "R"
UP = "U"
DOWN = "D"

DIRECTIONS = {
    UP: (0, 1),
    DOWN: (0, -1),
    LEFT: (-1, 0),
    RIGHT: (1, 0)
}


def get_moves():
    with open("inputs/day_9.txt") as f:
        return [(l.split()[0], int(l.split()[1])) for l in f]


@dataclass
class Point:
    x: int
    y: int


def run(n_tails):
    tails = [Point(0, 0) for _ in range(n_tails)]
    head = Point(0, 0)
    visited = set()

    for direction, distance in get_moves():
        for _ in range(distance):
            dx, dy = DIRECTIONS[direction]
            head.x += dx
            head.y += dy

            for i, tail in enumerate(tails):
                in_front = head if i == 0 else tails[i - 1]

                if abs(tail.x - in_front.x) <= 1 and abs(tail.y - in_front.y) <= 1:
                    continue

                if tail.x != in_front.x and tail.y != in_front.y:
                    tail.x += 1 if in_front.x > tail.x else -1
                    tail.y += 1 if in_front.y > tail.y else -1
                else:
                    if tail.x > in_front.x:
                        dx, dy = DIRECTIONS[LEFT]
                    elif tail.x < in_front.x:
                        dx, dy = DIRECTIONS[RIGHT]
                    elif tail.y > in_front.y:
                        dx, dy = DIRECTIONS[DOWN]
                    elif tail.y < in_front.y:
                        dx, dy = DIRECTIONS[UP]

                    tail.x += dx
                    tail.y += dy

            visited.add((tails[-1].x, tails[-1].y))

    return len(visited)


def part_one():
    return run(1)


def part_two():
    return run(9)


assert part_one() == 5960
assert part_two() == 2327
