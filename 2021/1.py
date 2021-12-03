from aocd import numbers, submit

# Part 1
increases = 0
last = None
for n in numbers:
    if last is not None and n > last:
        increases += 1
    last = n

# submit(increases)

# Part 2
increases = 0
window = (None, None, None)
for n in numbers:
    new = (window[1], window[2], n)
    if None not in window and sum(new) > sum(window):
        increases += 1
    window = new

submit(increases)
