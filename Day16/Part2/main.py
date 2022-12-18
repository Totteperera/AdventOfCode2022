import sys
from collections import deque

class ValveMap:
    def __init__(self, open, flow, paths) -> None:
        self.open = open
        self.flow = flow
        self.paths = paths
        self.shortest = {}

file_name = sys.argv[1]
line = [x.replace(",", "").split(";") for x in open(file_name).read().split("\n")]

valves = {}
current_valve = "AA"


for left, right in line:
    right = right.replace("valves", "valve")
    left = left.split(" ")
    open = False

    valves[left[1]] = ValveMap(open, int(left[-1].split("=")[-1]), [x for x in right.split("valve")[-1].strip().split(" ")])

minutes = 30
nr_of_valves = len(valves)


def shortest_path(start, dest):
    q = deque()
    vis = { start }
    
    distance = 0
    q.append((distance,start))

    while q:

        distance, current_valve = q.popleft()

        for path in valves[current_valve].paths:

            if path == dest:
                return distance + 1 

            if path not in vis:
                q.append((distance + 1, path))


def dfs(current_valve: str, open: set, minutes: int):
    global current_max

    n = []

    if(minutes <= 0):
        return 0

    if(len(open) == nr_of_valves):
        return 0
    
    for v in closed:
        if v not in open:
            if v in valves[current_valve].shortest:
                action_minutes = valves[current_valve].shortest[v] + 1
            else:
                shortest = shortest_path(current_valve, v)
                valves[current_valve].shortest[v] = shortest
                action_minutes = shortest + 1

            n.append((v, valves[v].flow, action_minutes))
        
    temp = []
    for c,fv,am in n:
        temp_o = set(open)
        temp_o.add(c)

        flow_val = (fv*(minutes-am))

        if(flow_val < 0):
            continue
       
        temp.append( flow_val + dfs(c, temp_o, (minutes-am)))
    
    if(len(temp) == 0):
        return 0

    value = sorted(temp, reverse=True)[0]
    if value > current_max:
        current_max = value
        print("new max", current_max)

    return value

current_max = 0
open = set()
closed = set()

for v in valves:
    if valves[v].flow == 0:
        open.add(v)
    else:
        closed.add(v)

print(nr_of_valves)
print(dfs(current_valve, set(open), 30))

for key in valves:
    value = valves[key]
    if len(value.shortest):
        print(key, value.flow, value.shortest)