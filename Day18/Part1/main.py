import sys
filename = sys.argv[1]

lines = [x.split(",") for x in open(filename).read().split("\n")]

index = [[] for x in range(len(lines))]
print(index)

for li, line in enumerate(lines):

    x, y, z = line

    for other_li, other_line in enumerate(lines):
        if other_li == li:
            continue

        matches = [set(x) for x in zip(line, other_line)]

        if len(list(filter(lambda x: len(x) == 1, matches))) == 2:

            not_same = tuple(list(filter(lambda x: len(x) == 2, matches))[0])
            if abs(int(not_same[0]) - int(not_same[1])) == 1:
                index[li].append(other_li)

sides = sum([len(x) for x in index])

print((len(lines))*6 - sides)
