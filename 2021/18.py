from ast import literal_eval
import functools
from itertools import permutations
import math
import re
from aocd import lines, submit


def add(left, right):
    return reduce(f'[{left},{right}]')


def reduce(number: str):
    res = number

    while True:
        depth = 0
        explode_index = 0
        for i, c in enumerate(res):
            if c == '[':
                depth += 1
            if c == ']':
                depth -= 1
            if depth == 5:
                explode_index = i
                break

        if explode_index:
            pair_end = explode_index + res[explode_index:].find(']')
            a, b = res[explode_index+1:pair_end].split(',')
            if matches := list(re.finditer(r'\d+', res[pair_end:])):
                m = matches[0]
                res = res[:pair_end+m.start()] + str(int(m.group()) + int(b)) + res[pair_end+m.end():]
            res = res[:explode_index] + '0' + res[pair_end+1:]
            if matches := list(re.finditer(r'\d+', res[0:explode_index])):
                m = matches[-1]
                res = res[:m.start()] + str(int(m.group()) + int(a)) + res[m.end():]
        elif m := re.search(r'\d{2,}', res):
            a = int(m.group()) // 2
            b = int(math.ceil(int(m.group()) / 2))
            pair = f'[{a},{b}]'
            res = res[:m.start()] + pair + res[m.end():]
        else:
            break

    return res


def magnitude(lst):
    if isinstance(lst, int):
        return lst
    else:
        return 3*magnitude(lst[0]) + 2*magnitude(lst[1])


# Part 1
# submit(magnitude(literal_eval(functools.reduce(add, lines))))

# Part 2
largest_magnitude = 0
for a, b in permutations(lines, 2):
    largest_magnitude = max(largest_magnitude, magnitude(literal_eval(add(a, b))))
submit(largest_magnitude)
