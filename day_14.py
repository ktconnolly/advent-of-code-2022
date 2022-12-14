START = (500, 0)


def get_points_between(x1, y1, x2, y2):
    points = set()

    if y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1

        for x in range(x1, x2 + 1):
            points.add((x, y1))

    elif x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1

        for y in range(y1, y2 + 1):
            points.add((x1, y))

    return points


def get_lines():
    lines = set()
    with open("inputs/day_14.txt") as f:
        for l in f:
            points = l.split(" -> ")
            for i in range(len(points) - 1):
                p1 = map(int, points[i].split(","))
                p2 = map(int, points[i + 1].split(","))
                lines = lines | get_points_between(*p1, *p2)
    return lines


def get_moves(x, y):
    return [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]


def simulate(bottomless):
    lines = get_lines()
    bottom = max(y for (_, y) in lines) + (0 if bottomless else 2)
    stopped_sand = set()
    sand = START
    while True:
        m1, m2, m3 = get_moves(*sand)
        if not bottomless and m1[1] == bottom:
            stopped_sand.add(sand)
            sand = START
        elif m1 not in lines and m1 not in stopped_sand:
            sand = m1
        elif m2 not in lines and m2 not in stopped_sand:
            sand = m2
        elif m3 not in lines and m3 not in stopped_sand:
            sand = m3
        else:
            stopped_sand.add(sand)
            if sand == START:
                break
            sand = START

        if sand[1] == bottom:
            break

    return len(stopped_sand)


def part_one():
    return simulate(bottomless=True)


def part_two():
    return simulate(bottomless=False)


assert part_one() == 817
assert part_two() == 23416
