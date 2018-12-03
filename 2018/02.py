from collections import Counter

from aocd import data

ids = data.splitlines()


# A

twos = sum(1 for id_ in ids if 2 in Counter(id_).values())
threes = sum(1 for id_ in ids if 3 in Counter(id_).values())

checksum = twos * threes
print(checksum)


# B
# This would be a lot easier if I used zip, so naturally I decided to avoid it.

correct_id_detective = (id_ for id_ in ids
                        if any(other_id for other_id in ids
                               if sum(1 for i, char in enumerate(id_) if char != other_id[i]) == 1)
                        )

correct_id1 = next(correct_id_detective)
correct_id2 = next(correct_id_detective)

common_list = [char for i, char in enumerate(correct_id1) if char == correct_id2[i]]
common = ''.join(common_list)

print(common)
