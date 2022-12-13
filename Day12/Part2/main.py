from colorama import init
import math
from queue import PriorityQueue
from collections import deque

def print_chart(current_node, closed_list):
    path = {}
    current = current_node
    while current is not None:
        path[str(current.position)] = True
        current = current.parent

    for c_i in range(len(chart)):
        for r_i in range(len(chart[c_i])):
            color = ""
            if (c_i,r_i) == current_node.position:
                color = '\x1b[6;30;44m'
            elif(str((c_i,r_i)) in path):
                color = '\x1b[6;30;45m'  

            elif(str((c_i,r_i)) in closed_list):
                color = '\x1b[6;30;42m'

            if color == "":
                    print(chart[c_i][r_i], end="")
            else:
                    print(color + chart[c_i][r_i] + '\x1b[0m', end="", flush=True)
            
                
        print("")

class Node:
    def __init__(self, parent = None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other) -> bool:
        return self.position == other.position

    def __str__(self) -> str:
        return str(self.position)


def astar(start, end):
    start_node = Node(None, start)

    queue = deque()
    queue.append((0, start_node))
    visited = {str(start_node)}
    counter = 0

    while queue:
        dist, current_node = queue.popleft()
        if counter % 1000 == 0:
            print_chart(current_node, visited)

        if current_node.position in end:
            print_chart(current_node, visited)
            print("FOUND PATH")
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        current_pos = current_node.position

        # not outside bounds north and valid
        next_pos = (current_pos[0] - 1, current_pos[1])
        if(current_pos[0] - 1 >= 0 and is_next_step_valid(current_pos, next_pos)):
            children.append(Node(current_node, next_pos))
        # not outside bounds south and valid
        next_pos = (current_pos[0] + 1, current_pos[1])
        if(current_pos[0] + 1 <= max_c_index and is_next_step_valid(current_pos, next_pos)):
            children.append(Node(current_node, next_pos))
            
        next_pos = (current_pos[0], current_pos[1] -1)
        if(current_pos[1] - 1 >= 0 and is_next_step_valid(current_pos, next_pos)):
            children.append(Node(current_node, next_pos))
            
        next_pos = (current_pos[0], current_pos[1] + 1)
        if(current_pos[1] + 1 <= max_r_index and is_next_step_valid(current_pos, next_pos)):
            children.append(Node(current_node, next_pos))

        for child in children:

            if str(child) in visited:
                continue

            visited.add(str(child))
            queue.append((dist+1 , child))

        counter += 1

def get_current_char(current_pos: tuple) -> str:
    return chart[current_pos[0]][current_pos[1]]

def get_ascii_value(pos: tuple) -> int:
    current_char = get_current_char(pos)
    return ord(current_char)

def is_next_step_valid(
    current_pos: tuple,
    next_pos: tuple) -> bool:

    diff_in_ascii = get_ascii_value(current_pos) - get_ascii_value(next_pos)
    return diff_in_ascii <= 1

init()
chart = []
starting_pos = ()
ending_pos = set()

with open("../input.txt") as f:
    for line in f:
        line = line.strip()
        new_list = list(line)

        chart.append(new_list)


for c_i in range(len(chart)):
    for r_i in range(len(chart[c_i])):
        if(chart[c_i][r_i] == "a"):
            ending_pos.add((c_i, r_i))
        if(chart[c_i][r_i] == "E"):
            chart[c_i][r_i] = "z"
            starting_pos = (c_i, r_i)

current_pos = starting_pos


for c_i in range(len(chart)):
    for r_i in range(len(chart[c_i])):
        print(chart[c_i][r_i], end="")

    print("")

results = []
max_c_index = len(chart) - 1
max_r_index = len(chart[0]) -1 

print("starting pos", starting_pos)
print("ending pos", ending_pos)
path = astar(starting_pos, ending_pos)

print(path)
print(len(path) -1 )






