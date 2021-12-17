from aocd import data, submit

xmin, xmax = tuple(map(int, data.split()[2].split('=')[1][:-1].split('..')))
ymin, ymax = tuple(map(int, data.split()[3].split('=')[1].split('..')))

highest_y = -9999
successful_launches = 0

for x in range(1, xmax+1):
    for y in range(ymin, -ymin):
        step = 1
        vx = x
        vy = y
        cur_x = 0
        cur_y = 0
        cur_highest_y = -9999
        while True:
            cur_x += vx
            cur_y += vy
            cur_highest_y = max(cur_y, cur_highest_y)
            if xmin <= cur_x <= xmax and ymin <= cur_y <= ymax:
                highest_y = max(cur_highest_y, highest_y)
                successful_launches += 1
                break
            if cur_x > xmax or cur_y < ymin:
                break
            vx = max(vx-1, 0)
            vy -= 1

# Part 1
# submit(highest_y)

# Part 2
submit(successful_launches)
