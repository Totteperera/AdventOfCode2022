
def is_visible_down(current_grid: list, index: int, current_row: list, row_index: int) -> int:
    result = 0
    for i in range(index + 1, len(current_grid)):
        if(current_row[row_index] <= current_grid[i][row_index]):
            result += 1
            return result
        if(current_row[row_index] > current_grid[i][row_index]):
            result +=1
    return result

def is_visible_up(current_grid: list, index: int, current_row: list, row_index: int) -> int:
    result = 0
    array_to_operate = []

    for i in range(index):
        array_to_operate.append(current_grid[i][row_index])

    if(len(array_to_operate) > 1):
        array_to_operate.reverse()

    for i in range(len(array_to_operate)):
        if(current_row[row_index] <= array_to_operate[i]):
            result += 1
            return result
        if(current_row[row_index] > array_to_operate[i]):
            result += 1

    return result

def is_visible_left(current_row: list, row_index: int) -> int:

    result = 0
    array_to_operate = list(current_row[0:row_index])
    if(len(array_to_operate) > 1):
        array_to_operate.reverse()

    for i in range(len(array_to_operate)):
        if(current_row[row_index] <= array_to_operate[i]):
            result += 1
            return result
        if(current_row[row_index] > array_to_operate[i]):
            result +=1

    return result

def is_visible_right(current_row: list, row_index: int) -> int:
    result = 0
    array_to_operate = list(current_row[row_index + 1:len(current_row)])
    print("right array", array_to_operate)
    for i in range(len(array_to_operate)):
        if(current_row[row_index] <= array_to_operate[i]):
            result += 1
            return result
        if(current_row[row_index] > array_to_operate[i]):
            result += 1

    return result


def get_is_visible(current_grid: list, index: int, current_row: list, row_index: int) -> int:
    right = is_visible_right(current_row, row_index)
    left = is_visible_left(current_row, row_index)
    up = is_visible_up(current_grid, index, current_row, row_index)
    down = is_visible_down(current_grid, index, current_row, row_index)

    print("checking", index, row_index)
    print("right", right)
    print("left", left)
    print("up", up)
    print("down", down)


    return right * left * up * down

f = open("input.txt", "r")

current_grid = []

for line in f:
    current_grid.append(list(line.strip()))

print(current_grid)

tree_counter = 0
line_counter = 0

for index in range(1, len(current_grid) - 1):
    current_row = current_grid[index]
    for row_index in range(1, len(current_row) - 1):
        visible_score = get_is_visible(
            current_grid, index, current_row, row_index)
        if(visible_score > tree_counter):
            tree_counter = visible_score

# tree_counter += len(current_grid) * 2  + len(current_grid[0]) * 2 -4

print(tree_counter)