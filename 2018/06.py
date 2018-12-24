from collections import Counter

from aocd import data

coordinates = set(tuple(int(n) for n in loc.split(', ')) for loc in data.splitlines())

grid_size = max(i for coord in coordinates for i in coord) + 1

grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]
infinity_coordinates = set()

for i in range(grid_size):
    for j in range(grid_size):
        closest_coordinate = None
        min_distance = grid_size*10
        tie = False

        for (x, y) in coordinates:
            distance = abs(x - i) + abs(y - j)

            if distance < min_distance:
                closest_coordinate = (x, y)
                min_distance = distance
                tie = False

            elif distance == min_distance:
                tie = True

        if not tie:
            grid[i][j] = closest_coordinate

            if i in [0, grid_size - 1] or j in [0, grid_size - 1]:
                infinity_coordinates.add(closest_coordinate)

greatest_area = Counter(l for r in grid for l in r if l in coordinates - infinity_coordinates).most_common(1)[0][1]

print(greatest_area)


# B

cool_club = []

for i in range(grid_size):
    for j in range(grid_size):
        distance = 0

        for (x, y) in coordinates:
            distance += abs(x - i) + abs(y - j)

        if distance < 10000:
            cool_club.append((i, j))

print(len(cool_club))
