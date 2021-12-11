from aocd import lines, submit

grid = [[int(o) for o in line] for line in lines]
flashes = 0


def get_neighbours(x, y):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if (i, j) == (0, 0):
                continue
            nx = x + i
            ny = y + j
            if 0 <= nx < 10 and 0 <= ny < 10:
                yield nx, ny


def flash(x, y):
    global flashes
    flashes += 1
    for i, j in get_neighbours(x, y):
        grid[j][i] += 1
        if grid[j][i] == 10:
            flash(i, j)


def step():
    for y in range(10):
        for x in range(10):
            grid[y][x] += 1
            if grid[y][x] == 10:
                flash(x, y)
    for y in range(10):
        for x in range(10):
            if grid[y][x] > 9:
                grid[y][x] = 0


# Part 1
for _ in range(100):
    step()

# submit(flashes)

# Part 2
grid = [[int(o) for o in line] for line in lines]
steps = 0
while any(o for line in grid for o in line if o > 0):
    step()
    steps += 1

submit(steps)
