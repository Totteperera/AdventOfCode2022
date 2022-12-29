import sys
import re
from collections import deque
filename = sys.argv[1]


def can_build_robot(robot: dict):
    can_build = True
    for k, v in robot.items():
        if packing[k] < v:
            can_build = False

    return can_build

def can_soon_build_robot(robot: dict):    
    can_build = True
    for k, v in robot.items():
        if packing[k] + robots[k] * 2 < v:
            can_build = False

    return can_build

for line in open(filename).read().strip().split("\n"):
    left = line.split(":")[0]
    right = line.split(":")[1]

    blueprint = re.findall("\d+", line.split(":")[0])[0]
    print("blueprint", blueprint)

    robot_texts = right.split(".")

    blueprint_robots = {
        "geode": {
            "ore": int(re.findall("\d+", robot_texts[3])[0]),
            "obsidian": int(re.findall("\d+", robot_texts[3])[1])
        },
        "obsidian": {
            "ore": int(re.findall("\d+", robot_texts[2])[0]),
            "clay": int(re.findall("\d+", robot_texts[2])[1])
        },
        "clay": {
            "ore": int(re.findall("\d+", robot_texts[1])[0])
        },
        "ore": {
            "ore": int(re.findall("\d+", robot_texts[0])[0])
        }
    }

    packing = {
        "ore": 0,
        "clay": 0,
        "obsidian": 0,
        "geode": 0
    }

    robots = {
        "ore": 1,
        "clay": 0,
        "obsidian": 0,
        "geode": 0
    }

    construction_line = deque()

    for i in range(24):
        print("------ minute", i + 1)

        print("ROBOTS:\n")
        for k,v in robots.items():
            print(k + ":",v)
        print()

        print("PACKAGING\n")
        for k,v in packing.items():
            print(k + ":",v)
        print()


        # add to construction line
        for robot_id, robot_value in blueprint_robots.items():

            if can_build_robot(robot_value):
                print("Adding", robot_id, "to construction line")
                construction_line.append(robot_id)

                for item_key, item_value in robot_value.items():
                    print("spending", item_value, "of", item_key)
                    packing[item_key] -= item_value

                break

            if can_soon_build_robot(robot_value):
                print("can soon build", robot_id)
                break

        # gather
        for robot_id, robot_value in robots.items():
            print("gather", robot_value, "of", robot_id)
            packing[robot_id] += robot_value
            
        print("PACKAGING\n")
        for k,v in packing.items():
            print(k + ":",v)
        print()
        
        # build
        while construction_line:
            new_robot_id = construction_line.popleft()
            print(new_robot_id, "added")
            robots[new_robot_id] += 1

    print("total geode:", packing["geode"])
    print("\n\n\n")