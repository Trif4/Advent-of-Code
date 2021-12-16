from math import prod
from aocd import data, submit

bits = bin(int(data, 16))[2:].zfill(4*len(data))
version_sum = 0


def read_packet(index):
    version, type_id, cur = read_header(index)
    if type_id == 4:
        return read_literal(cur)
    else:
        return read_operator(cur, type_id)


def read_header(index):
    version = int(bits[index:index+3], 2)
    type_id = int(bits[index+3:index+6], 2)
    global version_sum
    version_sum += version
    return version, type_id, index + 6


def read_literal(index):
    cur = index
    val = ''
    while True:
        group = bits[cur:cur+5]
        val += group[1:]
        cur += 5
        if group[0] == '0':
            break
    return int(val, 2), cur


def read_operator(index, type_id):
    length_type = bits[index]
    subpacket_values = []
    if length_type == '0':
        data_length = int(bits[index+1:index+16], 2)
        cur = index + 16
        while cur < index + 16 + data_length:
            val, cur = read_packet(cur)
            subpacket_values.append(val)
    else:
        packets = int(bits[index+1:index+12], 2)
        cur = index + 12
        for _ in range(packets):
            val, cur = read_packet(cur)
            subpacket_values.append(val)

    match type_id:
        case 0:
            val = sum(subpacket_values)
        case 1:
            val = prod(subpacket_values)
        case 2:
            val = min(subpacket_values)
        case 3:
            val = max(subpacket_values)
        case 5:
            val = 1 if subpacket_values[0] > subpacket_values[1] else 0
        case 6:
            val = 1 if subpacket_values[0] < subpacket_values[1] else 0
        case 7:
            val = 1 if subpacket_values[0] == subpacket_values[1] else 0
        case _:
            raise ValueError

    return val, cur


res = read_packet(0)[0]

# Part 1
# submit(version_sum)

# Part 2
submit(res)
