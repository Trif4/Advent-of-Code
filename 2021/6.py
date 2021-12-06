from collections import Counter

from aocd import data, submit


def simulate(days=80):
    school = Counter(map(int, data.split(',')))

    for day in range(days):
        school = {timer-1: amount for timer, amount in school.items()}
        school[8] = school.get(-1, 0)
        school[6] = school.get(6, 0) + school.pop(-1, 0)

    return sum(school.values())


# Part 1
# submit(simulate())

# Part 2
submit(simulate(256))
