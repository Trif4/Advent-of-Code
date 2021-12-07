from statistics import median
from aocd import data, submit

positions = list(map(int, data.split(',')))

# Part 1
med = median(positions)
fuel = int(sum(abs(p - med) for p in positions))
# submit(fuel)

# Part 2
fuel = 99999999999
for i in range(min(positions), max(positions)+1):
    fuel = min(fuel, sum((n := abs(p - i)) * (n+1) / 2 for p in positions))
submit(int(fuel))
