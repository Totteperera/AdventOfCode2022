import math

class Monkey:
    def __init__(
        self,
        starting_items: list,
        get_new_worry_level,
        divisble_by: int,
        send_to_if_true: int,
        send_to_if_false: int):
    
        self.starting_items = starting_items
        self.get_new_worry_level = get_new_worry_level
        self.divisble_by = divisble_by
        self.send_to_if_true = send_to_if_true
        self.send_to_if_false = send_to_if_false
        self.has_sent = 0

    def receive(self, item: int):
        self.starting_items.append(item)

    def get_receiving_monkey_number(self, divisible_nr: int) -> int:
        return self.send_to_if_true if divisible_nr % int(self.divisble_by) == 0 else self.send_to_if_false

    def add_sent(self):
        self.has_sent += 1

    def clear(self):
        self.starting_items = []

def get_starting_items(line: str) -> list:
    return list(map(lambda x: int(x.strip()), list(line.split(":")[1].split(","))))

def get_operation(line: str):
    right_values = line.split("=")[1].split(" ")

    operation = right_values[-2]

    def operation_function(old: int):
        operation_value = old if right_values[-1] == "old" else int(right_values[-1])
        print("operation_value", operation_value)
        result = 0
        print("operation,", operation)
        if(operation == "+"):
            result = old + operation_value
        else:
            result = old * operation_value

        return math.floor(result / 3)

    return operation_function

def get_divisible_by(line: str) -> int:
    return int(line.split(" ")[-1])

def get_send_to_if_true(line: str) -> int:
    return int(line.split(" ")[-1])

def get_send_to_if_false(line: str) -> int:
    return int(line.split(" ")[-1])

monkeys = []

with open("../input.txt") as f:

    for line in f:
        line = line.strip()

        if line.startswith("Monkey"):
            monkeys.append(
                Monkey(
                    get_starting_items(f.readline()),
                    get_operation(f.readline().strip()),
                    get_divisible_by(f.readline().strip()),
                    get_send_to_if_true(f.readline().strip()),
                    get_send_to_if_false(f.readline().strip())
                )
            )


nr_of_rounds = 20

for i in range(nr_of_rounds):
    for monkey_index in range(len(monkeys)):
        monkey = monkeys[monkey_index]
        print("monkey ", monkey_index, "has worry levels", *monkey.starting_items)
        for worry_level in monkey.starting_items:
            new_worry_level = monkey.get_new_worry_level(worry_level)
            print("round ", i, "new worry level", new_worry_level)
            monkey_to_send_to_index = monkey.get_receiving_monkey_number(new_worry_level)
            print("monkey_to_send_to_index", monkey_to_send_to_index)
            monkeys[monkey_to_send_to_index].receive(new_worry_level)
            monkey.add_sent()
        monkey.clear()
        for m in monkeys:
            print(m.starting_items)

sorted_monkeys = sorted(monkeys, key= lambda x: x.has_sent)

print(sorted_monkeys[-1].has_sent * sorted_monkeys[-2].has_sent)