import sys
from collections import deque

class Node:
    def __init__(self, flow, path):
        self.flow = flow
        self.path = path

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


def dfs(current_valve: str, paths: list, open: set, minutes: int) -> Node:
    global current_max

    n = []

    if(minutes <= 0):
        return Node(0, paths)

    if(len(open) == nr_of_valves):
        return Node(0, paths)
    
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
        temp_path = list(paths)
        temp_path.append((c,minutes-am))

        flow_val = (fv*(minutes-am))

        if(flow_val < 0):
            continue

        test_node = g(c, temp_path, temp_o, (minutes-am))
        node = Node(flow_val + test_node.flow, test_node.path)
        temp.append(node)
    
    if(len(temp) == 0):
        return Node(0, paths)

    node = sorted(temp, key=lambda x: x.flow, reverse=True)[0]
    if node.flow > current_max:
        current_max = node.flow
        print("new max", current_max)

    return node

current_max = 0
open = set()
closed = set()

for v in valves:
    if valves[v].flow == 0:
        open.add(v)
    else:
        closed.add(v)

print(nr_of_valves)
max_flow = dfs(current_valve, [(current_valve, 30)], set(open), 30)
print(max_flow.flow)

for p,m in max_flow.path:
    print(p,m)

for key in valves:
    value = valves[key]
    if len(value.shortest):
        print(key, value.flow, value.shortest)