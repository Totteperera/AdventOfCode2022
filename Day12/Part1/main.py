from colorama import init
import math

TRAVERSER_NAME_INDEX = 0

def print_chart(current_node, closed_list, open_list):
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

            elif (c_i,r_i) == open_list[0].position:
                color = '\x1b[6;30;43m' 

            if color == "":
                    print(chart[c_i][r_i], end="")
            else:
                    print(color + chart[c_i][r_i] + '\x1b[0m', end="", flush=True)
            
                
        print("")

def get_traverser_name():
    global TRAVERSER_NAME_INDEX
    index_name = TRAVERSER_NAME_INDEX
    TRAVERSER_NAME_INDEX += 1
    return "traverser" + str(index_name)

class Graph:
    def __init__(self, num_of_vertices):
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
    start_node.g = start_node.h = start_node.f = 0

    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = {}

    open_list.append(start_node)
    counter = 0
    while len(open_list) > 0:
        
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):

            if item.f < current_node.f:
                current_node = item
                current_index = index

        if counter % 1000 == 0:
            print(len(open_list), len(closed_list), open_list[0])
            print(current_node)
            print_chart(current_node, closed_list, open_list)

        # if len(open_list) == 1:
        #     print(len(open_list), len(closed_list), open_list[0])
        #     print(current_node)
        #     print(get_current_char(current_node.position))
        #     print_chart(current_node, closed_list, open_list)

        open_list.pop(current_index)
        closed_list[str(current_node)] = True
        if current_node == end_node:
            print_chart(current_node, closed_list, open_list)
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
            
            tentative_g_score = current_node.g + 1

            if(str(child) in closed_list and tentative_g_score >= child.g):
                continue

            should_add = True
            child.g = current_node.g + 1
            child.h = abs((child.position[0] - end_node.position[0])) + abs((child.position[1] - end_node.position[1]))
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g >= open_node.g:
                    should_add = False
                    continue

            if should_add:
                open_list.append(child)
                
        counter += 1

    print(open_list)

def get_current_char(current_pos: tuple) -> str:
    return chart[current_pos[0]][current_pos[1]]

def get_ascii_value(pos: tuple) -> int:
    current_char = get_current_char(pos)
    return ord(current_char) if current_char != "E" else ord("z") + 1

def is_next_step_valid(
    current_pos: tuple,
    next_pos: tuple) -> bool:
    if(get_current_char(current_pos) == "S" and get_current_char(next_pos) == "a"):
        return True

    diff_in_ascii = get_ascii_value(next_pos) - get_ascii_value(current_pos)
    return diff_in_ascii <= 1

init()
chart = []
starting_pos = ()
ending_pos = ()

with open("../input.txt") as f:
    for line in f:
        line = line.strip()
        new_list = list(line)

        chart.append(new_list)


for c_i in range(len(chart)):
    for r_i in range(len(chart[c_i])):
        if(chart[c_i][r_i] == "S"):
            starting_pos = (c_i, r_i)
        if(chart[c_i][r_i] == "E"):
            ending_pos = (c_i, r_i)

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
print(len(path))






