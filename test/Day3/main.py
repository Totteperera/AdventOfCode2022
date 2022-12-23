def is_matching(first, chars):
    for j in range(len(chars)):
        if (first == chars[j]):
            return True

    return False


def run(groupItems):
    line = groupItems[0]
    chars = list(line)
    nrOfChars = len(chars)

    for i in range(nrOfChars):
        if is_matching(chars[i], list(groupItems[1])) and is_matching(chars[i], list(groupItems[2])):
            return priority.index(chars[i])


priority = ["0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
            "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

f = open("input.txt")
matches = []
groupItems = []
counter = 1

for line in f:
    if (counter % 3 == 0):
        groupItems.append(line.strip())
        matches.append(run(groupItems))
        groupItems = []
    else:
        groupItems.append(line.strip())
    
    counter += 1

print(matches)
print(sum(matches))
