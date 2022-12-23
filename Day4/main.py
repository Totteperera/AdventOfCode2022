
f = open("input.txt")
counter = 0
for line in f:
    line = line.strip()
    pairs = line.split(",")
    first = pairs[0].split("-")
    second = pairs[1].split("-")

    if int(first[0]) < int(second[0]) and int(first[1]) < int(second[0]) :
        print('#first', first, ' second', second)
        continue
    elif int(first[0]) > int(second[0]) and int(second[1]) < int(first[0]) :
        print('##first', first, ' second', second)
        continue

#first ['7', '79']  second ['8', '78']
    # print("match!")
    counter += 1

print(counter)
    