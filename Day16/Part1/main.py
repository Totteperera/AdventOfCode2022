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


totals = 0


a = {("a", 1),("a", 2), ("a", 20), ("a", 4), ("a", 28)}

print(sorted(a, key=lambda x : x[1]))
minutes_to_open_valve = 1

while minutes > 0:

    open = [] 

    for v in valves:
        if valves[v].flow != 0 and not valves[v].open:

            action_minutes = shortest_path(current_valve, v) + minutes_to_open_valve
            shortest = shortest_path(current_valve, v)
            open.append((v, (valves[v].flow * (minutes - (shortest*2) + minutes_to_open_valve)), action_minutes))


    if(len(open) == 0):
        print(totals)
        exit(1)

    open = sorted(open, key=lambda x: x[1], reverse=True)
    print(open)

    current_valve, _ , action_minutes = open[0]
    minutes = minutes - action_minutes

    if(minutes <= 0):
        print(totals)
        exit(1)
    

    totals += valves[current_valve].flow * minutes
    valves[current_valve].open = True

    print("current valve", current_valve)