import math

class Monkey:
    def __init__(
        self,
        starting_items: list,
        get_new_worry_level : function,
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


def get_starting_items(line: str) -> list:
    return list(map(lambda x: int(x.strip()), list(line.split(":")[1].split(","))))

def get_operation(line: str) -> function:

    right_values = line.split("=")[1].split(" ")

    operation_value = int(right_values[-1])
    operation = right_values[1]

    def operation(old: int):
        result = 0
        if(operation == "+"):
            result = old + operation_value
        else:
            result = old * operation_value

        return math.floor(result / 3)

    return operation()

def get_divisible_by(line: str) -> int:
    return line.split(" ")[-1]

def get_send_to_if_true(line: str) -> int:
    return line.split(" ")[-1]

def get_send_to_if_false(line: str) -> int:
    return line.split(" ")[-1]

monkeys = []

with open("../input.txt") as f:

    for line in f:
        line = line.strip()

        if line.startswith("Monkey"):
            monkeys.append(
                Monkey(
                    get_starting_items(f.readline()),
                    get_operation(f.readline()),
                    get_divisible_by(f.readline),
                    get_send_to_if_true(f.readline),
                    get_send_to_if_false(f.readline)
                )
            )


nr_of_rounds = 20

for i in range(nr_of_rounds):
    for monkey in monkeys:
        for worry_level in monkey.starting_items:
            new_worry_level = monkey.get_new_worry_level(worry_level)
            