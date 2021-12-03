from aocd import lines, submit

# Part 1
pos = 0
depth = 0

for line in lines:
    t = line.split(' ')
    match (t[0], int(t[1])):
        case ['forward', x]:
            pos += x
        case ['down', x]:
            depth += x
        case ['up', x]:
            depth -= x

# submit(pos * depth)

# Part 2
pos = 0
depth = 0
aim = 0

for line in lines:
    t = line.split(' ')
    match (t[0], int(t[1])):
        case ['forward', x]:
            pos += x
            depth += aim * x
        case ['down', x]:
            aim += x
        case ['up', x]:
            aim -= x

submit(pos * depth)
