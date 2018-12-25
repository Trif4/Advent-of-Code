from collections import defaultdict
from dataclasses import dataclass
from string import ascii_uppercase

from aocd import data


def get_step_requirement_dict():
    step_requirements = defaultdict(list)

    for line in data.splitlines():
        step = line[36]
        req = line[5]

        if req not in step_requirements:
            # Ensure that all steps have a key
            step_requirements[req] = []

        step_requirements[step].append(req)

    return step_requirements


# A

step_requirements = get_step_requirement_dict()

res = ''
ready_steps = [step for step, requirements in step_requirements.items() if not requirements]

while ready_steps:
    ready_steps.sort()
    next_step = ready_steps.pop(0)

    for s, r in step_requirements.items():
        if next_step in r:
            r.remove(next_step)

            if not r:
                ready_steps.append(s)

    res += next_step

print(res)


# B

@dataclass
class Worker:
    step: str
    time_left: int


workers = [Worker(None, None) for i in range(5)]

step_requirements = get_step_requirement_dict()
ready_steps = [step for step, requirements in step_requirements.items() if not requirements]

seconds = 0


while True:
    for worker in workers:
        if worker.step:
            worker.time_left -= 1

            if worker.time_left == 0:
                for s, r in step_requirements.items():
                    if worker.step in r:
                        r.remove(worker.step)

                        if not r:
                            ready_steps.append(s)

                worker.step = None

        if not worker.step:
            if ready_steps:
                ready_steps.sort()
                next_step = ready_steps.pop(0)

                worker.step = next_step
                worker.time_left = 60 + ascii_uppercase.index(next_step) + 1

    if any(w.step for w in workers):
        seconds += 1
    else:
        break

print(seconds)
