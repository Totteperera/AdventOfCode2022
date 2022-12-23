from colorama import init
import math

moves = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0, 1),
    "D": (0,-1)
}

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}-{self.y}"

    def move(self, tup: tuple):
        self.x += tup[0]
        self.y += tup[1]

def is_adjacent(
        tail: Coordinate,
        head: Coordinate) -> bool:

    return abs(head.x - tail.x) <= 1 and abs(head.y - tail.y) <= 1

def get_tail(
    tail: Coordinate,
    head: Coordinate
) -> Coordinate:
    if not is_adjacent(tail, head):
        x_diff = (head.x - tail.x) / 2
        y_diff = (head.y - tail.y) / 2
        x_diff = math.ceil(x_diff) if x_diff > 0 else math.floor(x_diff)
        y_diff = math.ceil(y_diff) if y_diff > 0 else math.floor(y_diff)
        tail.move((x_diff, y_diff))
    return tail

def get_tail_index_at(
    knots: list,
    x: int,
    y: int
) -> int:
    for i in range(len(knots)):
        if(knots[i].x == x and knots[i].y == y):
            return i
    return -1

def print_result(knots: list, tail_has_been_at):
    grid_length_y = 120
    grid_length_y_m = 20
    grid_length_x = 120
    grid_length_x_m = 20

    for i in range(grid_length_y, -grid_length_y_m ,-1):
        for j in range(-grid_length_x_m, grid_length_x):
            tail_index = get_tail_index_at(knots, j, i)
            if(i == knots[0].y and j == knots[0].x):
                print('\x1b[1;37;43m' + "H" + '\x1b[0m' , end= " ", flush=True)
            elif (tail_index != -1):
                print('\x1b[1;37;44m' + str(tail_index) + '\x1b[0m', end= " ", flush=True)
            elif(f"{j}-{i}" in tail_has_been_at):
                print('\x1b[6;30;42m' + '+' '\x1b[0m', end= " ", flush=True)
            else:
                print("+", end= " ", flush=True)
        print("\n")


f = open("input.txt")
init()

knots = [
    Coordinate(0, 0),
    Coordinate(0, 0),
    Coordinate(0, 0),
    Coordinate(0, 0),
    Coordinate(0, 0),
    Coordinate(0, 0),
    Coordinate(0, 0),
    Coordinate(0, 0),
    Coordinate(0, 0),
    Coordinate(0, 0)
    ]

tail_has_been_at = {"0-0"}

for line in f:
    path = line[0]

    for i in range(int(line.split(" ")[1])):
        knots[0].move(moves[path])

        for index_knot in range(len(knots) - 1):
            knots[index_knot + 1] = get_tail(knots[index_knot + 1], knots[index_knot])

        tail_has_been_at.add(f"{knots[-1]}")


print(len(tail_has_been_at))
#print_result(knots, tail_has_been_at)



