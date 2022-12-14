input = [str(x).split("->") for x in open("../input.txt").read().strip().split("\n")]

mat = set()

for row in input:
    old = ()
    for c in row:
        x,y = map(int, c.strip().split(","))        

        if old:
            ox, oy = old
            if ox == x:
                starting_from = min(oy, y)
                for i in range(abs(y - oy)):
                    mat.add((x, starting_from + i))
            else:
                starting_from = min(ox, x)
                for i in range(abs(x - ox)):
                    mat.add((starting_from + i, y))

        mat.add((x,y))
        old = (x,y)

lowest_point = max([x[1] for x in mat])
bottom_y = lowest_point + 2

for i in range(100000):
    mat.add((i,bottom_y))

is_full = False
nr_of_sand = 0
while not is_full:

    is_set = False
    should_add_to_mat = True
    sx, sy = (500, 0)

    if (sx, sy) in mat:
        is_full = True

    while not is_set:
        for nx,ny in [(sx, sy + 1), (sx - 1, sy + 1), (sx + 1, sy + 1)]:
            if (nx,ny) not in mat:
                sx = nx
                sy = ny
                should_add_to_mat = False
                break

            if (nx, ny) in mat:
                should_add_to_mat = True
                continue


        if should_add_to_mat:
            mat.add((sx,sy))
            is_set = True
    
    nr_of_sand += 1

print(nr_of_sand - 1)