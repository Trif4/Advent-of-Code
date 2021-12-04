from itertools import chain
from aocd import data, submit

numlist, *boardsstr = data.split('\n\n')
numbers = list(map(int, numlist.split(',')))
boards = [[list(map(int, row.split())) for row in board.splitlines()] for board in boardsstr]


def bingo(find_last=False):
    won_boards = []
    for i, n in enumerate(numbers):
        print(n)
        for b in boards:
            if find_last and b in won_boards:
                continue
            for r in b + list(map(list, zip(*b))):
                for x in r:
                    # i'm 14 and this is deep
                    if x not in numbers[0:i+1]:
                        break
                else:
                    if find_last and len(boards) - len(won_boards) > 1:
                        won_boards.append(b)
                        break
                    else:
                        unmarked = [x for x in chain(*b) if x not in numbers[0:i+1]]
                        return sum(unmarked) * n


# Part 1
# submit(bingo())

# Part 2
submit(bingo(find_last=True))
