
f = open("input.txt")

elfs = []

calories = 0
for line in f:
    if line == "\n":
        elfs.append(calories)
        calories = 0
    else:
        calories += int(line)

elfs.sort(reverse=True)
print(elfs[0] + elfs[1] + elfs[2])

    

