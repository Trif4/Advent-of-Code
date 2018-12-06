import re
import string

from aocd import data

polymer = data


# A

pairs = [''.join(pair) for pair in zip(string.ascii_lowercase, string.ascii_uppercase)]


def reduce_polymer(p):
    prev_length = -1

    while prev_length != len(p):
        prev_length = len(p)

        for pair in pairs:
            p = p.replace(pair, '')
            p = p.replace(pair[::-1], '')

    return p


units = len(reduce_polymer(polymer))

print(units)


# B

min_units = min(len(reduce_polymer(re.sub(unit, '', polymer, flags=re.I))) for unit in string.ascii_lowercase)

print(min_units)
