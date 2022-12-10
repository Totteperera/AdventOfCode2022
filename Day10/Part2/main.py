from colorama import init

class Crt:
    def print_(self, c: int, x: int):
        cycle_v = c % 40
        if cycle_v == 0:
            print('')
        elif(cycle_v in [x, x+1, x+2]):
            print('\x1b[1;37;42m' + "#" + '\x1b[0m', end="")
        else:
            print(".", end="")

class Clock:
    def __init__(self):
        self.cycle = 0
        self.x = 1
    
    def tick(self):
        self.cycle += 1
        crt.print_(self.cycle, self.x)

class Cpu:
    def do_noop(self):
        clock.tick()

    def do_instruction(self, instruction: int):
        clock.tick()
        clock.tick()
        clock.x += instruction

f = open("../input.txt")
init()
crt = Crt()
clock = Clock()
cpu = Cpu()

for line in f:
    line = line.strip()

    if line == "noop":
        cpu.do_noop()
    else:
        cpu.do_instruction(int(line.split(" ")[1]))