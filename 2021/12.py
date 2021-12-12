from collections import defaultdict
from aocd import lines, submit

paths = defaultdict(list)

for path in lines:
    c1, c2 = path.split('-')
    paths[c1].append(c2)
    paths[c2].append(c1)


def pathfind(path, can_visit_twice=False):
    current = path[-1]
    if current == 'end':
        yield path
        return
    for c in paths[current]:
        if c != 'start':
            already_visited = c.lower() in path
            if not already_visited or can_visit_twice:
                yield from pathfind(path + [c], can_visit_twice and not already_visited)


# Part 1
# submit(len(list(pathfind(['start']))))

# Part 2
submit(len(list(pathfind(['start'], True))))
