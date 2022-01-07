from functools import cache
from itertools import product
from operator import add
from aocd import lines, submit

p1_start = int(lines[0].split()[-1])
p2_start = int(lines[1].split()[-1])

# Part 1
die = 0


def roll():
    global die
    die += 1
    if die > 100:
        die = 1
    return die


def play_deterministic():
    p1_space = p1_start
    p2_space = p2_start
    p1_score = 0
    p2_score = 0
    current_player = 1
    rolls = 0

    while p1_score < 1000 and p2_score < 1000:
        r = 0
        for i in range(3):
            r += roll()
            rolls += 1
        if current_player == 1:
            p1_space = (p1_space + r - 1) % 10 + 1
            p1_score += p1_space
            current_player = 2
        else:
            p2_space = (p2_space + r - 1) % 10 + 1
            p2_score += p2_space
            current_player = 1

    return min(p1_score, p2_score) * rolls


# submit(play_deterministic())


# Part 2
roll_values = tuple(map(sum, product((1, 2, 3), repeat=3)))


@cache
def play_dirac(p1_space, p2_space, p1_score, p2_score, current_player):
    if p1_score >= 21:
        return 1, 0
    elif p2_score >= 21:
        return 0, 1

    wins = (0, 0)
    for r in roll_values:
        if current_player == 1:
            p1sp = (p1_space + r - 1) % 10 + 1
            wins = tuple(map(add, wins, play_dirac(p1sp, p2_space, p1_score + p1sp, p2_score, 2)))
        else:
            p2sp = (p2_space + r - 1) % 10 + 1
            wins = tuple(map(add, wins, play_dirac(p1_space, p2sp, p1_score, p2_score + p2sp, 1)))
    return wins


submit(max(play_dirac(p1_start, p2_start, 0, 0, 1)))
