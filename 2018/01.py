from itertools import cycle

from aocd import data

changes = [int(x) for x in data.splitlines()]


# A

print(sum(changes))


# B

freq = 0
seen_freqs = set()
repeating_data = cycle(changes)

while freq not in seen_freqs:
    seen_freqs.add(freq)
    freq += next(repeating_data)

print(freq)
