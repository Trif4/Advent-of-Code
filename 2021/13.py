from operator import itemgetter
from aocd import data, submit

coords = [tuple(map(int, line.split(','))) for line in data.split('\n\n')[0].splitlines()]
folds = [(axis, int(n)) for line in data.split('\n\n')[1].splitlines() for axis, n in [line.split()[2].split('=')]]


def fold(paper, axis, n):
    folded_paper = set()
    for x, y in paper:
        if axis == 'x' and x > n:
            folded_paper.add((2*n - x, y))
        elif axis == 'y' and y > n:
            folded_paper.add((x, 2*n - y))
        else:
            folded_paper.add((x, y))

    return folded_paper


# Part 1
paper = fold(coords, folds[0][0], folds[0][1])
# submit(len(paper))

# Part 2
for axis, n in folds[1:]:
    paper = fold(paper, axis, n)

maxx = max(paper, key=itemgetter(0))[0]
maxy = max(paper, key=itemgetter(1))[1]

code = ''
for y in range(maxy + 1):
    for x in range(maxx + 1):
        if (x, y) in paper:
            code += '#'
        else:
            code += ' '
    code += '\n'

print(code)
