dict = {
    "A": [
        8,
        4,
        3
    ],
    "B": [
        9,
        5,
        1,
    ],
    "C": [
        7,
        6,
        2,
    ]
}

mapping = {
    "X": 2,
    "Y": 1,
    "Z": 0
}

f = open("input.txt")
result = 0

for line in f:
    input = line.split()
    result += dict[input[0]][mapping[input[1]]]

print(result)
