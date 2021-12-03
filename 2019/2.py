from aocd import data, submit

target = 19690720
noun = -1
verb = 99
output = 0

while output != target:
    verb = verb + 1
    if verb == 100:
        verb = 0
        noun = noun + 1

    ops = list(map(int, data.split(',')))
    ops[1] = noun
    ops[2] = verb
    step = 0

    while ops[step] != 99:
        val1 = ops[ops[step + 1]]
        val2 = ops[ops[step + 2]]
        dest = ops[step + 3]

        if ops[step] == 1:
            res = val1 + val2
        elif ops[step] == 2:
            res = val1 * val2
        else:
            raise Exception

        ops[dest] = res
        step += 4

    output = ops[0]

# submit(100 * noun + verb)

