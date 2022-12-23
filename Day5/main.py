
crates = [[]] * 9

f = open("input.txt")

for line in f:
    chars = list(line)
    crateIndex = 0
    counter = 1
    for c in chars:
        if (counter == 2):
            if (c != " "):
                if len(crates[crateIndex]) == 0:
                    crates[crateIndex] = [c]
                else:
                    currentList = crates[crateIndex]
                    currentList.append(c)
                    crates[crateIndex] = currentList
        if counter == 4:
            crateIndex += 1
            counter = 1
        else :
            counter += 1
    crateIndex = 0
# for l in crates:
#     l.reverse()

counter1 = 1
for l in crates:
    print('nr ', counter1)
    print(l)
    counter1 += 1

f.close()

f = open("input2.txt")

for instructionLine in f:
    instructionLine = instructionLine.strip()
    quantity = int(instructionLine.split("from")[0].replace("move", ""))
    fromCrate = int(instructionLine.split("from")[1].split("to")[0])
    toCrate = int(instructionLine.split("from")[1].split("to")[1])

    # print('moiving ', quantity, ' from ', fromCrate, " to ", toCrate)

    for index in range(quantity):
        movingValue = crates[fromCrate-1].pop(0)
        # print('moving value', movingValue) 
        crates[toCrate-1].insert(index, movingValue)

counter1 = 1
for l in crates:
    print('nr ', counter1)
    print(l)
    counter1 += 1
counter1 = 1

for l in crates:
    print(l[0], end='')
    counter1 += 1

f.close()