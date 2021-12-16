from dataclasses import dataclass
from aocd import lines, submit


@dataclass
class Cell:
    risk: int
    distance: int = None
    visited: bool = False


def neighbours(x, y, area):
    res = []
    for i in (-1, 1):
        nx = x + i
        ny = y + i
        if 0 <= nx < len(area[0]):
            res.append((nx, y))
        if 0 <= ny < len(area):
            res.append((x, ny))
    return res


def smallest_risk(area=lines):
    cavern = {(x, y): Cell(int(risk)) for y, line in enumerate(area) for x, risk in enumerate(line)}
    cavern[0, 0].distance = 0
    to_visit = {(0, 0)}
    end_cell = cavern[len(area[0]) - 1, len(area) - 1]

    while end_cell.visited is False:
        cur = min(to_visit, key=lambda c: cavern[c].distance)
        cur_cell = cavern[cur]
        for neighbour in neighbours(*cur, area):
            neighbour_cell = cavern[neighbour]
            if neighbour_cell.visited is False:
                dist = cur_cell.distance + neighbour_cell.risk
                if neighbour_cell.distance is None or dist < neighbour_cell.distance:
                    to_visit.add(neighbour)
                    neighbour_cell.distance = dist
        cur_cell.visited = True
        to_visit.remove(cur)

    return end_cell.distance


# Part 1
# submit(smallest_risk())

# Part 2
full_area = ''
for y in range(5):
    for line in lines:
        for x in range(5):
            for char in line:
                risk = int(char) + x + y
                if risk > 9:
                    risk -= 9
                full_area += str(risk)
        full_area += '\n'

submit(smallest_risk(full_area.splitlines()))
