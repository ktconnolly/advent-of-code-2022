def get_map():
    m = {}
    start, end = None, None
    with open("inputs/day_12.txt") as f:
        for r, row in enumerate(f):
            for c, col in enumerate(row):
                node = r, c
                if col == "S":
                    start = node
                    m[node] = "a"
                elif col == "E":
                    end = node
                    m[node] = "z"
                else:
                    m[node] = col
    return start, end, m


def get_neighbours(node):
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        yield node[0] + dx, node[1] + dy


def shortest_path(mp, start, destinations, move_fn):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node in visited:
            continue

        curr = mp.get(node)
        if node in destinations:
            return len(path) - 1

        visited.add(node)
        for neighbour in get_neighbours(node):
            n = mp.get(neighbour)
            if n is None:
                continue

            if move_fn(curr, n):
                new_path = path.copy()
                new_path.append(neighbour)
                queue.append(new_path)


def part_one():
    start, end, height_map = get_map()
    return shortest_path(height_map, start, [end],
                         lambda curr, n: ord(n) - ord(curr) <= 1)


def part_two():
    _, start, height_map = get_map()
    end = [k for k, v in height_map.items() if v == "a"]
    return shortest_path(height_map, start, end,
                         lambda curr, n: ord(curr) - ord(n) <= 1)


assert part_one() == 490
assert part_two() == 488
