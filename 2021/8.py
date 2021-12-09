from collections import Counter
from aocd import lines, submit

entries = [[part.split() for part in line.split('|')] for line in lines]
unique = [2, 3, 4, 7]

# Part 1
outputs = [val for e in entries for val in e[1]]
# submit(len(list(filter(lambda o: len(o) in unique, outputs))))


# Part 2
def translate(string, translation_map):
    return ''.join(translation_map[c] for c in string)


def subtract_from_string(string, remove, translation_map):
    reverse_translations = {v: k for k, v in translation_map.items()}
    return ''.join(c for c in string if c not in translate(remove, reverse_translations))


outputs = []
segments = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
count_map = {4: 'e', 6: 'b', 9: 'f'}
unique_replace_map = {2: ('f', 'c'), 3: ('cf', 'a'), 4: ('bcf', 'd'), 7: ('abcdef', 'g')}
for e in entries:
    translations = {}
    counter = Counter(''.join(e[0]))
    for letter, count in counter.items():
        if translated_letter := count_map.get(count):
            translations[letter] = translated_letter
    for digit in sorted(e[0], key=len):
        if ur := unique_replace_map.get(len(digit)):
            translations[subtract_from_string(digit, ur[0], translations)] = ur[1]
    outputs.append(int(''.join(
        str(segments.index(''.join(
            sorted(translate(c, translations) for c in digit)
        ))) for digit in e[1]
    )))

submit(sum(outputs))
