from aocd import lines, submit

# Part 1
length = len(lines[0])
epsilon = ''
for i in range(length):
    res = 0
    for n in lines:
        if n[i] == '1':
            res += 1
        else:
            res -= 1
    if res > 0:
        epsilon += '1'
    else:
        epsilon += '0'

gamma = ''.join('1' if x == '0' else '0' for x in epsilon)

# submit(int(epsilon, 2) * int(gamma, 2))

# Part 2
def get_rating(is_oxygen):
    numbers = lines
    keep = None
    for i in range(length):
        res = 0
        for n in numbers:
            if n[i] == '1':
                res += 1
            else:
                res -= 1
        if (is_oxygen and res >= 0) or (not is_oxygen and res < 0):
            numbers = [n for n in numbers if n[i] == '1']
        else:
            numbers = [n for n in numbers if n[i] == '0']
        if len(numbers) == 1:
            return int(numbers[0], 2)


oxygen = get_rating(True)
co2 = get_rating(False)

submit(oxygen * co2)
