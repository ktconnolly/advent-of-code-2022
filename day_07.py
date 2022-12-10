from collections import namedtuple

File = namedtuple("File", "size name")

AVAILABLE_SPACE = 70000000
REQUIRED_SPACE = 30000000


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

    def add_dir(self, directory):
        self.dirs.append(directory)

    def get_dir(self, name):
        for d in self.dirs:
            if d.name == name:
                return d
        return None

    def add_file(self, file):
        self.files.append(file)

    def get_size(self):
        return sum(d.get_size() for d in self.dirs) + sum(f.size for f in self.files)


def get_root():
    with open("inputs/day_07.txt") as f:
        lines = [l.strip() for l in f.readlines()]
        root = Directory(name="/")
        curr_dir = root
        for l in lines[2:]:
            l = l.split()

            if l[0] == "dir":
                child = Directory(name=l[1], parent=curr_dir)
                curr_dir.add_dir(child)
            elif str.isdigit(l[0]):
                file = File(size=int(l[0]), name=l[1])
                curr_dir.add_file(file)
            elif l[0] == "$" and l[1] == "cd":
                if l[2] == "..":
                    curr_dir = curr_dir.parent
                else:
                    curr_dir = curr_dir.get_dir(l[2])

    return root


def get_sizes(directory, sizes=None):
    if sizes is None:
        sizes = []

    sizes.append(directory.get_size())

    for child in directory.dirs:
        sizes += get_sizes(child)

    return sizes


def part_one():
    root = get_root()
    return sum(s if s <= 100000 else 0 for s in get_sizes(root))


def part_two():
    root = get_root()
    required = REQUIRED_SPACE - (AVAILABLE_SPACE - root.get_size())

    best = None
    for size in get_sizes(root):
        if size < required:
            continue

        if best is None or size - required < best - required:
            best = size

    return best


assert part_one() == 919137
assert part_two() == 2877389
