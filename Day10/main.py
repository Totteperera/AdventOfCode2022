class Cpu:
    should_sum_at = (20, 60, 100, 140, 180, 220)

    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.sum = 0

    def do_noop(self):
        self.tick()

    def do_instruction(self, instruction: int):
        self.tick()
        self.tick()
        self.x += instruction

    def tick(self):
        self.cycle += 1
        self.check_if_should_sum()

    def check_if_should_sum(self):
        if(self.cycle in self.should_sum_at):
            self.sum += self.cycle * self.x 


f = open("input.txt")
cpu = Cpu()

for line in f:
    line = line.strip()
    print(line)

    if line == "noop":
        cpu.do_noop()
    else:
        cpu.do_instruction(int(line.split(" ")[1]))

print(cpu.sum)