import sys
filename = sys.argv[1]

lines = [x.split(",") for x in open(filename).read().split("\n")]

a = [1,2,3]
b = [2,2,3]
c = zip(a,b)

index = {}

for li,line in enumerate(lines):
    x,y,z = line

    for other_li, other_line in enumerate(lines):
        if other_li == li:
            continue

        matches = [set(x) for x in zip(line, other_line)]
        
        if len(list(filter(lambda x: len(x) == 1, matches))) == 2:
            index[li] = index[li].append(li)
            # we have hit, save to index

        ox,oy,oz = other_line

        matching = 0

print(index)