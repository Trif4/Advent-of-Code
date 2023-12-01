import re
from itertools import product
from aocd import lines, submit

core = {}

for step in lines:
    print(step)
    state = step.split()[0]
    x1, x2, y1, y2, z1, z2 = map(int, re.findall(r'(-?\d+)', step))
    if ((-50 <= x1 <= 50 or -50 <= x2 <= 50) and
            (-50 <= y1 <= 50 or -50 <= y2 <= 50) and
            (-50 <= z1 <= 50 or -50 <= z2 <= 50)):
        for cube in product(range(x1, x2+1), range(y1, y2+1), range(z1, z2+1)):
            if state == 'on':
                core[cube] = 1
            else:
                core.pop(cube, None)

submit(len(core))
