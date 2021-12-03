from collections import defaultdict

from aocd import data, submit

points = defaultdict(lambda: (0, 0))

(l1, l2) = data.splitlines()


def setval(pos, line=1):
    global step
    step += 1
    (x, y) = points[pos]
    if line == 1:
        if not x:
            points[pos] = (step, y)
    else:
        if not y:
            points[pos] = (x, step)


current = (0, 0)
step = 0
for i in l1.split(','):
    di = i[0]
    n = int(i[1:])
    (x, y) = current
    if di == 'R':
        x += n
        for a in range(current[0] + 1, x + 1):
            setval((a, y))
    if di == 'L':
        x -= n
        for a in range(x, current[0]):
            setval((a, y))
    if di == 'U':
        y += n
        for a in range(current[1] + 1, y + 1):
            setval((x, a))
    if di == 'D':
        y -= n
        for a in range(y, current[1]):
            setval((x, a))

    current = (x, y)

current = (0, 0)
step = 0
for i in l2.split(','):
    di = i[0]
    n = int(i[1:])
    (x, y) = current
    if di == 'R':
        x += n
        for a in range(current[0] + 1, x + 1):
            setval((a, y), line=2)
    if di == 'L':
        x -= n
        for a in range(x, current[0]):
            setval((a, y), line=2)
    if di == 'U':
        y += n
        for a in range(current[1] + 1, y + 1):
            setval((x, a), line=2)
    if di == 'D':
        y -= n
        for a in range(y, current[1]):
            setval((x, a), line=2)

    current = (x, y)

lowest = 9999999
for point, (x, y) in points.items():
    if x and y:
        lowest = min(lowest, x + y)

print(lowest)
submit(lowest)
