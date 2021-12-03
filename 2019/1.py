from aocd import data, submit

sum = 0

for i in data.splitlines():
    a = i
    while a != 0:
        a = max(int(a)//3-2, 0)
        sum += a

submit(sum)
