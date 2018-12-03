import re
from collections import Counter

from aocd import data


class Claim:
    def __init__(self, definition):
        self.id, self.x, self.y, self.width, self.height = [int(i) for i in re.findall('\d+', definition)]
        self.positions = set()


class ClaimedPosition:
    def __init__(self, x, y, claim):
        self.x, self.y, self.claim = x, y, claim
        self.claim.positions.add(self)


claims = [Claim(line) for line in data.splitlines()]


# A

claimed_positions = set()

for claim in claims:
    for i in range(claim.width):
        for j in range(claim.height):
            p = ClaimedPosition(claim.x + i, claim.y + j, claim)
            claimed_positions.add(p)

claimed_positions_counter = Counter((p.x, p.y) for p in claimed_positions)
contested_square_inches = sum(1 for i in claimed_positions_counter.values() if i > 1)

print(contested_square_inches)


# B

claim_without_overlap = next(c for c in claims if all(claimed_positions_counter[p.x, p.y] == 1 for p in c.positions))

print(claim_without_overlap.id)
