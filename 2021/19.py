from functools import cache
from itertools import chain, permutations, pairwise, combinations
import operator
from aocd import data, submit

scanner_beacons = [[tuple(map(int, b.split(','))) for b in s.splitlines()[1:]] for s in data.split('\n\n')]


def subtract(a, b):
    return tuple(map(operator.sub, a, b))


def add(a, b):
    return tuple(map(operator.add, a, b))


def rotate_around_x(x, y, z):
    return [
        (x, y, z),
        (x, z, -y),
        (x, -y, -z),
        (x, -z, y),
    ]


def rotate_around_y(x, y, z):
    return [
        (x, y, z),
        (-z, y, x),
        (-x, y, -z),
        (z, y, -x)
    ]


def rotate_around_z(x, y, z):
    return [
        (x, y, z),
        (-y, x, z),
        (-x, -y, z),
        (y, -x, z)
    ]


def transformations(x, y, z):
    # I thought this was clever then realised it doesn't work but then it actually works anyway and I don't know why
    return list(chain.from_iterable(
        [rotate_around_x(*rotation) for rotation in rotate_around_y(x, y, z) + rotate_around_z(x, y, z)[1::2]]
    ))


@cache
def relative_beacons(root, beacons):
    return {subtract(root, other) for other in beacons}


scanner_transformed_beacons = [list(zip(*[transformations(*b) for b in s])) for s in scanner_beacons]
scanner_to_scanner_transforms = {}


def match_scanners(s1, s2):
    for b1 in scanner_beacons[s1]:
        b1_relatives = relative_beacons(b1, tuple(scanner_beacons[s1]))
        for b2i, b2 in enumerate(scanner_beacons[s2]):
            for t in range(24):
                s2_transformed = scanner_transformed_beacons[s2][t]
                b2_relatives = relative_beacons(s2_transformed[b2i], tuple(s2_transformed))
                if len(b1_relatives & b2_relatives) >= 12:
                    return subtract(b1, s2_transformed[b2i]), t


for s1, s2 in permutations(range(len(scanner_beacons)), 2):
    print(f'Comparing scanner {s1} and {s2}')
    if m := match_scanners(s1, s2):
        scanner_to_scanner_transforms[s1, s2] = m


def find_paths(path):
    if path[-1] in path[:-1]:
        return {tuple(path[:-1])}
    return {p for pair in scanner_to_scanner_transforms if pair[0] == path[-1] for p in find_paths(path + [pair[1]])}


true_beacons = set(scanner_beacons[0])
true_scanners = [(0, 0, 0)]*len(scanner_beacons)

for path in find_paths([0]):
    if true_scanners[path[-1]] != (0, 0, 0):
        continue
    beacons = set(scanner_beacons[path[-1]])
    scanner = scanner_to_scanner_transforms[path[-2], path[-1]][0]
    for pair, next_pair in list(pairwise(reversed(list(pairwise(path))))):
        beacons = {transformations(*b)[scanner_to_scanner_transforms[pair][1]] for b in beacons}
        scanner = add(scanner_to_scanner_transforms[next_pair][0],
                      transformations(*scanner)[scanner_to_scanner_transforms[next_pair][1]])
    beacons = {add(transformations(*b)[scanner_to_scanner_transforms[path[0], path[1]][1]], scanner) for b in
               beacons}
    true_beacons |= beacons
    true_scanners[path[-1]] = scanner


# Part 1
# submit(len(true_beacons))

# Part 2
longest_distance = 0
for a, b in combinations(true_scanners, 2):
    distance = sum(tuple(map(operator.abs, subtract(a, b))))
    longest_distance = max(longest_distance, distance)
submit(longest_distance)
