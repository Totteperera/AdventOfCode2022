import pprint

def manhatan_dist(x1, x2, y1, y2):
    return abs(x1-x2) + abs(y1-y2)

my_y = 2000000

x = [x.split(":") for x in open("../input.txt").read().strip().split("\n")]

sensor_to_beacons = {}

for t in x:    
    sx,sy = map(int, [x.split("=")[1] for x in t[0].split(",")])
    bx,by = map(int, [x.split("=")[1] for x in t[1].split(",")])
    sensor_to_beacons[(sx,sy)] = (manhatan_dist(sx, bx, sy, by), bx, by)

max_x = max([max(x[0], sensor_to_beacons[x][1]) for x in sensor_to_beacons])
min_x = min([min(x[0], sensor_to_beacons[x][1]) for x in sensor_to_beacons])
max_y = max([max(x[1], sensor_to_beacons[x][2]) for x in sensor_to_beacons])
min_y = min([min(x[1], sensor_to_beacons[x][2]) for x in sensor_to_beacons])

coverage = set()

for key in sensor_to_beacons:
    sx, sy = key

    # add sensor position
    coverage.add((sx,sy))

    up = (sx, sy + 1)
    down = (sx, sy - 1)
    left = (sx - 1, sy)
    right = (sx + 1, sy)

# up and down
    distance_to_beacon = sensor_to_beacons[key][0]
    for updown_i in range(distance_to_beacon):
    
        for nvx, nvy in [(sx, sy + updown_i), (sx, sy - updown_i)]:
            #left and right
            if nvy != my_y:
                continue

            for leftright_i in range(distance_to_beacon - updown_i):
                for nhx, nhy in [(sx - (leftright_i + 1), nvy), (sx + (leftright_i + 1), nvy)]:
                    coverage.add((nhx,nhy))
            coverage.add((nvx,nvy))


# print("max", max_x, max_y, "min", min_x, min_y)

print("test", sensor_to_beacons.values())
padding = 20
for y in range(min_y - padding, max_y + padding):
    for x in range(min_x - padding ,max_x + padding):

        if (x,y) in sensor_to_beacons:
            print(sensor_to_beacons[(x,y)][0], end="")
        elif (x,y) in [(x[1], x[2]) for x in sensor_to_beacons.values()]:
            print("B", end="")
        elif (x,y) in coverage:
            print("#", end="")
        else:
            print(" ", end="")
    print()

nr_of_spots = max_x - min_x
taken_spots =  list(filter(lambda x: x[1] == my_y, coverage))
b_at_my_y = set([(x[1],x[2]) for x in list(filter(lambda x: x[2] == my_y, sensor_to_beacons.values()))])

print(sensor_to_beacons.values())
print(len(taken_spots))
print(len(taken_spots) - len(b_at_my_y))


