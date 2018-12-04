import re
from collections import defaultdict, Counter

from aocd import data

log = sorted(data.splitlines())


# A

def get_shift_records():
    shift = []

    for record in log:
        if shift and '#' in record:
            yield shift
            shift = []
        shift.append(record)

    if shift:
        yield shift


guards = defaultdict(list)

for shift in get_shift_records():
    guard_id = int(re.search('#(\d+) ', shift[0]).group(1))

    sleep_times = []
    awake_times = []

    for record in shift[1:]:
        minutes = int(re.search('(\d+)]', record).group(1))
        if 'falls asleep' in record:
            sleep_times.append(minutes)
        elif 'wakes up' in record:
            awake_times.append(minutes)
        else:
            raise Exception

    guards[guard_id].extend(zip(sleep_times, awake_times))

protosphere = max(guards, key=lambda g: sum(awake - sleep for (sleep, awake) in guards[g]))
sleepiest_minute = Counter(m for (sleep, awake) in guards[protosphere] for m in range(sleep, awake)).most_common(1)[0][0]

print(protosphere * sleepiest_minute)


# B

def sleepiest_minute(bed_times):
    try:
        minute, count = Counter(m for (sleep, awake) in bed_times for m in range(sleep, awake)).most_common(1)[0]
    except IndexError:
        minute, count = 0, 0

    return minute, count


also_protosphere = max(guards, key=lambda g: sleepiest_minute(guards[g])[1])
sleepiest_minute = sleepiest_minute(guards[also_protosphere])[0]

print(also_protosphere * sleepiest_minute)
