with open("day02/input.in", "r") as f:
    data = f.readlines()

import re

powersum = 0

for index, line in enumerate(data):
    red_total = max(map(int, re.findall(r"\d+(?= red)", line)))
    green_total = max(map(int, re.findall(r"\d+(?= green)", line)))
    blue_total = max(map(int, re.findall(r"\d+(?= blue)", line)))

    power = red_total * blue_total * green_total

    powersum += power

print(powersum)