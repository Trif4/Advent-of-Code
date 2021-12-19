from collections import Counter
from itertools import pairwise
from aocd import data, submit

template, rules_section = data.split('\n\n')
rules = {pair: letter for line in rules_section.splitlines() for pair, letter in [line.split(' -> ')]}


def make_polymer(steps=10):
    pairs = Counter(pairwise(template))

    for _ in range(steps):
        new = Counter()
        for pair, count in pairs.items():
            if ins := rules.get(''.join(pair)):
                new[pair[0] + ins] += count
                new[ins + pair[1]] += count
        pairs = new

    return pairs


def result(steps=10):
    counts = Counter()
    for pair, count in make_polymer(steps).items():
        counts[pair[0]] += count
        counts[pair[1]] += count
    counts[template[0]] += 1
    counts[template[-1]] += 1

    return (counts.most_common()[0][1] - counts.most_common()[-1][1]) // 2


# Part 1
# submit(result())

# Part 2
submit(result(40))
