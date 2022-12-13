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

pairs = []

with open("../input.txt") as f:
    for line in f:
        if line.startswith("["):
            pairs.append((line.strip(), f.readline().strip()))

index_position = 0

p1_values = []
p2_values = []

the_sum = 0

for i, (p1, p2) in enumerate(pairs):

    returned_value = compare_arrays_in_right_order(eval(p1), eval(p2))
    if(returned_value < 0):
        the_sum += i+1

print(the_sum)



