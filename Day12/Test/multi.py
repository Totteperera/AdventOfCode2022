import multiprocessing as mp

TRAVERSER_NAME_INDEX = 0

def get_traverser_name():
    global TRAVERSER_NAME_INDEX
    index_name = TRAVERSER_NAME_INDEX
    TRAVERSER_NAME_INDEX += 1
    return "traverser" + str(index_name)

class Traverser:
    def __init__(self, steps, has_been):
        self.steps = steps
        self.has_been = has_been
        self.name = get_traverser_name()

def get_current_char(current_pos: tuple) -> str:
    return chart[current_pos[0]][current_pos[1]]

def get_ascii_value(pos: tuple) -> int:
    current_char = get_current_char(pos)
    return ord(current_char) if current_char != "E" else ord("z") + 1

def is_next_step_valid(
    current_traverser: Traverser,
    current_pos: tuple,
    next_pos: tuple) -> bool:
    if(get_current_char(current_pos) == "S"):
        return True

    return get_ascii_value(next_pos) - get_ascii_value(current_pos) <= 1 and next_pos not in current_traverser.has_been

def test_going_places(
    current_traverser: Traverser,
    current_pos: tuple
):
    global results
    current_traverser.has_been[current_pos] = True

    if(get_current_char(current_pos) == "E"):
        print("FOUND E!!!!")
        results.append(current_traverser)
        return

    if(TRAVERSER_NAME_INDEX % 100000 == 0):
        print("traverser",current_traverser.name, "current pos", get_current_char(current_pos), current_traverser.steps,"has been" ,len(current_traverser.has_been))

    # not outside bounds north and valid
    next_pos = (current_pos[0] - 1, current_pos[1])
    if(current_pos[0] - 1 >= 0 and is_next_step_valid(current_traverser, current_pos, next_pos)):
        # print("up , next pos", get_current_char(next_pos))
        mp.Process(test_going_places(Traverser(current_traverser.steps + 1, dict(current_traverser.has_been)), next_pos)).start()

    # not outside bounds south and valid
    next_pos = (current_pos[0] + 1, current_pos[1])
    if(current_pos[0] + 1 <= max_c_index and is_next_step_valid(current_traverser, current_pos, next_pos)):
        # print("down , next pos", get_current_char(next_pos))
        mp.Process(test_going_places(Traverser(current_traverser.steps + 1, dict(current_traverser.has_been)), next_pos)).start()

    next_pos = (current_pos[0], current_pos[1] -1)
    if(current_pos[1] - 1 >= 0 and is_next_step_valid(current_traverser, current_pos, next_pos)):
        # print("left, next pos", get_current_char(next_pos))
        mp.Process(test_going_places(Traverser(current_traverser.steps + 1, dict(current_traverser.has_been)), next_pos)).start()

    next_pos = (current_pos[0], current_pos[1] + 1)
    if(current_pos[1] + 1 <= max_r_index and is_next_step_valid(current_traverser, current_pos, next_pos)):
        # print("right, next pos", get_current_char(next_pos))
        mp.Process(test_going_places(Traverser(current_traverser.steps + 1, dict(current_traverser.has_been)), next_pos)).start()

    # print("we reached the end", current_traverser.name, get_current_char(current_pos), "has been", len(current_traverser.has_been))
    return


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


print(ord("b"))

results = []
max_c_index = len(chart) -1 
max_r_index = len(chart[0]) -1

print(len(list("abccccccccccccccccccccaaaaacccaaaaaaaaaaaacccccccccaacaacccccccccccccccccccccccccccccccccaaaaaa")) * 20)
exit(1)

test_going_places(Traverser(0, {}), current_pos)

print(min(map(lambda x : x.steps, results)))





