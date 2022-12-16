import pprint

def manhatan_dist(x1, x2, y1, y2):
    return abs(x1-x2) + abs(y1-y2)

at_most = 4000000
at_least = 0

line = [x.split(":") for x in open("../input.txt").read().strip().split("\n")]

sensor_to_beacons = {}

possible_b = set()

for t in line:
    sx,sy = map(int, [l.split("=")[1] for l in t[0].split(",")])
    bx,by = map(int, [l.split("=")[1] for l in t[1].split(",")])

    sensor_to_beacons[(sx,sy)] = manhatan_dist(sx, bx, sy, by)

    current_manhattan = manhatan_dist(sx, bx, sy, by) 

    for mhi in range(current_manhattan):
        up_right = (sx + current_manhattan + 1 - mhi, sy + mhi)
        up_left = (sx - current_manhattan + 1 - mhi, sy + mhi)
        down_right = (sx + current_manhattan + 1 - mhi, sy - mhi)
        down_left = (sx - current_manhattan + 1 - mhi, sy - mhi)

        for nx,ny in [up_right, up_left, down_right, down_left]:
            
            if(ny < at_least or ny > at_most or nx < at_least or nx > at_most):
                continue

            possible_b.add((nx,ny))
            
    #add edges up and down
    possible_b.add((sx, sy + (current_manhattan + 1)))
    possible_b.add((sx, sy - (current_manhattan + 1)))


for x,y in possible_b:
    if(x < at_least or x > at_most or y < at_least or y > at_most):
        continue

    if all([manhatan_dist(x, sx, y, sy) > sensor_to_beacons[(sx,sy)] for sx,sy in sensor_to_beacons]):
        print(x, y)
        print(x * 4000000 + y)
