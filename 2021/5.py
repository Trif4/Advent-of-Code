from collections import defaultdict
from itertools import zip_longest
from aocd import lines, submit


def overlap_count(diagonals=False):
    ocean = defaultdict(int)

    for line in lines:
        p1, p2 = line.split(' -> ')
        x1, y1 = tuple(map(int, p1.split(',')))
        x2, y2 = tuple(map(int, p2.split(',')))
        if x1 == x2 or y1 == y2 or diagonals:
            if x1 <= x2:
                xrng = range(x1, x2+1)
            else:
                xrng = range(x1, x2-1, -1)
            if y1 <= y2:
                yrng = range(y1, y2+1)
            else:
                yrng = range(y1, y2-1, -1)

            if len(xrng) == 1:
                fillvalue = xrng[0]
            elif len(yrng) == 1:
                fillvalue = yrng[0]
            else:
                fillvalue = None

            for x, y in zip_longest(xrng, yrng, fillvalue=fillvalue):
                ocean[(x, y)] += 1

    return sum(1 for p in ocean.values() if p > 1)


# Part 1
# submit(overlap_count())

# Part 2
submit(overlap_count(True))
