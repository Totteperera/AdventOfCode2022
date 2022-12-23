def all_chars_different(
    chars: list(),
    startIndex: int,
    endIndex: int):
    valuesInRange = {}
    for index in range(startIndex, endIndex + 1):
        valuesInRange[chars[index]] = True
    print(valuesInRange, 'startIndex', startIndex , 'endIndex', endIndex)
    return len(valuesInRange) == 14

def get_marker_index(
    chars: list()) :
    endIndex = 13
    lengthOfChars = len(chars)
    for index in range(lengthOfChars) :
        if(endIndex > lengthOfChars):
            break
        if(all_chars_different(chars, index, endIndex)) :
            return endIndex
        endIndex += 1

f = open("input.txt")

line = f.readline()
chars = list(line)

print(get_marker_index(chars) + 1)

