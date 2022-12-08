def get_trees():
    with open("inputs/day_8.txt") as f:
        return [[int(col) for col in l.strip()] for l in f]


def part_one():
    trees = get_trees()
    h, w = len(trees), len(trees[0])
    visible = 0
    for row in range(h):
        for col in range(w):
            height = trees[row][col]
            visible += int(
                (all(trees[row][c] < height for c in range(col))
                 or all(trees[row][c] < height for c in range(col + 1, w))
                 or all(trees[r][col] < height for r in range(row))
                 or all(trees[r][col] < height for r in range(row + 1, h))))

    return visible


def part_two():
    trees = get_trees()
    h, w = len(trees), len(trees[0])
    best = -1
    for row in range(h):
        for col in range(w):
            height = trees[row][col]

            up = 0
            for r in range(row - 1, -1, -1):
                up += 1
                if trees[r][col] >= height:
                    break

            down = 0
            for r in range(row + 1, h):
                down += 1
                if trees[r][col] >= height:
                    break

            left = 0
            for c in range(col - 1, -1, -1):
                left += 1
                if trees[row][c] >= height:
                    break

            right = 0
            for c in range(col + 1, w):
                right += 1
                if trees[row][c] >= height:
                    break

            best = max(best, up * down * left * right)

    return best


assert part_one() == 1832
assert part_two() == 157320
