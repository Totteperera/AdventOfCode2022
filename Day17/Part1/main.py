import sys

filename = sys.argv[1]


def next_rock(y, counter):
    x = 2
    match counter % 5:
        case 0:
            return [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)]
        case 1:
            return [(x, y + 1), (x + 1, y), (x + 1, y + 1), (x + 1, y + 2), (x + 2, y + 1)]
        case 2:
            return [(x, y), (x + 1, y), (x + 2, y), (x + 2, y + 1), (x+2, y+2)]
        case 3:
            return [(x, y), (x, y+1), (x, y+2), (x, y+3)]
        case 4:
            return [(x, y), (x, y+1), (x+1, y), (x+1, y+1)]

def can_move_horizontally(jet, min_x, max_x):
    return wall_l <= min_x + jetsmap[jet] and wall_r >= max_x + jetsmap[jet]

jetsmap = {
    "<": -1,
    ">": 1
}

for line in open(filename):
    jets = list(line)

print(jets)

chamber_width = 7

solid = set([(x, 0) for x in range(chamber_width)])

wall_l = 0
wall_r = 6
max_y = 0

rocks_to_iterate = 2022
jet_counter = 0
for i in range(rocks_to_iterate):
    rock = next_rock(max_y + 4, i)

    rock_next_y = 1
    rock_next_x = 0
    rock_is_moving = True

    rock_max_x = max([x[0] for x in rock])
    rock_min_x = min([x[0] for x in rock])
    while rock_is_moving:
        jet = jets[jet_counter % len(jets)]
        # print("jet_counter  len(jets)", jet_counter % len(jets), jet, jetsmap[jet], "minx", rock_min_x)
        rock_next_x = jetsmap[jet]
        move_horizontally = True

        for rx,ry in rock:
            if not can_move_horizontally(jet, rock_min_x, rock_max_x) or (rx + rock_next_x, ry - (rock_next_y - 1)) in solid:
                move_horizontally = False
                break
                
        if move_horizontally:
            rock_max_x = 0
            rock_min_x = 7
            for ri in range(len(rock)):
                    rock_max_x = max(rock_max_x, rx + rock_next_x)
                    rock_min_x = min(rock_min_x, rx + rock_next_x)
                    rx, ry = rock[ri]
                    rock[ri] = (rx + rock_next_x, ry)

        for rx,ry in rock:
            if (rx, ry - rock_next_y) in solid:
                rock_is_moving = False        

        if not rock_is_moving:
            for rx,ry in rock:
                solid.add((rx,  ry - rock_next_y + 1))
                max_y = max(max_y, ry - rock_next_y + 1)

        rock_next_y += 1
        jet_counter += 1

        # for y in reversed(range(max_y + 6)):
        #     for x in range(-1, 8):
        #         if (x, y) in solid:
        #             print("#", end="")
        #         elif (x, y + rock_next_y -1 ) in rock:
        #             print("@", end="")
        #         elif x == -1 or x == 7:
        #             print("|" ,end = "")
        #         else:
        #             print(" ", end="")
        #     print()
        # print()

print(max_y)