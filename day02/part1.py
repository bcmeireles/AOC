with open("day02/input.in", "r") as f:
    data = f.readlines()

import re

possible = 0

for index, line in enumerate(data):
    red_total = map(int, re.findall(r"\d+(?= red)", line))
    green_total = map(int, re.findall(r"\d+(?= green)", line))
    blue_total = map(int, re.findall(r"\d+(?= blue)", line))
    
    if any(x > 12 for x in red_total):
        continue

    if any(x > 13 for x in green_total):
        continue

    if any(x > 14 for x in blue_total):
        continue

    possible += index + 1

print(possible)