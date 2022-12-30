import sys
import re
import multiprocessing
filename = sys.argv[1]

ORE = "o"
CLAY = "c"
OBSIDIAN = "ob"
GEODE = "g"


def can_build_robot(robot: dict, packing: dict):
    can_build = True
    for k, v in robot.items():
        if packing[k] < v:
            can_build = False

    return can_build

def gather(packing: dict, robots: dict):
    temp = {}

    for robot_id, gatherers in robots.items():
        temp[robot_id] = packing[robot_id] + gatherers

    return temp

def use(packing: dict, robot_value: dict):
    temp = {}
    for k, v in packing.items():
        temp[k] = v

    for item_id, item_value in robot_value.items():
        temp[item_id] = packing[item_id] - item_value

    return temp


def construct_robot(robots: dict, id: str):
    temp = {}
    for k, v in robots.items():
        additional = 0
        if k == id:
            additional = 1

        temp[k] = v + additional
    return temp


def f(x):

    robots, packing, minutes, blueprint, blueprint_robots, cache = x
    c_key = (str(robots), str(packing), minutes)

    if c_key in cache:
        return (cache[c_key], blueprint)

    if minutes == 0:
        return (packing, blueprint)

    alternatives = []

    # append no build option
    alternatives.append((dict(robots), gather(packing, robots), minutes - 1, blueprint, blueprint_robots, cache))

    for robot_id, robot_value in blueprint_robots.items():
        if can_build_robot(robot_value, packing):
            alternatives.append((
                construct_robot(robots, robot_id),
                gather(use(packing, blueprint_robots[robot_id]), robots),
                minutes - 1,
                blueprint,
                blueprint_robots,
                cache
            ))

    returned = max([f(x) for x in alternatives], key=lambda x: x[0][GEODE])
    cache[c_key] = returned[0]

    return (returned[0],blueprint)

total = 0
inputs = []
blueprint_robots = {}
cache = {}

if __name__ == "__main__":

    for line in open(filename).read().strip().split("\n"):
        left = line.split(":")[0]
        right = line.split(":")[1]

        blueprint = int(re.findall("\d+", left)[0])
        cache[blueprint] = {}

        print("blueprint", blueprint)

        robot_texts = right.split(".")

        blueprint_robots = {
            GEODE: {
                ORE: int(re.findall("\d+", robot_texts[3])[0]),
                OBSIDIAN: int(re.findall("\d+", robot_texts[3])[1])
            },
            OBSIDIAN: {
                ORE: int(re.findall("\d+", robot_texts[2])[0]),
                CLAY: int(re.findall("\d+", robot_texts[2])[1])
            },
            CLAY: {
                ORE: int(re.findall("\d+", robot_texts[1])[0])
            },
            ORE: {
                ORE: int(re.findall("\d+", robot_texts[0])[0])
            }
        }

        packing = {
            ORE: 0,
            CLAY: 0,
            OBSIDIAN: 0,
            GEODE: 0
        }

        robots = {
            ORE: 1,
            CLAY: 0,
            OBSIDIAN: 0,
            GEODE: 0
        }

        inputs.append((dict(robots), dict(packing), 24, blueprint, blueprint_robots, {}))

    pool = multiprocessing.Pool()

    result = pool.map(f, inputs)
    test = sum([x[0][GEODE]*x[1] for x in result])
    print(test)