from functools import cache
import math
from aocd import lines, submit

heightmap = [[int(h) for h in line] for line in lines]


def neighbours(x, y):
    res = []
    for i in (-1, 1):
        nx = x + i
        ny = y + i
        if 0 <= nx < len(heightmap[0]):
            res.append((nx, y))
        if 0 <= ny < len(heightmap):
            res.append((x, ny))
    return res


def neighbour_heights(x, y):
    return [heightmap[ny][nx] for nx, ny in neighbours(x, y)]


# Part 1
risk = 0

for y, line in enumerate(heightmap):
    for x, height in enumerate(line):
        if all(height < neighbour for neighbour in neighbour_heights(x, y)):
            risk += height + 1

# submit(risk)


# Part 2
@cache
def basin_neighbours(x, y):
    return set().union(
        *(basin_neighbours(nx, ny) for nx, ny in neighbours(x, y)
          if (nh := heightmap[ny][nx]) > heightmap[y][x] and nh != 9)
    ) | {(x, y)}


basins = []
for y, line in enumerate(heightmap):
    for x, height in enumerate(line):
        if all(height < neighbour for neighbour in neighbour_heights(x, y)):
            basins.append(len(basin_neighbours(x, y)))

basins.sort(reverse=True)
submit(math.prod(basins[0:3]))
