from collections import deque

class ValveMap:
    def __init__(self, open, flow, paths) -> None:
        self.open = open
        self.flow = flow
        self.paths = paths

line = [x.replace(",", "").split(";") for x in open("../input.txt").read().split("\n")]

valves = {}
current_valve = "AA"


for left, right in line:
    right = right.replace("valves", "valve")
    left = left.split(" ")
    open = False

    if left[1] == "AA":
        open = True

    valves[left[1]] = ValveMap(open, int(left[-1].split("=")[-1]), [x for x in right.split("valve")[-1].strip().split(" ")])

minutes = 30
nr_of_valves = len(valves)

def tick():
    global minutes
    minutes -= 1
    print("TICK MINUTES ARE NOW", minutes)

def get_next_valve_flow(valve, minutes, visited):

    # print("RUNNING", valve, minutes, visited)
    if minutes <= 0 or len(visited) == nr_of_valves:
        return 0 

    if valve in visited:
        return max([get_next_valve_flow(path, minutes - 1, set(visited)) for path in valves[valve].paths])

    visited.add(valve)
    return valves[valve].flow * minutes + max([get_next_valve_flow(path, minutes - 2, set(visited)) for path in valves[valve].paths])


visited = {"AA"}

for v in valves:
    if valves[v].flow == 0:
        visited.add(v)

totals = set()


q = deque()

# this is not working very well..
# kolla i day 12 och använd den algon med lite adjustments

print(get_next_valve_flow("AA", 30, visited))
exit(1)


while minutes > 0:
    next_valve_flow = 0
    next_valve = ""
    print("current valve", current_valve)
    for path in valves[current_valve].paths:
        flow_value = get_next_valve_flow(path, minutes - 2)

        if(flow_value > next_valve_flow):
            next_valve_flow = flow_value
            current_valve = path

    print("next valve", current_valve, next_valve_flow)

    if not valves[current_valve].open and valves[current_valve].flow > 0:
        tick()

        if(minutes == 0):
            break

        valves[current_valve].open = True
        totals.add(minutes * valves[current_valve].flow)
        print("totals", totals)

    tick()
    
print(totals)




