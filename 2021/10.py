from collections import deque
from statistics import median
from aocd import lines, submit

char_pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

# Part 1
syntax_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score = 0
for line in lines:
    stack = deque()
    for char in line:
        if char in char_pairs.keys():
            stack.append(char)
        elif char_pairs[stack.pop()] != char:
            score += syntax_points[char]
            break

# submit(score)

# Part 2
autocomplete_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []
for line in lines:
    stack = deque()
    for char in line:
        if char in char_pairs.keys():
            stack.append(char)
        elif char_pairs[stack.pop()] != char:
            break
    else:
        score = 0
        while stack:
            score = score * 5 + autocomplete_points[char_pairs[stack.pop()]]
        if score:
            scores.append(score)

submit(median(sorted(scores)))
