

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
print("lowest point", lowest_point)
print("mat", mat)
is_full = False
nr_of_sand = 0
while not is_full:

    is_set = False
    should_add_to_mat = True
    sx, sy = (500, 0)
    while not is_set:
        # print("running")
        for nx,ny in [(sx, sy + 1), (sx - 1, sy + 1), (sx + 1, sy + 1)]:
            # print("nx", nx, "ny", ny)
            if (nx,ny) not in mat:
                # print("not in mat")
                sx = nx
                sy = ny
                # print("new sx", sx, "new sy", sy)
                should_add_to_mat = False

                if ny >= lowest_point:
                    print("hit lowest point")
                    is_full = True
                    is_set = True

                break

            if (nx, ny) in mat:
                # print("in mat", "nx", nx, "ny", ny)
                should_add_to_mat = True
                continue


        if should_add_to_mat:
            mat.add((sx,sy))
            # print("adding to mat, length of mat", len(mat))
            is_set = True
    
    nr_of_sand += 1

print(nr_of_sand - 1)
    







