with open("day08/input.in", "r") as f:
    data = f.readlines()
                
paths = {}

for line in data[2:]:
    line = line.strip().split(" ")
    paths[line[0]] = {
        "L": line[2][1:-1],
        "R": line[3][:-1]
    }

currents = [x for x in paths.keys() if x[-1] == "A"]

path = data[0].strip()
costs = []

for current in currents:
    i = 0
    while True:
        current = paths[current][path[i % len(path)]]
        i += 1
        if current[-1] == "Z":
            costs.append(i)
            break

import math
print(math.lcm(*costs))