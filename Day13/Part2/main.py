import math
def compare_arrays_in_right_order(first, second):

    if type(first) == int:
        if type(second) == int:
            return first - second
        else:
            return compare_arrays_in_right_order([first], second)
    else:
        if type(second) == int:
            return compare_arrays_in_right_order(first, [second])
        
    for z_first, z_second in zip(first, second):
        result = compare_arrays_in_right_order(z_first, z_second)
        if result:
            return result
    
    return len(first) - len(second)

lines = []

with open("../input.txt") as f:
    for line in f:
        if line.startswith("["):
            lines.append((line.strip()))

sorted_list = []

the_sum = 0
to_sum = []

for i, line in enumerate(lines):
    value = eval(line)

    if len(sorted_list) == 0:
        sorted_list.append(value)
        continue
    was_added = False
    for sorted_index, sorted_value in enumerate(sorted_list):
        if(compare_arrays_in_right_order(sorted_value, value) > 0):
            sorted_list.insert(sorted_index, value)
            was_added = True
            break
    
    if not was_added:
        sorted_list.append(value)

for i,s in enumerate(sorted_list):
    if s == [[6]] or s == [[2]]:
        to_sum.append(i+1)
    print(s)

print(math.prod(to_sum))




